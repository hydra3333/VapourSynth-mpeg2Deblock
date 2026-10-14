#!/usr/bin/env python3
"""Stage 2 S2-I1 read-only reader for the frozen Stage 1 v1 temporary index.

This module intentionally does not import the Stage 1 analyzer.  S2-I1 regression
checks compare this independent interpretation with the frozen analyzer v0.2.
"""

from __future__ import annotations

import argparse
import collections
import json
import struct
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator

FILE_HEADER = struct.Struct("<8sHHIQII")
RECORD_HEADER = struct.Struct("<4sIQIIIHBBHHHHIBBBBBBBBBBH8s")
MB_STRUCT = struct.Struct("<8B")

assert FILE_HEADER.size == 32
assert RECORD_HEADER.size == 64
assert MB_STRUCT.size == 8

FILE_MAGIC = b"S1MBIDX1"
RECORD_MAGIC = b"FRM1"
FILE_VERSION = 1
FILE_COMPLETE_FLAG = 0x00000001
RECORD_FLAGS_V1 = 0x0007
ENDIAN_MARKER = 0x01020304

PICTURE_TYPE = {1: "I", 2: "P", 3: "B"}
TRANSFORM = {0: "NONE", 1: "FRAME", 2: "FIELD"}
CODING = {1: "SKIPPED", 2: "INTRA", 3: "INTER"}


class Stage2IndexError(Exception):
    def __init__(self, errors: Iterable[str]):
        self.errors = tuple(errors)
        super().__init__("; ".join(self.errors[:10]))


@dataclass(frozen=True, slots=True)
class Macroblock:
    transform: int
    coding: int
    q: int
    q_update: int
    cbp: int
    motion_type_raw: int
    motion_dir_bits: int
    motion_source: int
    valid: bool
    q_inherited: bool
    pred_derived: bool
    dct_read: bool
    reserved: int


@dataclass(frozen=True, slots=True)
class PictureRecord:
    output_ordinal: int
    sequence_ordinal: int
    source_bitstream_framenum: int
    source_sequence_framenum: int
    temporal_reference: int
    picture_coding_type: int
    picture_structure: int
    coded_width: int
    coded_height: int
    mb_width: int
    mb_height: int
    mb_count: int
    progressive_frame: int
    top_field_first: int
    repeat_first_field: int
    frame_pred_frame_dct: int
    q_scale_type: int
    chroma_format: int
    custom_intra: int
    custom_non_intra: int
    chroma_intra_diff: int
    chroma_non_intra_diff: int
    mb_payload: bytes

    @property
    def picture_type(self) -> str:
        return PICTURE_TYPE[self.picture_coding_type]

    def iter_macroblocks(self) -> Iterator[Macroblock]:
        payload = self.mb_payload
        for offset in range(0, len(payload), MB_STRUCT.size):
            yield _decode_macroblock(payload[offset : offset + MB_STRUCT.size])

    def macroblock(self, x: int, y: int) -> Macroblock:
        if not (0 <= x < self.mb_width and 0 <= y < self.mb_height):
            raise IndexError(f"macroblock coordinate ({x},{y}) outside {self.mb_width}x{self.mb_height}")
        offset = (y * self.mb_width + x) * MB_STRUCT.size
        return _decode_macroblock(self.mb_payload[offset : offset + MB_STRUCT.size])


