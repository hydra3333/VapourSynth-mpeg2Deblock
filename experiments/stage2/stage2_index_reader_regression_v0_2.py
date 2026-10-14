#!/usr/bin/env python3
"""S2-I1 v0.2 regression against frozen analyzer-v0.2 summary results."""

from __future__ import annotations

import hashlib
import shutil
import struct
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

import stage2_index_reader_v0_2 as s2

# Frozen Stage 1 baseline identities plus summary values independently produced by
# tools/Stage1_Inspector_Analyzer_v0_2.py from those exact files.
EXPECTED = {
    "LG_576i_3_LP.idx": {
        "sha256": "849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011",
        "record_count": 204,
        "picture_types": {"B": 136, "I": 17, "P": 51},
        "progressive_frame": {"0": 204},
        "transform_states": {"FIELD": 174291, "FRAME": 75903, "NONE": 80286},
        "qp_histogram": {"1":1659,"2":485,"3":935,"4":2989,"5":1402,"6":554,"7":384,"8":1657,"10":9268,"12":29275,"14":50794,"16":59870,"18":45979,"20":47547,"22":26088,"24":20473,"28":12373,"32":3757,"36":807,"40":108,"44":49,"48":58,"52":60,"56":74,"64":124,"72":129,"80":168,"88":187,"96":245,"104":386,"112":12596},
        "leading_b_excluded_ordinals": [0, 1],
    },
    "LG_576i_4_EP.idx": {
        "sha256": "11b42aadf9f46b72dec20a8f3fdd754d07cdce78f0460a14eda08838336ffa87",
        "record_count": 216,
        "picture_types": {"B": 144, "I": 18, "P": 54},
        "progressive_frame": {"0": 216},
        "transform_states": {"FIELD": 130385, "FRAME": 16575, "NONE": 24112},
        "qp_histogram": {"1":560,"2":195,"3":737,"4":1520,"5":422,"6":212,"7":293,"8":3089,"10":10519,"12":28364,"14":45612,"16":33858,"18":17069,"20":9213,"22":6168,"24":4587,"28":2412,"32":439,"36":88,"40":73,"44":64,"48":82,"52":108,"56":129,"64":196,"72":298,"80":586,"88":748,"96":128,"104":61,"112":3242},
        "leading_b_excluded_ordinals": [0, 1],
    },
    "LG_576i_5_MLS.idx": {
        "sha256": "378980ea462122a02d75f412faf9cfaf79962d503c68a8f6ee41c32b24d98d7f",
        "record_count": 420,
        "picture_types": {"B": 280, "I": 35, "P": 105},
        "progressive_frame": {"1": 420},
        "transform_states": {"FRAME": 142100, "NONE": 24220},
        "qp_histogram": {"2":6132,"4":4429,"6":13940,"8":33282,"10":38968,"12":24748,"14":12654,"16":7146,"18":4998,"20":5904,"22":3950,"24":2765,"26":2016,"28":1597,"30":1101,"32":965,"34":636,"36":411,"38":295,"40":137,"42":95,"44":66,"46":29,"48":8,"50":14,"52":18,"54":8,"56":1,"58":3,"60":1,"62":3},
        "leading_b_excluded_ordinals": [0, 1],
    },
    "TEST_2A_A001.idx": {
        "sha256": "afe51f251b2861d5c62e1629d95645c47b06f69d86f03b5fc531cf9fe3ea9273",
        "record_count": 300,
        "picture_types": {"B": 133, "I": 34, "P": 133},
        "progressive_frame": {"0": 300},
        "transform_states": {"FIELD": 29330, "FRAME": 281112, "NONE": 164758},
        "qp_histogram": {"1":19,"2":124,"3":1169,"4":6504,"5":14586,"6":26354,"7":27959,"8":63336,"10":63927,"12":45530,"14":29046,"16":17867,"18":16570,"20":17208,"22":19915,"24":38012,"28":33295,"32":22186,"36":11479,"40":6276,"44":4622,"48":3148,"52":2155,"56":1679,"64":1061,"72":750,"80":423},
        "leading_b_excluded_ordinals": [],
    },
    "TEST_2A_A001_blocky.idx": {
        "sha256": "cbf6e8720e47e1f097e6310540d8cbd20862e3a427ad53c61d9a235acdba9288",
        "record_count": 300,
        "picture_types": {"B": 199, "I": 26, "P": 75},
        "progressive_frame": {"0": 300},
        "transform_states": {"FIELD": 108611, "FRAME": 63019, "NONE": 303570},
        "qp_histogram": {"62": 475200},
        "leading_b_excluded_ordinals": [],
    },
    "TEST_4A_A003.idx": {
        "sha256": "5b989ced016adfe5cc4546f196dd63cb2db9b431798a99203c830a98165b9a65",
        "record_count": 300,
        "picture_types": {"B": 198, "I": 26, "P": 76},
        "progressive_frame": {"0": 300},
        "transform_states": {"FIELD": 333986, "FRAME": 94741, "NONE": 57273},
        "qp_histogram": {"2":124,"3":1322,"4":5631,"5":13452,"6":14483,"7":8168,"8":11965,"10":24156,"12":76430,"14":121348,"16":93593,"18":51052,"20":29408,"22":16952,"24":12004,"26":1,"28":5310,"30":3,"32":562,"36":36},
        "leading_b_excluded_ordinals": [],
    },
}


