# How MediaInfo Maps Your Some Usual Requested Characteristics
# 
# | Characteristic            | MediaInfo Stream & Parameter                   | Typical Values / Format                                              |
# | :------------------------ | :--------------------------------------------- | :------------------------------------------------------------------- |
# | **Width**                 | `Stream.Video`, `"Width"`                      | `720`, `1920`, `1280`, etc.                                          |
# | **Height**                | `Stream.Video`, `"Height"`                     | `480`, `576`, `1080`, etc.                                           |
# | **CFR or VFR**            | `Stream.Video`, `"FrameRate_Mode"`             | `CFR`, `VFR`                                                         |
# | **Framerate**             | `Stream.Video`, `"FrameRate"`                  | `29.970`, `25.000`, `23.976`                                         |
# | **Framerate Numerator**   | `Stream.Video`, `"FrameRate_Num"`              | `30000`, `25`, `24000`                                               |
# | **Framerate Denominator** | `Stream.Video`, `"FrameRate_Den"`              | `1001`, `1`                                                          |
# | **NTSC or PAL**           | `Stream.Video`, `"Standard"`                   | `NTSC`, `PAL`, `SECAM` (or deduced from fps/lines if header omitted) |
# | **Scan Type**             | `Stream.Video`, `"ScanType"`                   | `Interlaced`, `Progressive`, `MBAFF`                                 |
# | **Field Order**           | `Stream.Video`, `"ScanOrder"`                  | `TFF` (Top Field First), `BFF` (Bottom Field First)                  |
# | **Bitrate**               | `Stream.Video`, `"BitRate"` & `"BitRate_Mode"` | `6000000` bps / `CBR` or `VBR`                                       |
# | **Extra Handy Info**      | DAR, PAR, Duration, Audio tracks, Colorimetry  | `DisplayAspectRatio/String`, `Duration/String3`, etc.                |
# 
# Important Windows / Python 3.8+ Detail
# In Python 3.8 and later on Windows, Python tightened DLL loading security. Even
# if MediaInfo.dll is in the same directory or on your system PATH, ctypes.windll
# will not look there unless you explicitly register the folder with
# os.add_dll_directory() before loading MediaInfoDLL3.
#

import os
import sys
import argparse
from pathlib import Path
from fractions import Fraction

vapoursynth_path = r"D:\TEST\Vapoursynth_x64_R81"

# ==============================================================================
# Setup DLL search path and load MediaInfoDLL3
# ==============================================================================
dll_search_dirs = [
    Path(__file__).parent.resolve(),
    Path(vapoursynth_path),
]

# Add directory to Windows DLL search path (Python 3.8+)
for d in dll_search_dirs:
    if d.is_dir():
        if str(d) not in sys.path:
            sys.path.insert(0, str(d))
        if hasattr(os, "add_dll_directory") and (d / "MediaInfo.dll").exists():
            try:
                os.add_dll_directory(str(d))
            except Exception:
                pass

try:
    from MediaInfoDLL3 import MediaInfo, Stream
except ImportError as err:
    print(f"Error importing MediaInfoDLL3: {err}")
    print("Ensure MediaInfoDLL3.py and MediaInfo.dll are in the same folder or Python path.")
    sys.exit(1)


def deduce_standard(raw_standard: str, fps_str: str, height_str: str) -> str:
    """Return explicit standard if present, or deduce PAL vs NTSC from fps/height."""
    if raw_standard.strip():
        return raw_standard.strip()

    try:
        fps = round(float(fps_str), 3)
        h = int(height_str)
        if fps in (25.0, 50.0) or h in (576, 288):
            return "PAL (deduced from fps/height)"
        elif fps in (23.976, 24.0, 29.97, 59.94, 60.0) or h in (480, 240):
            return "NTSC (deduced from fps/height)"
        else:
            return "Neither / Non-standard"
    except (ValueError, TypeError):
        return "Neither / Unknown"


def deduce_fps_fraction(fps_str: str, num_str: str, den_str: str):
    """Return numerator and denominator even if stream headers omit them."""
    if num_str and den_str:
        return num_str, den_str

    try:
        fps = round(float(fps_str), 3)
        table = {
            23.976: (24000, 1001),
            24.000: (24, 1),
            25.000: (25, 1),
            29.970: (30000, 1001),
            30.000: (30, 1),
            50.000: (50, 1),
            59.940: (60000, 1001),
            60.000: (60, 1),
        }
        if fps in table:
            num, den = table[fps]
            return str(num), str(den)
        frac = Fraction(fps).limit_denominator(1001)
        return str(frac.numerator), str(frac.denominator)
    except Exception:
        return num_str or "N/A", den_str or "N/A"