@dataclass(frozen=True, slots=True)
class Stage1Index:
    path: Path
    version: int
    file_flags: int
    records: tuple[PictureRecord, ...]

    @property
    def frame_count(self) -> int:
        return len(self.records)

    @property
    def width(self) -> int:
        return self.records[0].coded_width if self.records else 0

    @property
    def height(self) -> int:
        return self.records[0].coded_height if self.records else 0

    @property
    def leading_b_ordinals(self) -> tuple[int, ...]:
        result: list[int] = []
        seen_i = False
        for rec in self.records:
            if rec.picture_coding_type == 1:
                seen_i = True
            elif rec.picture_coding_type == 3 and not seen_i:
                result.append(rec.output_ordinal)
        return tuple(result)

    def quality_excluded(self, ordinal: int) -> bool:
        return ordinal in self.leading_b_ordinals

    def summary(self) -> dict[str, object]:
        picture_types: collections.Counter[str] = collections.Counter()
        picture_structures: collections.Counter[int] = collections.Counter()
        progressive: collections.Counter[int] = collections.Counter()
        transforms: collections.Counter[str] = collections.Counter()
        coding: collections.Counter[str] = collections.Counter()
        q_histogram: collections.Counter[int] = collections.Counter()
        q_scale_type: collections.Counter[int] = collections.Counter()
        total_mb = 0

        for rec in self.records:
            picture_types[rec.picture_type] += 1
            picture_structures[rec.picture_structure] += 1
            progressive[rec.progressive_frame] += 1
            q_scale_type[rec.q_scale_type] += 1
            total_mb += rec.mb_count
            for mb in rec.iter_macroblocks():
                transforms[TRANSFORM[mb.transform]] += 1
                coding[CODING[mb.coding]] += 1
                q_histogram[mb.q] += 1

        return {
            "path": str(self.path),
            "version": self.version,
            "file_flags": self.file_flags,
            "record_count": self.frame_count,
            "sequence_count": len({r.sequence_ordinal for r in self.records}),
            "dimensions": [self.width, self.height],
            "mb_grid": [self.records[0].mb_width, self.records[0].mb_height] if self.records else [0, 0],
            "total_macroblocks": total_mb,
            "picture_types": dict(sorted(picture_types.items())),
            "picture_structures": {str(k): v for k, v in sorted(picture_structures.items())},
            "progressive_frame": {str(k): v for k, v in sorted(progressive.items())},
            "q_scale_type": {str(k): v for k, v in sorted(q_scale_type.items())},
            "transform_states": dict(sorted(transforms.items())),
            "coding_states": dict(sorted(coding.items())),
            "qp_histogram": {str(k): v for k, v in sorted(q_histogram.items())},
            "leading_b_excluded_count": len(self.leading_b_ordinals),
            "leading_b_excluded_ordinals": list(self.leading_b_ordinals),
        }


def _decode_macroblock(raw: bytes) -> Macroblock:
    transform, coding, q, q_update, cbp, motion_type_raw, motion_dir_bits, packed = MB_STRUCT.unpack(raw)
    return Macroblock(
        transform=transform,
        coding=coding,
        q=q,
        q_update=q_update,
        cbp=cbp,
        motion_type_raw=motion_type_raw,
        motion_dir_bits=motion_dir_bits,
        motion_source=packed & 0x03,
        valid=bool(packed & 0x04),
        q_inherited=bool(packed & 0x08),
        pred_derived=bool(packed & 0x10),
        dct_read=bool(packed & 0x20),
        reserved=packed & 0xC0,
    )


def _validate_macroblock(mb: Macroblock, rec: PictureRecord, mb_index: int, errors: list[str]) -> None:
    prefix = f"record {rec.output_ordinal} MB {mb_index}"
    if mb.transform not in (0, 1, 2):
        errors.append(f"{prefix}: invalid transform {mb.transform}")
    if mb.coding not in (1, 2, 3):
        errors.append(f"{prefix}: invalid coding {mb.coding}")
    if mb.q_update not in (0, 1):
        errors.append(f"{prefix}: invalid q_update {mb.q_update}")
    if mb.cbp > 63:
        errors.append(f"{prefix}: CBP {mb.cbp} exceeds 4:2:0 range")
    if mb.motion_type_raw > 3:
        errors.append(f"{prefix}: motion_type_raw {mb.motion_type_raw} > 3")
    if mb.motion_dir_bits & ~3:
        errors.append(f"{prefix}: invalid motion_dir_bits {mb.motion_dir_bits}")
    if mb.reserved:
        errors.append(f"{prefix}: reserved packed bits set 0x{mb.reserved:02x}")
    if not mb.valid:
        errors.append(f"{prefix}: macroblock not marked valid")
    if mb.q_inherited != (mb.q_update == 0):
        errors.append(f"{prefix}: q_inherited duplicate flag mismatch")
    if mb.pred_derived != (mb.motion_source in (2, 3)):
        errors.append(f"{prefix}: pred_derived duplicate flag mismatch")
    if mb.coding == 1:
        if mb.transform != 0:
            errors.append(f"{prefix}: SKIPPED is not NONE")
        if mb.q_update != 0:
            errors.append(f"{prefix}: SKIPPED has q_update")
        if mb.dct_read:
            errors.append(f"{prefix}: SKIPPED has dct_read")
        if mb.motion_source == 1:
            errors.append(f"{prefix}: SKIPPED has CODED motion source")
    if mb.motion_source == 3 and not (mb.coding == 1 and rec.picture_coding_type == 3):
        errors.append(f"{prefix}: INHERITED motion outside skipped B picture")
    if mb.motion_source == 0 and mb.motion_dir_bits != 0:
        errors.append(f"{prefix}: motion dirs nonzero with no motion source")
    if mb.dct_read and (
        rec.picture_structure != 3 or rec.frame_pred_frame_dct != 0 or mb.coding == 1
    ):
        errors.append(f"{prefix}: dct_read outside allowed context")
    if mb.transform == 2 and (
        not mb.dct_read
        or rec.picture_structure != 3
        or rec.frame_pred_frame_dct != 0
        or mb.coding == 1
    ):
        errors.append(f"{prefix}: FIELD without valid dct_type context")
    if mb.coding == 2:
        if mb.transform == 0:
            errors.append(f"{prefix}: INTRA has NONE transform")
        if mb.cbp != 63:
            errors.append(f"{prefix}: INTRA CBP {mb.cbp} != 63")
    if mb.coding == 3 and mb.cbp == 0 and mb.transform != 0:
        errors.append(f"{prefix}: INTER CBP=0 is not NONE")
    if mb.coding == 3 and mb.cbp > 0 and mb.transform == 0:
        errors.append(f"{prefix}: INTER CBP>0 has NONE transform")
    if (
        rec.picture_structure == 3
        and rec.frame_pred_frame_dct == 0
        and mb.transform != 0
        and not mb.dct_read
    ):
        errors.append(f"{prefix}: transform present without dct_read in frame picture with frame_pred_frame_dct=0")


