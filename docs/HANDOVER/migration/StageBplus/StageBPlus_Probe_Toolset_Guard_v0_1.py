#!/usr/bin/env python3
"""Stage B+ disposable MSBuild toolset guard probe, v0.1.

Run in an ordinary Windows CMD prompt (not VsDevCmd):
  python StageBPlus_Probe_Toolset_Guard_v0_1.py StageBPlus_CANDIDATE_FOR_CLAUDE_v0_2.zip

Reads candidate ZIP, creates test projects under %TEMP%, and verifies the
real inspector project evaluation plus its exact minimum-v145 guard target.
Does NOT modify any Git repository or invoke a compiler/linker.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import zipfile

ZIP_NAME = "StageBPlus_CANDIDATE_FOR_CLAUDE_v0_2.zip"
PROJECT_NAME = "Mpeg2BlockInspector.vcxproj"
TARGET_NAME = "BPlus_MinimumPlatformToolset"
REQUIRED = {
    "v145": (True, None),
    "v143": (False, "v145 or newer"),
    "v150": (True, None),
    "vX": (False, "resolved numeric"),
    "": (False, "resolved numeric"),
}


def checked_run(label: str, command: list[str], expected: bool,
                must_contain: str | None = None) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(command, text=True, capture_output=True, errors="replace")
    combined = (proc.stdout + "\n" + proc.stderr).strip()
    okay = (proc.returncode == 0) == expected
    if must_contain and must_contain not in combined:
        okay = False
    print(f"{'PASS' if okay else 'FAIL'} {label}: return code {proc.returncode}"
          + (f" [expected {'0' if expected else 'nonzero'}]"))
    if not okay:
        print("  COMMAND:", subprocess.list2cmdline(command))
        print("  OUTPUT:\n" + combined[-9000:])
        raise RuntimeError(f"Probe failed: {label}")
    return proc


def read_candidate(path: Path) -> tuple[bytes, str]:
    with zipfile.ZipFile(path) as zf:
        bad = zf.testzip()
        if bad is not None:
            raise RuntimeError(f"Corrupt ZIP entry: {bad}")
        names = set(zf.namelist())
        if PROJECT_NAME not in names or "PACKAGE_SHA256.txt" not in names:
            raise RuntimeError("The reviewed flat ZIP is missing project or SHA manifest")
        manifest = zf.read("PACKAGE_SHA256.txt").decode("ascii")
        for line in manifest.splitlines():
            line = line.strip()
            if not line:
                continue
            match = re.fullmatch(r"([a-fA-F0-9]{64})\s+(.+)", line)
            if match is None:
                raise RuntimeError("Malformed candidate SHA-256 inventory")
            want, filename = match.groups()
            if filename not in names:
                raise RuntimeError(f"Missing inventoried file: {filename}")
            found = hashlib.sha256(zf.read(filename)).hexdigest()
            if found.lower() != want.lower():
                raise RuntimeError(f"Candidate SHA mismatch: {filename}")
        project = zf.read(PROJECT_NAME)
    if project.count(b"<PlatformToolset>$(DefaultPlatformToolset)</PlatformToolset>") != 2:
        raise RuntimeError("Expected two default-toolset project properties")
    text = project.decode("ascii")
    begin = text.find('<Target Name="' + TARGET_NAME + '"')
    if begin < 0:
        raise RuntimeError("Target not found in project")
    end = text.find("</Target>", begin)
    if end < 0:
        raise RuntimeError("Unclosed target in project")
    target = text[begin:end + len("</Target>")]
    if "VersionLessThan" not in target or "Regex" not in target:
        raise RuntimeError("Unexpected target contents")
    return project, target


def find_msbuild() -> tuple[Path, dict]:
    pf86 = os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")
    vswhere = Path(pf86) / "Microsoft Visual Studio" / "Installer" / "vswhere.exe"
    if not vswhere.is_file():
        raise RuntimeError(f"VS discovery tool not found: {vswhere}")
    proc = checked_run("vswhere", [str(vswhere), "-latest", "-products", "*",
                    "-requires", "Microsoft.Component.MSBuild",
                    "Microsoft.VisualStudio.Component.VC.Tools.x86.x64",
                    "-format", "json", "-utf8"], True)
    installed = json.loads(proc.stdout.lstrip("\ufeff"))
    if len(installed) != 1 or installed[0].get("isPrerelease", False):
        raise RuntimeError("Expected one latest released qualifying VS installation")
    vs = installed[0]
    msbuild = (Path(vs["installationPath"]) / "MSBuild" / "Current"
               / "Bin" / "amd64" / "MSBuild.exe")
    if not msbuild.is_file():
        raise RuntimeError(f"x64 MSBuild not found: {msbuild}")
    print("Visual Studio:", vs.get("displayName"), vs.get("installationVersion"))
    print("MSBuild:", msbuild)
    return msbuild, vs


def main() -> int:
    if os.name != "nt" or sys.maxsize < 2**32:
        raise RuntimeError("This probe must run on 64-bit Windows Python")
    if any(k.startswith("VSCMD_ARG_") for k in os.environ):
        raise RuntimeError("Use a plain CMD prompt, not a VsDevCmd environment")
    if len(sys.argv) != 2:
        print("Usage: python StageBPlus_Probe_Toolset_Guard_v0_1.py " + ZIP_NAME)
        return 2
    path = Path(sys.argv[1]).resolve()
    if not path.is_file():
        raise RuntimeError(f"Candidate ZIP not found: {path}")
    project, target = read_candidate(path)
    print("PASS ZIP integrity and SHA-256 package inventory:", path)
    msbuild, _ = find_msbuild()

    # All generated files are disposed on exit. No repository files are touched.
    with tempfile.TemporaryDirectory(prefix="StageBPlus_guard_") as temp:
        root = Path(temp)
        real_project = root / PROJECT_NAME
        real_project.write_bytes(project)
        standalone = root / "guard-only.proj"
        standalone.write_text(
            '<?xml version="1.0" encoding="utf-8"?>\n'
            '<Project xmlns="http://schemas.microsoft.com/developer/msbuild/2003">\n'
            + target.replace("\r\n", "\n") + '\n</Project>\n', encoding="ascii", newline="\r\n")

        # Evaluate the *reviewed* candidate project, imported VS C++ property files,
        # both configurations, without compiling or linking anything.
        observed = {}
        for cfg in ("Debug", "Release"):
            base = [str(msbuild), str(real_project), "-nologo", "-noAutoResponse",
                    f"-p:Configuration={cfg}", "-p:Platform=x64"]
            prop = checked_run(f"{cfg} property evaluation", base + [
                "-getProperty:PlatformToolset,DefaultPlatformToolset"], True)
            try:
                properties = json.loads(prop.stdout)["Properties"]
                selected = properties["PlatformToolset"]
                default = properties["DefaultPlatformToolset"]
            except (KeyError, ValueError, TypeError) as err:
                raise RuntimeError(f"Unexpected MSBuild property format: {prop.stdout}") from err
            print(f"  {cfg}: DefaultPlatformToolset={default!r}, PlatformToolset={selected!r}")
            if not re.fullmatch(r"v[0-9]+", selected) or selected != default:
                raise RuntimeError(f"{cfg} resolved toolset != default numeric toolset")
            if int(selected[1:]) < 145:
                raise RuntimeError(f"{cfg} resolved below minimum v145")
            observed[cfg] = selected
            checked_run(f"{cfg} REAL candidate guard", base + [
                f"-t:{TARGET_NAME}", "-v:minimal"], True)

        # Use exact Guard Target extracted from the reviewed candidate in an
        # import-free scratch .proj: v150 can be tested even if not installed.
        for value, (expect_pass, msg) in REQUIRED.items():
            tag = value or "<empty>"
            command = [str(msbuild), str(standalone), "-nologo", "-noAutoResponse",
                       f"-t:{TARGET_NAME}", "-v:minimal"]
            # Omitting the property altogether exercises a truly empty value.
            if value:
                command.append(f"-p:PlatformToolset={value}")
            checked_run(f"ISOLATED EXACT target PlatformToolset={tag}",
                        command, expect_pass, msg)
        print("FINAL RESULT: PASS (no project build, no repository modifications)")
        print("Resolved tools: Debug=" + observed["Debug"] + ", Release=" + observed["Release"])
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print("FINAL RESULT: FAIL:", str(exc), file=sys.stderr)
        raise SystemExit(1)