def inspect_file(filepath: Path):
    mi = MediaInfo()
    # Always pass absolute Windows path string
    if not mi.Open(str(filepath.resolve())):
        print(f"\n[ERROR] Unable to open: {filepath.name}")
        return

    video_count = mi.Count_Get(Stream.Video)
    if video_count == 0:
        print(f"\n[SKIP] {filepath.name} (No video stream found)")
        mi.Close()
        return

    # --- Video Stream 0 Properties ---
    v_format      = mi.Get(Stream.Video, 0, "Format")          # e.g. MPEG Video
    v_version     = mi.Get(Stream.Video, 0, "Format_Version")  # e.g. Version 2
    v_profile     = mi.Get(Stream.Video, 0, "Format_Profile")  # e.g. Main@Main
    width         = mi.Get(Stream.Video, 0, "Width")
    height        = mi.Get(Stream.Video, 0, "Height")
    dar           = mi.Get(Stream.Video, 0, "DisplayAspectRatio/String")
    par           = mi.Get(Stream.Video, 0, "PixelAspectRatio")
    
    fps_mode      = mi.Get(Stream.Video, 0, "FrameRate_Mode")   # CFR / VFR
    fps           = mi.Get(Stream.Video, 0, "FrameRate")
    fps_num       = mi.Get(Stream.Video, 0, "FrameRate_Num")
    fps_den       = mi.Get(Stream.Video, 0, "FrameRate_Den")
    fps_num, fps_den = deduce_fps_fraction(fps, fps_num, fps_den)

    raw_standard  = mi.Get(Stream.Video, 0, "Standard")
    standard      = deduce_standard(raw_standard, fps, height)

    scan_type     = mi.Get(Stream.Video, 0, "ScanType")         # Interlaced / Progressive
    scan_order    = mi.Get(Stream.Video, 0, "ScanOrder")        # TFF / BFF
    scan_order_s  = mi.Get(Stream.Video, 0, "ScanOrder/String") # Top Field First, etc.

    if scan_type.lower() == "interlaced":
        field_order = f"{scan_order} ({scan_order_s})" if scan_order else (scan_order_s or "Unknown")
    else:
        field_order = "N/A (Progressive)"

    bitrate_mode  = mi.Get(Stream.Video, 0, "BitRate_Mode")     # CBR / VBR
    bitrate_str   = mi.Get(Stream.Video, 0, "BitRate/String")   # e.g. 6 000 kb/s
    bitrate_max   = mi.Get(Stream.Video, 0, "BitRate_Maximum/String")

    # --- Additional Useful Info ---
    duration      = mi.Get(Stream.General, 0, "Duration/String3") # HH:MM:SS.mmm
    file_size     = mi.Get(Stream.General, 0, "FileSize/String")
    container     = mi.Get(Stream.General, 0, "Format")           # MPEG-PS, MPEG-TS, etc.
    frame_count   = mi.Get(Stream.Video, 0, "FrameCount")
    chroma        = mi.Get(Stream.Video, 0, "ChromaSubsampling")  # 4:2:0
    bit_depth     = mi.Get(Stream.Video, 0, "BitDepth")           # 8 bit
    color_space   = mi.Get(Stream.Video, 0, "ColorSpace")         # YUV
    matrix        = mi.Get(Stream.Video, 0, "matrix_coefficients")

    # Audio Stream summary
    audio_count = mi.Count_Get(Stream.Audio)
    audio_summary = []
    for a_idx in range(audio_count):
        a_fmt = mi.Get(Stream.Audio, a_idx, "Format")
        a_ch  = mi.Get(Stream.Audio, a_idx, "Channels/String")
        a_sr  = mi.Get(Stream.Audio, a_idx, "SamplingRate/String")
        a_br  = mi.Get(Stream.Audio, a_idx, "BitRate/String")
        a_lang = mi.Get(Stream.Audio, a_idx, "Language/String") or "und"
        audio_summary.append(f"#{a_idx+1}: {a_fmt} {a_ch} @ {a_sr}, {a_br} [{a_lang}]")

    mi.Close()

    # --- Print Clean Formatted Report ---
    sep = "=" * 75
    print(sep)
    print(f"File: {filepath.name}")
    print(f"Path: {filepath}")
    print("-" * 75)
    print(f"  Container / Codec     : {container} | {v_format} {v_version} ({v_profile})")
    print(f"  Dimensions (W x H)    : {width} x {height} (DAR {dar}, PAR {par})")
    print(f"  Frame Rate Mode       : {fps_mode or 'CFR'}")
    print(f"  Frame Rate            : {fps} fps (Num: {fps_num} / Den: {fps_den})")
    print(f"  Standard              : {standard}")
    print(f"  Scan Type             : {scan_type}")
    print(f"  Field Order           : {field_order}")
    print(f"  Video Bitrate         : {bitrate_str or 'N/A'} ({bitrate_mode or 'N/A'}" +
          (f", Max: {bitrate_max})" if bitrate_max else ")"))
    print(f"  Duration / Frames     : {duration or 'N/A'} ({frame_count or 'N/A'} frames)")
    print(f"  Color Space / Matrix  : {color_space} {chroma} {bit_depth}-bit | Matrix: {matrix or 'Default'}")
    print(f"  File Size             : {file_size}")
    if audio_summary:
        print(f"  Audio Streams ({audio_count})     : {audio_summary[0]}")
        for extra_a in audio_summary[1:]:
            print(f"                          {extra_a}")
    else:
        print(f"  Audio Streams         : None")