def read_index(path: str | Path) -> Stage1Index:
    path = Path(path)
    errors: list[str] = []
    records: list[PictureRecord] = []

    with path.open("rb") as handle:
        raw = handle.read(FILE_HEADER.size)
        if len(raw) != FILE_HEADER.size:
            raise Stage2IndexError(["truncated file header"])

        magic, version, header_size, endian, final_count, file_flags, reserved = FILE_HEADER.unpack(raw)
        if magic != FILE_MAGIC:
            errors.append(f"bad file magic {magic!r}")
        if version != FILE_VERSION:
            errors.append(f"unsupported version {version}")
        if header_size != FILE_HEADER.size:
            errors.append(f"file_header_size {header_size} != {FILE_HEADER.size}")
        if endian != ENDIAN_MARKER:
            errors.append(f"bad endian marker 0x{endian:08x}")
        if reserved != 0:
            errors.append("file header reserved field is nonzero")
        if not (file_flags & FILE_COMPLETE_FLAG):
            errors.append("file is not marked complete")
        if file_flags & ~FILE_COMPLETE_FLAG:
            errors.append(f"file has unsupported/error flags 0x{file_flags & ~FILE_COMPLETE_FLAG:08x}")
        if errors:
            raise Stage2IndexError(errors)

        expected_ordinal = 0
        first_dimensions: tuple[int, int, int, int] | None = None
        while True:
            record_offset = handle.tell()
            header = handle.read(RECORD_HEADER.size)
            if not header:
                break
            if len(header) != RECORD_HEADER.size:
                errors.append(f"truncated record header at offset {record_offset}")
                break

            values = RECORD_HEADER.unpack(header)
            (
                record_magic,
                record_size,
                ordinal,
                sequence_ordinal,
                bitstream_frame_number,
                sequence_frame_number,
                temporal_reference,
                picture_coding_type,
                picture_structure,
                coded_width,
                coded_height,
                mb_width,
                mb_height,
                mb_count,
                progressive_frame,
                top_field_first,
                repeat_first_field,
                frame_pred_frame_dct,
                q_scale_type,
                chroma_format,
                custom_intra,
                custom_non_intra,
                chroma_intra_diff,
                chroma_non_intra_diff,
                record_flags,
                record_reserved,
            ) = values

            payload_size = mb_count * MB_STRUCT.size
            payload = handle.read(payload_size)

            rec = PictureRecord(
                output_ordinal=ordinal,
                sequence_ordinal=sequence_ordinal,
                source_bitstream_framenum=bitstream_frame_number,
                source_sequence_framenum=sequence_frame_number,
                temporal_reference=temporal_reference,
                picture_coding_type=picture_coding_type,
                picture_structure=picture_structure,
                coded_width=coded_width,
                coded_height=coded_height,
                mb_width=mb_width,
                mb_height=mb_height,
                mb_count=mb_count,
                progressive_frame=progressive_frame,
                top_field_first=top_field_first,
                repeat_first_field=repeat_first_field,
                frame_pred_frame_dct=frame_pred_frame_dct,
                q_scale_type=q_scale_type,
                chroma_format=chroma_format,
                custom_intra=custom_intra,
                custom_non_intra=custom_non_intra,
                chroma_intra_diff=chroma_intra_diff,
                chroma_non_intra_diff=chroma_non_intra_diff,
                mb_payload=payload,
            )

            prefix = f"record {ordinal}"
            if record_magic != RECORD_MAGIC:
                errors.append(f"{prefix}: bad magic {record_magic!r}")
            if ordinal != expected_ordinal:
                errors.append(f"record ordinal {ordinal} expected {expected_ordinal}")
            expected_ordinal += 1
            if mb_count != mb_width * mb_height:
                errors.append(f"{prefix}: mb_count mismatch")
            expected_size = RECORD_HEADER.size + payload_size
            if record_size != expected_size:
                errors.append(f"{prefix}: record_size {record_size} != {expected_size}")
            if record_reserved != b"\x00" * 8:
                errors.append(f"{prefix}: reserved bytes nonzero")
            if record_flags != RECORD_FLAGS_V1:
                errors.append(f"{prefix}: record_flags 0x{record_flags:04x} != 0x{RECORD_FLAGS_V1:04x}")
            if len(payload) != payload_size:
                errors.append(f"{prefix}: truncated MB payload")
                break

            # Stage 2 v0.6 supported-domain checks.
            if picture_coding_type not in PICTURE_TYPE:
                errors.append(f"{prefix}: unsupported picture_coding_type {picture_coding_type}")
            if picture_structure != 3:
                errors.append(f"{prefix}: field picture structure {picture_structure} unsupported in Stage 2")
            if progressive_frame not in (0, 1):
                errors.append(f"{prefix}: progressive_frame {progressive_frame} is not boolean")
            if top_field_first not in (0, 1):
                errors.append(f"{prefix}: top_field_first {top_field_first} is not boolean")
            if repeat_first_field not in (0, 1):
                errors.append(f"{prefix}: repeat_first_field {repeat_first_field} is not boolean")
            if frame_pred_frame_dct not in (0, 1):
                errors.append(f"{prefix}: frame_pred_frame_dct {frame_pred_frame_dct} is not boolean")
            if q_scale_type not in (0, 1):
                errors.append(f"{prefix}: q_scale_type {q_scale_type} is not boolean")
            if chroma_format != 1:
                errors.append(f"{prefix}: chroma_format {chroma_format} unsupported; Stage 2 requires 4:2:0")
            for name, value in (
                ("custom_intra", custom_intra),
                ("custom_non_intra", custom_non_intra),
                ("chroma_intra_diff", chroma_intra_diff),
                ("chroma_non_intra_diff", chroma_non_intra_diff),
            ):
                if value not in (0, 1):
                    errors.append(f"{prefix}: {name} {value} is not boolean")
            if coded_width <= 0 or coded_height <= 0 or mb_width <= 0 or mb_height <= 0:
                errors.append(f"{prefix}: non-positive dimensions or MB grid")
            if mb_width != (coded_width + 15) // 16 or mb_height != (coded_height + 15) // 16:
                errors.append(
                    f"{prefix}: MB grid {mb_width}x{mb_height} inconsistent with coded dimensions "
                    f"{coded_width}x{coded_height}"
                )

            dimensions = (coded_width, coded_height, mb_width, mb_height)
            if first_dimensions is None:
                first_dimensions = dimensions
            elif dimensions != first_dimensions:
                errors.append(
                    f"{prefix}: dimensions/MB grid changed from {first_dimensions} to {dimensions}; "
                    "unsupported in current Stage 2"
                )

            if errors:
                raise Stage2IndexError(errors)

            if picture_coding_type in PICTURE_TYPE:
                for mb_index in range(mb_count):
                    start = mb_index * MB_STRUCT.size
                    mb = _decode_macroblock(payload[start : start + MB_STRUCT.size])
                    _validate_macroblock(mb, rec, mb_index, errors)
            if errors:
                raise Stage2IndexError(errors)

            records.append(rec)

        if len(records) != final_count:
            errors.append(f"parsed record count {len(records)} != header final_record_count {final_count}")

    if errors:
        raise Stage2IndexError(errors)
    if not records:
        raise Stage2IndexError(["index contains no records"])

    return Stage1Index(path=path, version=version, file_flags=file_flags, records=tuple(records))


