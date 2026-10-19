#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inspect MPG/MPEG-2 metadata using the user's MediaInfo.dll installation.

Original basis: EXAMPLE_PY_USING_MEDIAINFO_DLL(1).py (Google AI Studio example,
with the owner's persistent DLL-search-handle correction).

Version 0.2.0 - add provenance-preserving VAL_ best-available outputs.

The original program's explanatory mapping and notes are retained below and
extended. This utility is a metadata preflight, NOT the MPEG-2 macroblock indexer
and NOT a frame-accurate decoder or blockiness assessor.

Examples (Windows CMD):
    python mpeg2deblock_fetch_metadata.py "D:\\VHS\\test.mpg"
    python mpeg2deblock_fetch_metadata.py "D:\\VHS\\test.mpg" --prefix SRC_ --bat "D:\\VHS\\test_metadata.bat"
    python mpeg2deblock_fetch_metadata.py "D:\\VHS" --recursive --prefix SRC_ --bat-dir "D:\\VHS\\metadata"
    call "D:\\VHS\\test_metadata.bat"
    echo %SRC_MI_VIDEO_FRAME_COUNT%
    echo %SRC_EST_VIDEO_FRAME_COUNT%
    echo %SRC_VAL_VIDEO_FRAME_COUNT%
    echo %SRC_VAL_VIDEO_FRAME_COUNT_SOURCE%

Note: percentage expansion in a parenthesised caller BAT block occurs before
CALL, so inspect resulting variables on lines outside that block, or use CALL
SET commands deliberately. Generated BAT output is ASCII/CRLF and deliberately
rejects metadata values unsafe for faithful CMD SET assignment rather than
silently altering or injecting them. See README.
"""

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
# Original example reminder: retain os.add_dll_directory() handles for the entire
# time the DLL is in use; never discard them immediately.

import argparse
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from fractions import Fraction
import os
from pathlib import Path
import re
import sys
import tempfile

# Original example's default portable VapourSynth installation. It can be
# overridden by --mediainfo-dir; the wrapper and DLL must be in the same folder.
vapoursynth_path = r"D:\TEST\Vapoursynth_x64_R81"

# ==============================================================================
# FULL PREDECLARED MEDIAINFO FIELD CATALOGUE -- EDIT HERE, NOT IN inspect_file()
# ==============================================================================
# Each active F(...) controls BOTH MediaInfo.Get() and the corresponding BAT
# variable and the inventory report. To disable a field without forgetting its
# definition, comment out its line using '#'; uncomment it when needed.
#
# Format: F('GENERAL'|'VIDEO'|'AUDIO', 'OUTPUT_SUFFIX', 'MediaInfo Parameter', 'Readable label')
# OUTPUT_SUFFIX has no user prefix or MI_: prefix SRC_ produces
#   SRC_MI_GENERAL_DURATION, SRC_MI_VIDEO_FRAME_COUNT, SRC_MI_AUDIO_0_FORMAT.
# Audio catalogue is applied separately to EVERY detected audio stream.
#
# These are PREDECLARED possible requests, not a claim that every file/version
# provides every field. Missing fields yield the empty string, never a fabricated
# default. MediaInfo API names are case-insensitive on current MediaInfo builds,
# but the spellings here follow common MediaInfo names. Optional entries may be
# unavailable on particular media. Keep estimates in EST_ namespace.


@dataclass(frozen=True)
class F:
    group: str
    suffix: str
    parameter: str
    label: str


FIELDS = (
    # --- General / container fields ---
    F('GENERAL', 'FORMAT',                 'Format',                      'Container format'),
    F('GENERAL', 'FORMAT_PROFILE',         'Format_Profile',              'Container profile'),
    F('GENERAL', 'FORMAT_VERSION',         'Format_Version',              'Container format version'),
    F('GENERAL', 'FILE_SIZE',              'FileSize',                    'File size (bytes)'),
    F('GENERAL', 'FILE_SIZE_STRING',       'FileSize/String',             'File size (display)'),
    F('GENERAL', 'DURATION',               'Duration',                    'Overall duration (ms)'),
    F('GENERAL', 'DURATION_STRING3',       'Duration/String3',            'Overall duration (display)'),
    F('GENERAL', 'OVERALL_BITRATE',        'OverallBitRate',              'Overall bit rate (bps)'),
    F('GENERAL', 'OVERALL_BITRATE_MODE',   'OverallBitRate_Mode',         'Overall bit rate mode'),
    F('GENERAL', 'VIDEO_COUNT',            'VideoCount',                 'Video stream count (reported)'),
    F('GENERAL', 'AUDIO_COUNT',            'AudioCount',                 'Audio stream count (reported)'),
    # Uncomment as useful; potentially free-text fields are less suitable for BAT.
    # F('GENERAL', 'COMPLETE_NAME',          'CompleteName',               'Original file name'),
    # F('GENERAL', 'ENCODED_DATE',           'Encoded_Date',               'Encoded date'),
    # F('GENERAL', 'TAGGED_DATE',            'Tagged_Date',                'Tagged date'),
    # F('GENERAL', 'WRITING_APPLICATION',    'WritingApplication',        'Writing application'),
    # F('GENERAL', 'WRITING_LIBRARY',        'WritingLibrary',            'Writing library'),
    # F('GENERAL', 'TITLE',                  'Title',                      'Title'),
    # F('GENERAL', 'COMMENT',                'Comment',                    'Comment'),

    # --- Selected video stream (zero-based stream index, default 0) ---
    F('VIDEO', 'FORMAT',                  'Format',                        'Video format'),
    F('VIDEO', 'FORMAT_VERSION',          'Format_Version',                'Video format version'),
    F('VIDEO', 'FORMAT_PROFILE',          'Format_Profile',                'Video profile'),
    F('VIDEO', 'CODEC_ID',                'CodecID',                       'Codec ID'),
    F('VIDEO', 'WIDTH',                   'Width',                         'Width (pixels)'),
    F('VIDEO', 'HEIGHT',                  'Height',                        'Height (pixels)'),
    F('VIDEO', 'SAMPLED_WIDTH',           'Sampled_Width',                 'Sampled width'),
    F('VIDEO', 'SAMPLED_HEIGHT',          'Sampled_Height',                'Sampled height'),
    F('VIDEO', 'DISPLAY_ASPECT_RATIO',    'DisplayAspectRatio',            'Display aspect ratio'),
    F('VIDEO', 'DISPLAY_ASPECT_RATIO_S',  'DisplayAspectRatio/String',     'Display aspect ratio (display)'),
    F('VIDEO', 'PIXEL_ASPECT_RATIO',      'PixelAspectRatio',              'Pixel aspect ratio'),
    F('VIDEO', 'FRAME_RATE_MODE',         'FrameRate_Mode',                'Constant/variable frame rate'),
    F('VIDEO', 'FRAME_RATE',              'FrameRate',                     'Frame rate (fps)'),
    F('VIDEO', 'FRAME_RATE_NUM',          'FrameRate_Num',                 'Frame rate numerator'),
    F('VIDEO', 'FRAME_RATE_DEN',          'FrameRate_Den',                 'Frame rate denominator'),
    F('VIDEO', 'FRAME_COUNT',             'FrameCount',                    'Reported video frame count'),
    F('VIDEO', 'DURATION',                'Duration',                      'Video duration (ms)'),
    F('VIDEO', 'DURATION_STRING3',        'Duration/String3',              'Video duration (display)'),
    F('VIDEO', 'STANDARD',                'Standard',                      'PAL/NTSC/SECAM (reported)'),
    F('VIDEO', 'SCAN_TYPE',               'ScanType',                      'Scan type'),
    F('VIDEO', 'SCAN_ORDER',              'ScanOrder',                     'Scan/field order'),
    F('VIDEO', 'SCAN_ORDER_S',            'ScanOrder/String',              'Field order (display)'),
    F('VIDEO', 'BITRATE',                 'BitRate',                       'Video bit rate (bps)'),
    F('VIDEO', 'BITRATE_S',               'BitRate/String',                'Video bit rate (display)'),
    F('VIDEO', 'BITRATE_MODE',            'BitRate_Mode',                  'Video bit rate mode'),
    F('VIDEO', 'BITRATE_MAXIMUM',         'BitRate_Maximum',               'Maximum video bit rate (bps)'),
    F('VIDEO', 'BITRATE_MAXIMUM_S',       'BitRate_Maximum/String',        'Maximum bit rate (display)'),
    F('VIDEO', 'COLOR_SPACE',             'ColorSpace',                    'Colour space'),
    F('VIDEO', 'CHROMA_SUBSAMPLING',      'ChromaSubsampling',             'Chroma subsampling'),
    F('VIDEO', 'BIT_DEPTH',               'BitDepth',                      'Bit depth'),
    F('VIDEO', 'COLOR_RANGE',             'colour_range',                 'Colour range'),
    F('VIDEO', 'COLOR_PRIMARIES',         'colour_primaries',             'Colour primaries'),
    F('VIDEO', 'TRANSFER_CHARACTERISTICS','transfer_characteristics',    'Transfer characteristics'),
    F('VIDEO', 'MATRIX_COEFFICIENTS',     'matrix_coefficients',           'Matrix coefficients'),
    F('VIDEO', 'FORMAT_SETTINGS_GOP',     'Format_Settings_GOP',          'GOP settings'),
    F('VIDEO', 'FORMAT_SETTINGS_MATRIX',  'Format_Settings_Matrix',       'Quantisation matrix setting'),
    F('VIDEO', 'GOP_OPEN_CLOSED',         'GOP_OpenClosed',               'GOP open/closed'),
    F('VIDEO', 'INTRA_DC_PRECISION',      'intra_dc_precision',           'Intra DC precision'),
    F('VIDEO', 'DELAY',                   'Delay',                         'Stream delay (ms)'),
    # F('VIDEO', 'FORMAT_SETTINGS_MATRIX_DATA', 'Format_Settings_Matrix_Data', 'Custom matrix coefficients'),
    # F('VIDEO', 'TIME_CODE_FIRST',        'TimeCode_FirstFrame',          'Time code of first frame'),
    # F('VIDEO', 'BITS_PIXEL_FRAME',       'Bits-(Pixel*Frame)',           'Bits per pixel/frame'),
    # F('VIDEO', 'WRITING_LIBRARY',        'WritingLibrary',              'Video encoder library'),
    # F('VIDEO', 'ENCODED_LIBRARY_NAME',   'Encoded_Library_Name',        'Encoder library name'),
    # F('VIDEO', 'CHROMA_SUBSAMPLING_POS', 'ChromaSubsampling_Position',   'Chroma sample positioning'),
    # F('VIDEO', 'COLOUR_DESCRIPTION',     'colour_description_present',  'Colour-description-present flag'),
    # F('VIDEO', 'HDR_FORMAT',             'HDR_Format',                  'HDR format'),

    # --- All audio streams, enumerated by Stream.Audio index ---
    F('AUDIO', 'FORMAT',                   'Format',                 'Audio format'),
    F('AUDIO', 'FORMAT_PROFILE',           'Format_Profile',         'Audio profile'),
    F('AUDIO', 'CODEC_ID',                 'CodecID',                'Audio codec ID'),
    F('AUDIO', 'CHANNELS',                 'Channels',               'Audio channel count'),
    F('AUDIO', 'CHANNELS_S',               'Channels/String',        'Audio channels (display)'),
    F('AUDIO', 'SAMPLING_RATE',            'SamplingRate',           'Audio sampling rate (Hz)'),
    F('AUDIO', 'SAMPLING_RATE_S',          'SamplingRate/String',    'Audio sampling rate (display)'),
    F('AUDIO', 'BITRATE',                  'BitRate',                'Audio bit rate (bps)'),
    F('AUDIO', 'BITRATE_S',                'BitRate/String',         'Audio bit rate (display)'),
    F('AUDIO', 'BITRATE_MODE',             'BitRate_Mode',           'Audio bit rate mode'),
    F('AUDIO', 'DURATION',                 'Duration',               'Audio duration (ms)'),
    F('AUDIO', 'LANGUAGE',                 'Language',               'Audio language code'),
    F('AUDIO', 'LANGUAGE_S',               'Language/String',        'Audio language (display)'),
    F('AUDIO', 'DELAY',                    'Delay',                  'Audio delay (ms)'),
    # F('AUDIO', 'CHANNEL_LAYOUT',         'ChannelLayout',          'Audio channel layout'),
    # F('AUDIO', 'BIT_DEPTH',              'BitDepth',               'Audio bit depth'),
    # F('AUDIO', 'STREAM_SIZE',            'StreamSize',             'Audio stream size'),
    # F('AUDIO', 'TITLE',                  'Title',                  'Audio title'),
    # F('AUDIO', 'COMPRESSION_MODE',       'Compression_Mode',       'Compression mode'),
)

# ==============================================================================
# RESOLVED VALUE GROUPS -- COMMENT OUT AN ENTIRE LINE TO DISABLE THAT GROUP
# ==============================================================================
# All possible VAL_ exports live in this small table. They do NOT cause new
# MediaInfo.Get() calls: they select between existing MI_ and EST_ values.
# The fields below are ONLY those for which calculate_estimates() supplies a
# meaningful fallback; we do not duplicate every raw MediaInfo field.
#
# Each tuple is an ATOMIC resolution group. FRAME_RATE_NUM and FRAME_RATE_DEN
# are deliberately paired: choosing one numerator from MI and one denominator
# from EST could silently invent a frame rate not reported or estimated by
# either. If neither source supplies the full pair, both VAL values stay blank.
#
# For every suffix S in a group, the output is:
#   VAL_S         - the selected MI_S or EST_S, otherwise empty
#   VAL_S_SOURCE  - 'MI' or 'EST', otherwise empty
# The caller prefix SRC_ is applied at BAT generation, as with raw fields.
# A missing raw value is never converted to a fake 'N/A' or guessed default.
RESOLVED_GROUPS = (
    ('VIDEO_STANDARD',),
    ('VIDEO_FRAME_RATE_NUM', 'VIDEO_FRAME_RATE_DEN'),
    ('VIDEO_FRAME_COUNT',),
)

# ==============================================================================
# Helper functions: no hidden lists of MediaInfo.Get() parameter names elsewhere
# ==============================================================================
# Original deduce_standard()/deduce_fps_fraction() logic is retained in spirit,
# with output provenance separated: MI_* is NEVER overwritten with an estimate.
# For MPEG-2, frame counts can be container/duration-derived. MI_FRAME_COUNT is
# therefore "MediaInfo reported", not "verified counted by decoding".
# VAL_* names contain a selected best-available value, with a separate _SOURCE
# field indicating MI or EST. VAL is not a new measurement or estimate.


def deduce_standard(raw_standard: str, fps_str: str, height_str: str) -> str:
    """Return a tentative standard only when MediaInfo did not report one.

    Original approach: 25/50 fps or height 576/288 -> PAL; 23.976/29.97
    or height 480/240 -> NTSC. This is a *heuristic*, not a signal-format proof.
    Prefer frame rate over height and decline if the indicators conflict.
    """
    if raw_standard.strip():
        return ''
    try:
        fps = round(float(fps_str), 3)
        h = int(height_str)
    except (ValueError, TypeError, OverflowError):
        return ''
    rate_pal = fps in (25.0, 50.0)
    rate_ntsc = fps in (23.976, 29.97, 59.94)
    height_pal = h in (576, 288)
    height_ntsc = h in (480, 240)
    if rate_pal and not height_ntsc:
        return 'PAL (heuristic)'
    if rate_ntsc and not height_pal:
        return 'NTSC-family (heuristic)'
    return ''


def deduce_fps_fraction(fps_str: str, num_str: str, den_str: str) -> tuple[str, str]:
    """Original example's standard-frame-rate lookup, but estimate only if raw
    rational values are BOTH unavailable. Do not overwrite reported MI fields.
    """
    if num_str or den_str:
        # A partially reported pair is not an excuse to fabricate the other half.
        return '', ''
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
        if fps <= 0:
            return '', ''
        if fps in table:
            num, den = table[fps]
        else:
            frac = Fraction(fps).limit_denominator(1001)
            num, den = frac.numerator, frac.denominator
        return str(num), str(den)
    except (ValueError, TypeError, OverflowError, ZeroDivisionError):
        return '', ''


PREFIX_RE = re.compile(r'[A-Za-z][A-Za-z0-9_]*_\Z')
SAFE_SUFFIX_RE = re.compile(r'[A-Z][A-Z0-9_]*\Z')


def validate_catalogue() -> None:
    """Detect editing mistakes in the declarative field list immediately."""
    seen: set[tuple[str, str]] = set()
    for field in FIELDS:
        if field.group not in ('GENERAL', 'VIDEO', 'AUDIO'):
            raise ValueError(f'Bad catalogue group: {field.group}')
        if not SAFE_SUFFIX_RE.fullmatch(field.suffix):
            raise ValueError(f'Bad catalogue variable suffix: {field.suffix}')
        if not field.parameter:
            raise ValueError(f'Empty MediaInfo parameter: {field}')
        pair = (field.group, field.suffix)
        if pair in seen:
            raise ValueError(f'Duplicate catalogue output variable: {pair}')
        seen.add(pair)


def load_mediainfo(selected_dir: Path | None):
    """Import MediaInfoDLL3.py from ONE selected directory; keep DLL handles.

    Original example searched beside this script and in vapoursynth_path.
    Unlike the original eager import, this delays loading until after --help
    and --mediainfo-dir have been processed. No DLL download is attempted.
    """
    search_dirs = ([selected_dir] if selected_dir else
                   [Path(__file__).resolve().parent, Path(vapoursynth_path)])
    chosen = next((d.resolve() for d in search_dirs if d is not None
                   and (d / 'MediaInfoDLL3.py').is_file()
                   and (d / 'MediaInfo.dll').is_file()), None)
    if chosen is None:
        raise RuntimeError('Cannot find both MediaInfoDLL3.py and MediaInfo.dll. '
                           'Use --mediainfo-dir to select their directory.')

    # Python 3.8+ DLL search directories: the handle controls its lifetime.
    dll_handles = []
    if hasattr(os, 'add_dll_directory'):
        dll_handles.append(os.add_dll_directory(str(chosen)))
    # MediaInfoDLL3 imports native code from the chosen directory. This script
    # does not add every directory to sys.path, avoiding ambiguous DLL versions.
    sys.path.insert(0, str(chosen))
    try:
        from MediaInfoDLL3 import MediaInfo, Stream
    except (ImportError, OSError) as exc:
        raise RuntimeError(f'Failed loading MediaInfoDLL3 from {chosen}: {exc}') from exc
    return MediaInfo, Stream, dll_handles, chosen


def collect_fields(mi, Stream, video_index: int):
    """Perform only catalogue-declared Get calls; retain missing as empty.

    Raw source values are not silently converted to strings such as 'N/A',
    'CFR', 'Progressive', or 'Default'. One video track and ALL audio tracks.
    """
    n_video = int(mi.Count_Get(Stream.Video))
    n_audio = int(mi.Count_Get(Stream.Audio))
    if n_video <= video_index:
        raise ValueError(f'Video stream {video_index} unavailable; found {n_video}')
    if n_audio < 0 or n_video < 0:
        raise ValueError('MediaInfo returned negative stream count')

    vals: dict[str, str] = {
        'MI_VIDEO_STREAM_COUNT': str(n_video),
        'MI_AUDIO_STREAM_COUNT': str(n_audio),
        'MI_VIDEO_SELECTED_INDEX': str(video_index),
    }
    for field in FIELDS:
        if field.group == 'GENERAL':
            kind, index, name = Stream.General, 0, f'MI_GENERAL_{field.suffix}'
            vals[name] = mi.Get(kind, index, field.parameter) or ''
        elif field.group == 'VIDEO':
            kind, index, name = Stream.Video, video_index, f'MI_VIDEO_{field.suffix}'
            vals[name] = mi.Get(kind, index, field.parameter) or ''
        else:
            for a_idx in range(n_audio):
                name = f'MI_AUDIO_{a_idx}_{field.suffix}'
                vals[name] = mi.Get(Stream.Audio, a_idx, field.parameter) or ''
    return vals


def calculate_estimates(raw: dict[str, str]) -> dict[str, str]:
    """Populate estimates separately; absent dependencies -> empty values.

    EST_VIDEO_FRAME_COUNT is only populated when MI_VIDEO_FRAME_COUNT is absent
    and an explicitly non-VFR frame rate and valid video duration are available.
    It is approximate, NEVER an independently verified decoded frame count.
    """
    def get(name: str) -> str:
        return raw.get(f'MI_VIDEO_{name}', '').strip()

    standard = deduce_standard(get('STANDARD'), get('FRAME_RATE'), get('HEIGHT'))
    est_num, est_den = deduce_fps_fraction(
        get('FRAME_RATE'), get('FRAME_RATE_NUM'), get('FRAME_RATE_DEN'))
    frame_count = ''
    method = ''
    if not get('FRAME_COUNT') and get('FRAME_RATE_MODE').upper() != 'VFR':
        try:
            num_s = get('FRAME_RATE_NUM') or est_num
            den_s = get('FRAME_RATE_DEN') or est_den
            duration = Decimal(get('DURATION'))
            num, den = int(num_s), int(den_s)
            if num > 0 and den > 0 and duration > 0:
                frame_count = str(int((duration * Decimal(num) /
                                       (Decimal(1000) * Decimal(den)))
                                      .to_integral_value(rounding=ROUND_HALF_UP)))
                method = 'video_duration_ms_x_frame_rate_rounded'
        except (InvalidOperation, ValueError, OverflowError, ZeroDivisionError):
            pass
    return {
        'EST_VIDEO_STANDARD': standard,
        'EST_VIDEO_FRAME_RATE_NUM': est_num,
        'EST_VIDEO_FRAME_RATE_DEN': est_den,
        'EST_VIDEO_FRAME_COUNT': frame_count,
        'EST_VIDEO_FRAME_COUNT_METHOD': method,
    }


def resolve_values(raw_and_estimated: dict[str, str]) -> dict[str, str]:
    """Select one provenance-preserving best-available value per declared group.

    MI takes precedence over EST, but only when ALL values in a resolution
    group are present. This protects paired quantities such as the frame-rate
    numerator/denominator from being assembled from incompatible sources.

    An empty VAL or VAL_*_SOURCE means neither complete source was available.
    The original MI_ and independently calculated EST_ entries are unchanged.
    """
    resolved: dict[str, str] = {}
    for suffixes in RESOLVED_GROUPS:
        mi_names = [f'MI_{suffix}' for suffix in suffixes]
        est_names = [f'EST_{suffix}' for suffix in suffixes]
        if all(raw_and_estimated.get(k, '').strip() for k in mi_names):
            source, selected = 'MI', mi_names
        elif all(raw_and_estimated.get(k, '').strip() for k in est_names):
            source, selected = 'EST', est_names
        else:
            source, selected = '', None
        for pos, suffix in enumerate(suffixes):
            resolved[f'VAL_{suffix}'] = (
                raw_and_estimated[selected[pos]] if selected else '')
            resolved[f'VAL_{suffix}_SOURCE'] = source
    return resolved


def inspect_file(filepath: Path, MediaInfo, Stream, video_index: int) -> dict[str, str]:
    """Open one file, retrieve table-controlled metadata, close in finally.

    Original script's key steps are preserved: MediaInfo(), Open(), Count_Get(),
    Get(), Close(). Always pass an absolute Windows path to MediaInfo.Open().
    """
    mi = MediaInfo()
    opened = False
    try:
        if not mi.Open(str(filepath.resolve())):
            raise ValueError(f'MediaInfo could not open {filepath}')
        opened = True
        result = collect_fields(mi, Stream, video_index)
        result.update(calculate_estimates(result))
        # Resolving is a separate, final step; MI and EST stay unmodified.
        result.update(resolve_values(result))
        return result
    finally:
        # The original example closed on normal completion only. Always close
        # after successful Open, including when a Get() call raises an error.
        if opened:
            mi.Close()


def display_report(filepath: Path, vals: dict[str, str]) -> None:
    """Original example's readable report, now sourced from the field table.

    The detailed field inventory below exposes every enabled catalogue entry,
    including raw values that the concise summary does not display.
    """
    def g(name: str) -> str:
        return vals.get(name, '') or 'N/A'

    def v(name: str) -> str:
        return g('MI_VIDEO_' + name)

    sep = '=' * 75
    print(sep)
    print(f'File: {filepath.name}')
    print(f'Path: {filepath.resolve()}')
    print('-' * 75)
    print(f"  Container / Codec     : {g('MI_GENERAL_FORMAT')} | {v('FORMAT')} {v('FORMAT_VERSION')} ({v('FORMAT_PROFILE')})")
    print(f"  Dimensions (W x H)    : {v('WIDTH')} x {v('HEIGHT')} (DAR {v('DISPLAY_ASPECT_RATIO_S')}, PAR {v('PIXEL_ASPECT_RATIO')})")
    # The original example used fps_mode or 'CFR'. Missing != CFR.
    print(f"  Frame Rate Mode       : {v('FRAME_RATE_MODE')}")
    print(f"  Frame Rate            : {v('FRAME_RATE')} fps (Num: {v('FRAME_RATE_NUM')} / Den: {v('FRAME_RATE_DEN')})")
    print(f"  Standard              : {v('STANDARD')} (estimate: {g('EST_VIDEO_STANDARD')})")
    print(f"  Scan Type             : {v('SCAN_TYPE')}")
    # Unknown scan type must not be silently labelled progressive.
    scan = vals.get('MI_VIDEO_SCAN_TYPE', '').lower()
    if scan == 'interlaced':
        field_order = f"{v('SCAN_ORDER')} ({v('SCAN_ORDER_S')})"
    elif scan == 'progressive':
        field_order = 'N/A (Progressive)'
    else:
        field_order = v('SCAN_ORDER')
    print(f'  Field Order           : {field_order}')
    print(f"  Video Bitrate         : {v('BITRATE_S')} ({v('BITRATE_MODE')}; Max: {v('BITRATE_MAXIMUM_S')})")
    print(f"  Duration / Frames     : {g('MI_GENERAL_DURATION_STRING3')} ({v('FRAME_COUNT')} reported frames)")
    print(f"  Estimated Frames      : {g('EST_VIDEO_FRAME_COUNT')} (only if no reported count)")
    # VAL_ is convenient for BAT/Python callers, and does not obscure whether
    # the chosen value came from MediaInfo or from our fallback calculation.
    print(f"  Resolved Frames       : {g('VAL_VIDEO_FRAME_COUNT')} (source: {g('VAL_VIDEO_FRAME_COUNT_SOURCE')})")
    # No longer label an unknown matrix as 'Default'.
    print(f"  Color Space / Matrix  : {v('COLOR_SPACE')} {v('CHROMA_SUBSAMPLING')} {v('BIT_DEPTH')}-bit | Matrix: {v('MATRIX_COEFFICIENTS')}")
    print(f"  File Size             : {g('MI_GENERAL_FILE_SIZE_STRING')}")
    n_audio = int(vals['MI_AUDIO_STREAM_COUNT'])
    if n_audio:
        for a_idx in range(n_audio):
            p = f'MI_AUDIO_{a_idx}_'
            print(f"  Audio #{a_idx+1}            : {g(p + 'FORMAT')} {g(p + 'CHANNELS_S')} @ {g(p + 'SAMPLING_RATE_S')}, {g(p + 'BITRATE_S')} [{g(p + 'LANGUAGE_S')}]")
    else:
        print('  Audio Streams         : None')
    print('  --- All enabled MI_, EST_, and provenance-tagged VAL_ fields ---')
    for key, value in vals.items():
        print(f'  {key:<43} : {value or "<missing>"}')
    print(sep)


def validate_batch_value(key: str, value: str) -> None:
    """Fail closed if a raw value cannot be assigned literally in any CMD mode.

    SET "NAME=value" safely encloses spaces and common punctuation. However,
    quotes, percent expansion, delayed exclamation expansion, caret escape,
    CR/LF, non-ASCII and overly long lines are dangerous or non-portable.
    A faithful export must refuse these rather than silently sanitise data.
    Comment out problematic free-text catalogue entries if not required.
    """
    if not isinstance(value, str):
        raise ValueError(f'{key}: non-string MediaInfo return value')
    if any(ord(c) < 32 or ord(c) > 126 or c in '"%!^' for c in value):
        raise ValueError(f'{key}: contains characters unsafe for portable CMD export; '
                         'disable this field in FIELDS or use a safe source')
    if len(key) + len(value) + 9 > 7500:
        raise ValueError(f'{key}: too long for safe CMD command-line handling')


def make_batch(prefix: str, vals: dict[str, str]) -> str:
    """Return standalone CALL-able BAT body, with namespace clearing.

    NO SETLOCAL: SETLOCAL would roll back all exports at EOF. Prefix is strictly
    restricted to identifiers ending in underscore. %VAR% is not used inside
    the generated assignments. Always emit even missing fields as empty SET.
    MI_ and EST_ remain intact; VAL_ variables select one source transparently.
    """
    if not PREFIX_RE.fullmatch(prefix):
        raise ValueError('Prefix must match [A-Za-z][A-Za-z0-9_]*_ (for example SRC_)')
    items = [(prefix + key, val) for key, val in vals.items()]
    items.append((prefix + 'METADATA_OK', '1'))
    for key, value in items:
        validate_batch_value(key, value)
    lines = [
        'REM @echo off',
        'REM Generated by mpeg2deblock_fetch_metadata.py.',
        'REM Intended to be run via CALL from a Windows CMD/BAT script.',
        'REM Clears only the requested namespace, including obsolete fields.',
        'REM CAUTION: do not invoke from a caller with delayed expansion enabled',
        'REM if that caller later reads values containing exclamation marks.',
        f"for /f \"tokens=1 delims==\" %%V in ('set {prefix} 2^>nul') do set \"%%V=\"",
    ]
    # Metadata status comes LAST so the caller can recognise completed export.
    for key, value in items:
        lines.append(f'set "{key}={value}"')
    lines.append('exit /b 0')
    # CRLF is mandatory for consistent Windows processing. No UTF-8 BOM.
    return '\r\n'.join(lines) + '\r\n'


def atomic_write_ascii(path: Path, content: str) -> None:
    """Atomically replace one BAT after all values have been validated."""
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temp_name = tempfile.mkstemp(prefix='.__metadata_', suffix='.tmp',
                                           dir=str(path.parent))
    try:
        with os.fdopen(descriptor, 'w', encoding='ascii', newline='') as out:
            out.write(content)
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def selected_files(source: Path, recursive: bool, extensions: list[str]) -> list[Path]:
    """Original script's folder-scan behaviour, now also supporting one file."""
    if source.is_file():
        return [source]
    if not source.is_dir():
        raise ValueError(f'File or folder does not exist: {source}')
    ext_set = {e.lower() if e.startswith('.') else '.' + e.lower() for e in extensions}
    pattern = '**/*' if recursive else '*'
    return sorted((f for f in source.glob(pattern)
                   if f.is_file() and f.suffix.lower() in ext_set),
                  key=lambda p: str(p).casefold())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description='Inspect MPEG-2/MPG characteristics using MediaInfo.dll; optionally export CALL-able BAT files.')
    parser.add_argument('source', nargs='?', default='.',
                        help='Video file or folder of video files (default: current folder).')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Search subdirectories recursively (folder mode).')
    parser.add_argument('--ext', nargs='+', default=['.mpg', '.mpeg', '.m2v'],
                        help='File extensions for folder scans (default: .mpg .mpeg .m2v).')
    parser.add_argument('--mediainfo-dir', type=Path, default=None,
                        help='Directory containing both MediaInfo.dll and MediaInfoDLL3.py.')
    parser.add_argument('--video-index', type=int, default=0,
                        help='Zero-based video stream to query (default: 0).')
    parser.add_argument('--prefix', default='SRC_',
                        help='Batch variable prefix ending in underscore (default: SRC_).')
    outputs = parser.add_mutually_exclusive_group()
    outputs.add_argument('--bat', type=Path, default=None,
                         help='Generate exactly this BAT path (single source file only).')
    outputs.add_argument('--bat-dir', type=Path, default=None,
                         help='Generate one *_metadata.bat per MPG in this folder; mirror subfolders.')
    parser.add_argument('--quiet', action='store_true',
                        help='Suppress full human-readable reports; still print outputs and errors.')
    args = parser.parse_args(argv)
    if args.video_index < 0:
        parser.error('--video-index must be nonnegative')
    if not PREFIX_RE.fullmatch(args.prefix):
        parser.error('--prefix must end in _ and contain only ASCII letters, digits and underscores')
    src = args.source and Path(args.source).resolve()
    if args.bat is not None and not src.is_file():
        parser.error('--bat requires a single input file; use --bat-dir for a folder')
    validate_catalogue()
    files = selected_files(src, args.recursive, args.ext)
    if not files:
        print(f'No matching files found in: {src}', file=sys.stderr)
        return 2
    # Pre-check all destination collisions before generating anything.
    bat_paths: dict[Path, Path] = {}
    used: set[str] = set()
    for filepath in files:
        if args.bat is not None:
            destination = args.bat.resolve()
        elif args.bat_dir is not None:
            relative = filepath.relative_to(src) if src.is_dir() else Path(filepath.name)
            destination = args.bat_dir.resolve() / relative.parent / f'{filepath.stem}_metadata.bat'
        else:
            continue
        canonical = str(destination).casefold()
        if canonical in used:
            raise ValueError(f'Duplicate metadata BAT destination: {destination}')
        used.add(canonical)
        if destination.resolve() == filepath.resolve():
            raise ValueError('Refusing to overwrite the video source')
        bat_paths[filepath] = destination
    MediaInfo, Stream, dll_handles, chosen_dir = load_mediainfo(args.mediainfo_dir)
    print(f'MediaInfo directory: {chosen_dir}')
    print(f'Found {len(files)} file(s) in {src}')
    failures = 0
    for filepath in files:
        try:
            vals = inspect_file(filepath, MediaInfo, Stream, args.video_index)
            if not args.quiet:
                display_report(filepath, vals)
            if filepath in bat_paths:
                # Do not create/replace the output until every value is safe.
                bat_text = make_batch(args.prefix, vals)
                atomic_write_ascii(bat_paths[filepath], bat_text)
                print(f'BAT: {bat_paths[filepath]}')
        except (OSError, ValueError, RuntimeError, UnicodeError) as exc:
            failures += 1
            print(f'[ERROR] {filepath}: {exc}', file=sys.stderr)
    if failures:
        print(f'FAILED: {failures}/{len(files)} file(s)', file=sys.stderr)
        return 1
    print(f'PASS: {len(files)} file(s)')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, RuntimeError) as exc:
        print(f'[FATAL] {exc}', file=sys.stderr)
        sys.exit(1)

# ==============================================================================
# HISTORICAL EXPLANATORY COMMENTARY FROM THE ATTACHED GOOGLE AI STUDIO EXAMPLE
# ==============================================================================
# The following original documentation is retained for continuity. It describes
# the same general architecture; inspect_file() above supersedes its old example.
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