def main():
    parser = argparse.ArgumentParser(
        description="EXAMPLE Inspect characteristics of MPEG-2 (.mpg) video files using MediaInfo.dll."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=".",
        help="Folder containing .mpg files (defaults to current folder)."
    )
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Search subdirectories recursively."
    )
    parser.add_argument(
        "--ext",
        nargs="+",
        default=[".mpg", ".mpeg", ".m2v"],
        help="File extensions to scan (default: .mpg .mpeg .m2v)"
    )

    args = parser.parse_args()
    folder_path = Path(args.folder).resolve()

    if not folder_path.exists() or not folder_path.is_dir():
        print(f"Error: Folder does not exist: {folder_path}")
        sys.exit(1)

    extensions = [ext.lower() if ext.startswith(".") else f".{ext.lower()}" for ext in args.ext]
    glob_pattern = "**/*" if args.recursive else "*"
    files = [f for f in folder_path.glob(glob_pattern) if f.is_file() and f.suffix.lower() in extensions]

    if not files:
        print(f"No matching files found in: {folder_path} with extensions {extensions}")
        return

    print(f"Found {len(files)} file(s) in {folder_path}\n")
    for file in sorted(files):
        inspect_file(file)
    print("=" * 75)


if __name__ == "__main__":
    main()

# 
# Assuming you mean MediaInfoDLL3.py (from your directory listing), it is the
# ctypes wrapper bridge that connects your Python script to the compiled C++
# library (MediaInfo.dll).
# 
# 1. The 3-Layer Architecture
# 
# When you run the Python code, the components work together across three distinct
# layers:
# 
# ┌────────────────────────────────────────────────────────┐
# │  inspect_mpeg2.py  (Your Python Code)                  │
# │  - Calls mi.Get(Stream.Video, 0, "Width")              │
# └──────────────────────────┬─────────────────────────────┘
#                            │
#                            ▼
# ┌────────────────────────────────────────────────────────┐
# │  MediaInfoDLL3.py  (The ctypes Wrapper / Bridge)       │
# │  - Converts Python strings & ints to C-level types     │
# │  - Marshals wide-character pointers (wchar_t*)         │
# │  - Defines Stream enums (General=0, Video=1, Audio=2)  │
# └──────────────────────────┬─────────────────────────────┘
#                            │
#                            ▼
# ┌────────────────────────────────────────────────────────┐
# │  MediaInfo.dll  (Native Compiled 64-bit C++ Engine)    │
# │  - Demuxes the .mpg container                          │
# │  - Parses MPEG-2 Sequence & Extension headers          │
# │  - Extracts bitrates, aspect ratios, field orders      │
# └────────────────────────────────────────────────────────┘
# 
# Without MediaInfoDLL3.py, Python cannot directly understand MediaInfo.dll unless
# you manually write dozens of ctypes function definitions, type signatures
# (c_wchar_p, c_size_t), and memory handlers yourself.
# 
# 2. How It Fits Into the Code
# 
# In the script provided earlier, MediaInfoDLL3.py is imported directly:
# 
# from MediaInfoDLL3 import MediaInfo, Stream
# 
# Inside MediaInfoDLL3.py:
# 1.  It loads the DLL via Windows windll.MediaInfo.
# 2.  It defines the Stream class constants:
#       - Stream.General = 0
#       - Stream.Video = 1
#       - Stream.Audio = 2
#       - Stream.Text = 3
# 3.  It exposes high-level Python methods like .Open(), .Close(), .Get(), and
#     .Count_Get() that wrap the low-level C exports inside MediaInfo.dll.
# 
# 3. Why Are There Both MediaInfoDLL.py and MediaInfoDLL3.py?
# 
# Historically:
#   - MediaInfoDLL.py was originally written for Python 2.
#   - MediaInfoDLL3.py was created when Python 3 arrived to handle Unicode strings
#     (str vs bytes) and 64-bit pointer differences.
# 
# In modern versions of MediaInfo, the developers merged the codebase. Both files
# are now identical cross-compatible versions. As stated in the header of
# MediaArea's source code:
# 
# "MediaInfoDLL.py and MediaInfoDLL3.py are same, but all files are kept in order
# to not break programs calling them."
# 
# Summary
#   - You only need one of them.
#   - If you import from MediaInfoDLL3 import MediaInfo, Stream, your program uses
#     MediaInfoDLL3.py.
#   - If you changed the import to from MediaInfoDLL import ..., it would work
#     identically.