def validate_clip_metadata(
    index: Stage1Index,
    *,
    frame_count: int,
    width: int,
    height: int,
    picture_types: Iterable[str] | None = None,
) -> None:
    errors: list[str] = []
    if frame_count != index.frame_count:
        errors.append(f"frame count mismatch: clip={frame_count} index={index.frame_count}")
    if width != index.width or height != index.height:
        errors.append(f"dimension mismatch: clip={width}x{height} index={index.width}x{index.height}")

    if picture_types is not None:
        clip_types = list(picture_types)
        if len(clip_types) != frame_count:
            errors.append(f"picture-type list length {len(clip_types)} != clip frame count {frame_count}")
        for ordinal, (clip_type, rec) in enumerate(zip(clip_types, index.records)):
            if clip_type != rec.picture_type:
                errors.append(
                    f"picture type mismatch at frame {ordinal}: clip={clip_type!r} index={rec.picture_type!r}"
                )
                if len(errors) >= 100:
                    break

    if errors:
        raise Stage2IndexError(errors)


EXPECTED_4A_BLOCKY = {
    "record_count": 300,
    "dimensions": [720, 576],
    "mb_grid": [45, 36],
    "picture_types": {"B": 199, "I": 26, "P": 75},
    "progressive_frame": {"0": 300},
    "transform_states": {"FIELD": 35243, "FRAME": 56235, "NONE": 394522},
    "coding_states": {"INTER": 316290, "INTRA": 46078, "SKIPPED": 123632},
    "q_scale_type": {"0": 300},
    "qp_histogram": {"62": 486000},
    "leading_b_excluded_count": 0,
}


