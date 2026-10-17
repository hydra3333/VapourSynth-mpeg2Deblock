#!/usr/bin/env python3
"""S2-I3 P0 exact P-skip admission. No filtering; no VapourSynth dependency.

The caller MUST independently verify BestSource/index frame counts, dimensions,
_PictType and the SHA256 of the *actual* index opened. Frames are native plane-0
read-only stride-aware uint8 arrays. Do not reinterpret NONE as SKIPPED.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Callable
import numpy as np

# Axis shifts include all seven historically tested S2-I2 incorrect offsets.
OFFSETS = tuple((v, 0) for v in (-16, -8, -4, -2, -1, 1, 2, 4, 8, 16)) + \
          tuple((0, v) for v in (-16, -8, -4, -2, -1, 1, 2, 4, 8, 16)) + \
          ((-1, -1), (-1, 1), (1, -1), (1, 1))
assert len(OFFSETS) == 24 and len(set(OFFSETS)) == 24
TEMPORAL = ('older_anchor', 'next_display', 'previous_display')
MIN_SKIPS = 200
MIN_P_PICTURES = 10


class AdmissionStructureError(ValueError):
    """A structural failure is distinct from a non-discriminating test."""


def inspect_record_order(index) -> list[int | None]:
    """Returns the preceding I/P display-order anchor for each picture."""
    if not index.records:
        raise AdmissionStructureError('empty index')
    anchors = []
    anchor = None
    for n, rec in enumerate(index.records):
        if rec.output_ordinal != n:
            raise AdmissionStructureError(f'index output_ordinal mismatch at {n}')
        if rec.picture_type not in ('I', 'P', 'B'):
            raise AdmissionStructureError(f'unsupported picture type at {n}')
        if rec.picture_structure != 3 or rec.chroma_format != 1:
            raise AdmissionStructureError(f'picture {n} must be a frame picture, 4:2:0')
        if rec.coded_width != index.width or rec.coded_height != index.height or \
           rec.mb_width * 16 != index.width or rec.mb_height * 16 != index.height:
            raise AdmissionStructureError(f'picture {n} dimensions or MB grid mismatch')
        anchors.append(anchor)
        if rec.picture_type in ('I', 'P'):
            anchor = n
    return anchors


def check_view(y, width: int, height: int):
    if not isinstance(y, np.ndarray) or y.dtype != np.dtype('uint8') or \
       y.shape != (height, width) or y.ndim != 2:
        raise AdmissionStructureError('frame Y must be native uint8, exact indexed dimensions')
    if y.flags.writeable:
        # Inputs from the BestSource adapter must be read-only; test fixtures too.
        raise AdmissionStructureError('frame Y is writeable; unsafe source plane')


def _positions(rec):
    """Use coding=1, never transform/NONE or INTER CBP=0 as a proxy."""
    for m, mb in enumerate(rec.iter_macroblocks()):
        if mb.coding == 1:
            yield (m % rec.mb_width) * 16, (m // rec.mb_width) * 16


def _compare_windows(a, b, positions, dx=0, dy=0):
    if a.shape != b.shape:
        raise AdmissionStructureError('reference luma size differs from current')
    h, w = a.shape
    valid = exact = 0
    for x, y in positions:
        xx, yy = x + dx, y + dy
        if xx < 0 or yy < 0 or xx + 16 > w or yy + 16 > h:
            continue
        valid += 1
        # Offset BOTH pictures identically. Never wrap or pad.
        exact += int(np.array_equal(a[yy:yy+16, xx:xx+16], b[yy:yy+16, xx:xx+16]))
    return valid, exact


def _make_counter():
    return {'compared': 0, 'identical': 0, 'excluded_picture_count': 0}


def run_pskip(index, get_luma: Callable[[int], np.ndarray]):
    """Return stable JSON-compatible evidence. Never mutate or persist pixels.

    Structural/type/stride conditions MUST be verified by the injected provider
    and the caller; this routine verifies its own structural preconditions.
    """
    anchors = inspect_record_order(index)
    controls = {f'{dx},{dy}': _make_counter() for dx, dy in OFFSETS}
    temporal = {name: _make_counter() for name in TEMPORAL}
    true_total = true_exact = p_count = without_anchor = 0
    rows = []
    failures = []
    seen = {}

    def get(n):
        if n not in seen:
            value = get_luma(n)
            check_view(value, index.width, index.height)
            seen[n] = value
            if len(seen) > 6:
                seen.pop(next(iter(seen)))
        return seen[n]

    for n, rec in enumerate(index.records):
        if rec.picture_type != 'P':
            continue
        if anchors[n] is None:
            without_anchor += 1
            continue
        coords = list(_positions(rec))
        if not coords:
            continue
        p_count += 1
        a = get(n)
        ref = get(anchors[n])
        n_valid, n_exact = _compare_windows(a, ref, coords)
        if n_valid != len(coords):
            raise AdmissionStructureError(f'P picture {n}: true-position skipped block outside frame')
        true_total += n_valid
        true_exact += n_exact
        if n_exact != n_valid:
            failures.append({'picture': n, 'mismatched_skips': n_valid - n_exact})
        rows.append({'picture': n, 'anchor': anchors[n], 'p_skips': n_valid,
                     'exact': n_exact})
        for dx, dy in OFFSETS:
            counter = controls[f'{dx},{dy}']
            count, exact = _compare_windows(a, ref, coords, dx, dy)
            counter['compared'] += count
            counter['identical'] += exact
            if count == 0:
                counter['excluded_picture_count'] += 1
        # A is preceding anchor before the true anchor. B/C are DISPLAY-order
        # neighbours, not compressed/decode order. Exclude equal-to-true-anchor.
        control_refs = {
            'older_anchor': anchors[anchors[n]],
            'next_display': n + 1 if n + 1 < index.frame_count else None,
            'previous_display': n - 1 if n - 1 != anchors[n] else None,
        }
        for name in TEMPORAL:
            c = temporal[name]
            t = control_refs[name]
            if t is None or t == n or t == anchors[n]:
                c['excluded_picture_count'] += 1
                continue
            z = get(t)
            count, exact = _compare_windows(a, z, coords)
            c['compared'] += count
            c['identical'] += exact

    # Apply decisions in order: structural errors already raised by parser/checks;
    # any true-position difference overrides inconclusive controls/populations.
    if failures:
        status, reason = 'FAIL', 'non-identical P-skip block at indexed true position'
    elif true_total < MIN_SKIPS or p_count < MIN_P_PICTURES:
        status, reason = 'INCONCLUSIVE', 'below declared >=200 MB / >=10 P-picture floor'
    else:
        bad = [name for name, c in list(controls.items()) + list(temporal.items())
               if c['compared'] == 0 or c['identical'] == c['compared']]
        if bad:
            status, reason = 'INCONCLUSIVE', 'missing or nondiscriminating controls: ' + ', '.join(bad)
        else:
            status, reason = 'REGISTERED', 'all structural/true-position/negative-control gates met'
    return {
        'schema': 'S2-I3-P0-PSKIP-1', 'status': status, 'reason': reason,
        'record_count': index.frame_count, 'picture_count_with_qualified_pskips': p_count,
        'P_pictures_without_anchor_excluded': without_anchor,
        'true_position': {'compared': true_total, 'identical': true_exact},
        'control_offsets': {key: controls[key] for key in sorted(controls)},
        'temporal_controls': temporal, 'per_P_picture': rows,
        'first_mismatches': failures[:20], 'control_count': len(OFFSETS),
        'method': 'native Y 16x16 uint8 exact copy; index SKIPPED in P frame; display-order I/P anchor',
    }