def require_equal(label: str, actual, expected) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: {actual!r} != {expected!r}")


def compare_one(path: Path, expected: dict) -> None:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    require_equal(f"{path.name} SHA-256", digest, expected["sha256"])
    summary = s2.read_index(path).summary()
    for key in (
        "record_count",
        "picture_types",
        "progressive_frame",
        "transform_states",
        "qp_histogram",
        "leading_b_excluded_ordinals",
    ):
        require_equal(f"{path.name} {key}", summary[key], expected[key])
    print(
        f"PASS {path.name}: records={summary['record_count']} "
        f"transforms={summary['transform_states']} "
        f"leading_B={summary['leading_b_excluded_ordinals']}"
    )


def expect_rejected(label: str, source: Path, patch) -> None:
    with tempfile.TemporaryDirectory(prefix="s2_i1_negative_") as td:
        target = Path(td) / source.name
        shutil.copyfile(source, target)
        data = bytearray(target.read_bytes())
        patch(data)
        target.write_bytes(data)
        try:
            s2.read_index(target)
        except s2.Stage2IndexError:
            print(f"PASS negative {label}: rejected")
        else:
            raise AssertionError(f"negative test {label}: malformed index was accepted")


def run_negative_tests(source: Path) -> None:
    expect_rejected("bad-file-magic", source, lambda d: d.__setitem__(0, ord("X")))

    def clear_complete(d: bytearray) -> None:
        struct.pack_into("<I", d, 24, 0)
    expect_rejected("incomplete-file", source, clear_complete)

    def bad_ordinal(d: bytearray) -> None:
        struct.pack_into("<Q", d, 32 + 8, 1)
    expect_rejected("bad-first-ordinal", source, bad_ordinal)

    def field_picture(d: bytearray) -> None:
        d[32 + 31] = 1
    expect_rejected("unsupported-field-picture", source, field_picture)


def main() -> int:
    samples = REPO_ROOT / "VHSC_samples"
    print(f"S2-I1 repository root: {REPO_ROOT}")
    print("S2-I1 expected summaries: frozen analyzer v0.2 results for the six accepted baseline hashes")

    try:
        for name, expected in EXPECTED.items():
            path = samples / name
            print(f"S2-I1 reading accepted baseline: {path}")
            compare_one(path, expected)
        run_negative_tests(samples / "TEST_4A_A003.idx")
    except (AssertionError, OSError, s2.Stage2IndexError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2

    candidate = samples / "TEST_4A_A003_blocky.idx"
    if candidate.exists():
        print(f"NOTICE: repository-area 4A-blocky candidate exists: {candidate}")
        try:
            s2.validate_4a_blocky_candidate(s2.read_index(candidate))
            print("PASS: existing 4A-blocky candidate matches frozen Stage 1 section 8.1 totals")
        except s2.Stage2IndexError as exc:
            print(f"FAIL 4A-blocky candidate: {exc}", file=sys.stderr)
            return 2
    else:
        print("EXPECTED NEXT S2-I1 ACTION: TEST_4A_A003_blocky.idx is absent; generate it in scratch with the frozen inspector and validate it.")

    print("PASS: S2-I1 v0.2 reader reproduces frozen analyzer v0.2 totals on all six accepted indexes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