def validate_4a_blocky_candidate(index: Stage1Index) -> None:
    summary = index.summary()
    errors = []
    for key, expected in EXPECTED_4A_BLOCKY.items():
        actual = summary[key]
        if actual != expected:
            errors.append(f"TEST_4A_A003_blocky {key}: {actual!r} != expected {expected!r}")
    if errors:
        raise Stage2IndexError(errors)


def _print_errors(exc: Stage2IndexError) -> None:
    print("INVALID Stage 2 index input", file=sys.stderr)
    for error in exc.errors[:100]:
        print("  " + error, file=sys.stderr)
    if len(exc.errors) > 100:
        print(f"  ... {len(exc.errors) - 100} more errors", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description="Stage 2 S2-I1 read-only Stage 1 index reader")
    sub = parser.add_subparsers(dest="command", required=True)

    summary_parser = sub.add_parser("summary", help="validate an index and print its Stage 2 summary")
    summary_parser.add_argument("index")
    summary_parser.add_argument("--json", action="store_true")

    candidate_parser = sub.add_parser(
        "validate-4a-blocky",
        help="validate a generated TEST_4A_A003_blocky index against frozen Stage 1 report totals",
    )
    candidate_parser.add_argument("index")

    args = parser.parse_args()
    try:
        print(f"S2-I1 reading index: {args.index}")
        index = read_index(args.index)
        if args.command == "summary":
            data = index.summary()
            if args.json:
                print(json.dumps(data, indent=2, sort_keys=True))
            else:
                print(f"VALID records={data['record_count']} dimensions={data['dimensions'][0]}x{data['dimensions'][1]}")
                print(f"picture_types={data['picture_types']}")
                print(f"progressive_frame={data['progressive_frame']}")
                print(f"transform_states={data['transform_states']}")
                print(f"qp_histogram={data['qp_histogram']}")
                print(
                    "leading_B_quality_exclusion="
                    f"{data['leading_b_excluded_count']} ordinals={data['leading_b_excluded_ordinals']}"
                )
        elif args.command == "validate-4a-blocky":
            validate_4a_blocky_candidate(index)
            print("PASS: TEST_4A_A003_blocky matches frozen Stage 1 section 8.1 totals")
            print(json.dumps(index.summary(), indent=2, sort_keys=True))
    except (OSError, Stage2IndexError) as exc:
        if isinstance(exc, Stage2IndexError):
            _print_errors(exc)
        else:
            print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
