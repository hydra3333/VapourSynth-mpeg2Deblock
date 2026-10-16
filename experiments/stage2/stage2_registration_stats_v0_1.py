"""S2-I2 diagnostic mathematics: NumPy + frozen S2-I1 records; no VapourSynth dependency.

No pixel filtering, no pixel-based seam location. v0.1 IMPLEMENTATION CANDIDATE.
"""
from __future__ import annotations

from collections import Counter, defaultdict
import csv
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable

import numpy as np

TRANSFORM = {0: 'NONE', 1: 'FRAME', 2: 'FIELD'}
CODING = {1: 'SKIPPED', 2: 'INTRA', 3: 'INTER'}
CATEGORIES = {0:'CONTROL', 1:'INTERNAL-FRAME', 2:'INTERNAL-FIELD',
              3:'MID-FIELD-NO-CODED-SEAM', 4:'NONE-SKIPPED-P',
              5:'NONE-SKIPPED-B', 6:'NONE-INTER-CBP0', 7:'NONE-OTHER', 8:'OUTER'}
PICTURE_CODES = {'I':1, 'P':2, 'B':3}
PICTURE_NAMES = {v:k for k,v in PICTURE_CODES.items()}
ENTRY_DTYPE = np.dtype([('o','i1'),('cat','i1'),('p','i1'),('q','i1'),('frame','i2'),
                        ('gop','i2'),('plain','f4'),('robust','f4'),('t','i1'),
                        ('coding','i1'),('nt','i1'),('nc','i1'),('nq','i1')])
OFFSETS = [(0, 0), (4, 0), (8, 0), (16, 0), (0, 1), (0, 2), (0, 8), (0, 16)]
SHIFTS = [(dx, dy) for dy in (-1, 0, 1) for dx in (-1, 0, 1)]
ROW_MARGIN = 0.05
OTHER_MARGIN = 0.10
FRAME_FRACTION = 2.0 / 3.0
# Predeclared bands (QP 112 saturation is isolated, per Stage 2 v0.6 13.5).
QP_BANDS = [('QP_0_15', 0, 15), ('QP_16_31', 16, 31),
            ('QP_32_63', 32, 63), ('QP_64_111', 64, 111),
            ('QP_112', 112, 112), ('QP_ABOVE_112', 113, 127)]
BORDER = 16


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def write_csv(path: Path, rows: Iterable[dict], columns: list[str]):
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=columns, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)


def check_luma(y, record):
    if not isinstance(y, np.ndarray) or y.ndim != 2 or y.dtype != np.int16:
        raise ValueError('luma must be a two-dimensional int16 NumPy copy of unmodified plane 0')
    h, w = y.shape
    if w != record.coded_width or h != record.coded_height or w % 16 or h % 16:
        raise ValueError('luma/index dimensions or 16x16 grid mismatch')
    if w < 64 or h < 64 or (record.mb_width, record.mb_height) != (w // 16, h // 16):
        raise ValueError('unsupported macroblock grid')
    if record.picture_structure != 3 or record.chroma_format != 1:
        raise ValueError('only frame pictures and native MPEG-2 4:2:0 are supported')
    if np.any(y < 0) or np.any(y > 255):
        raise ValueError('expected unchanged 8-bit Y plane; no pixel-format conversion')


def displaced(y, cx, ry):
    """Positive cx/ry moves PIXELS right/down; index stays fixed. No wrap at edges.

    Only invariant 16-pixel interior is measured; padding never enters those samples.
    """
    if not (0 <= cx <= BORDER and 0 <= ry <= BORDER):
        raise ValueError('control offset outside fixed 16-pixel protected border')
    if cx == ry == 0:
        return y
    out = np.zeros_like(y)
    out[ry:, cx:] = y[:y.shape[0] - ry, :y.shape[1] - cx]
    return out


def mb_labels(rec):
    t = np.empty((rec.mb_height, rec.mb_width), dtype=np.int8)
    c = np.empty_like(t)
    q = np.empty_like(t)
    for i, mb in enumerate(rec.iter_macroblocks()):
        my, mx = divmod(i, rec.mb_width)
        t[my, mx], c[my, mx], q[my, mx] = mb.transform, mb.coding, mb.q
    return t, c, q


def d_maps(y):
    h, w = y.shape
    hh, ww = h // 16, w // 16
    # Pair order is same-field: 6|8, 7|9; never 7|8.
    even = np.abs(y[8::16] - y[6::16]).reshape(hh, ww, 16).mean(axis=2)
    odd = np.abs(y[9::16] - y[7::16]).reshape(hh, ww, 16).mean(axis=2)
    background = sum(np.abs(y[b::16] - y[a::16]).reshape(hh, ww, 16).mean(axis=2)
                     for a, b in ((2, 4), (3, 5), (10, 12), (11, 13))) / 4.0
    raw = (even + odd) / 2.0
    return raw, raw - background, even, odd, background


def contrast_for_shift(d, labels, dx, dy):
    # Target lattice does not move under label shifts: MB x,y in [1,last-1).
    hh, ww = labels.shape
    target = d[1:hh - 1, 1:ww - 1]
    lab = labels[1 - dy:hh - 1 - dy, 1 - dx:ww - 1 - dx]
    fs, bs = target[lab == 1], target[lab == 2]
    if len(fs) == 0 or len(bs) == 0:
        return float('nan'), int(len(fs)), int(len(bs)), float('nan'), float('nan')
    return float(fs.mean() - bs.mean()), int(len(fs)), int(len(bs)), float(fs.mean()), float(bs.mean())


def phase_stats(y):
    h, w = y.shape
    # right-side column x; fixed target sample domain x=16..w-17, y=16..h-17.
    xs = np.arange(BORDER, w - BORDER)
    col_diff = np.abs(y[BORDER:h - BORDER, BORDER:w - BORDER] -
                      y[BORDER:h - BORDER, BORDER - 1:w - BORDER - 1])
    col_sums = np.bincount(xs % 8, weights=col_diff.sum(axis=0), minlength=8)
    col_counts = np.bincount(xs % 8, minlength=8) * (h - 2 * BORDER)
    ys = np.arange(BORDER, h - BORDER)
    row_diff = np.abs(y[BORDER + 2:h - BORDER + 2, BORDER:w - BORDER] -
                      y[BORDER:h - BORDER, BORDER:w - BORDER])
    row_sums = np.bincount(ys % 8, weights=row_diff.sum(axis=1), minlength=8)
    row_counts = np.bincount(ys % 8, minlength=8) * (w - 2 * BORDER)
    return col_sums, col_counts, row_sums, row_counts


def rank_top(values, targets):
    if not np.all(np.isfinite(values)):
        return False
    k = len(targets)
    hi = min(values[j] for j in targets)
    return all(hi > values[j] for j in range(len(values)) if j not in targets)


def gates(c, c_frames, col_s, col_n, row_s, row_n, col_frames, row_frames):
    # Strict ties are INCONCLUSIVE for 3x3/column, FAIL for row outside top-two tie.
    zero = c[SHIFTS.index((0, 0))]
    nonzero = [v for (s, v) in zip(SHIFTS, c) if s != (0, 0)]
    best_alt = max(nonzero, default=float('nan'))
    if not np.isfinite(zero) or not np.isfinite(best_alt) or zero <= 0:
        three = 'INCONCLUSIVE'
    elif best_alt > zero:
        three = 'FAIL'
    elif zero == best_alt:
        three = 'INCONCLUSIVE'
    elif (zero - best_alt) / zero >= OTHER_MARGIN and c_frames >= FRAME_FRACTION:
        three = 'PASS'
    else:
        three = 'INCONCLUSIVE'
    cm = col_s / np.maximum(col_n, 1)
    rm = row_s / np.maximum(row_n, 1)
    c_other = float(max(cm[1:]))
    c_margin = float((cm[0] - c_other) / cm[0]) if cm[0] > 0 else float('nan')
    if cm[0] < c_other and np.count_nonzero(cm == cm.max()) == 1:
        cg = 'FAIL'
    elif cm[0] > c_other and c_margin >= OTHER_MARGIN:
        cg = 'PASS'
    else:
        cg = 'INCONCLUSIVE'
    rlow, rother = float(min(rm[6], rm[7])), float(max(rm[:6]))
    rmargin = float((rlow - rother) / rlow) if rlow > 0 else float('nan')
    if rlow <= rother:  # any outside phase in aggregate top-two, including tie => FAIL
        rg = 'FAIL'
    elif rmargin >= ROW_MARGIN and row_frames >= FRAME_FRACTION:
        rg = 'PASS'
    else:
        rg = 'INCONCLUSIVE'
    return {'shift': three, 'column': cg, 'row': rg, 'contrast_zero': zero,
            'contrast_best_other': best_alt, 'column_margin': c_margin,
            'row_margin': rmargin, 'column_means': cm.tolist(), 'row_means': rm.tolist(), 'c': c.tolist(),
            'shift_frame_fraction': c_frames, 'column_frame_fraction': col_frames,
            'row_frame_fraction': row_frames}


def _score_vertical(blk, cx, left_blk=None):
    """All MBs at once; output two float arrays shaped (MB rows, MB columns)."""
    right = blk
    left = blk if left_blk is None else left_blk
    if left_blk is None:
        cross = right[..., :, cx] - right[..., :, cx - 1]
        low = left[..., :, cx - 2] - left[..., :, cx - 3]
        high = right[..., :, cx + 2] - right[..., :, cx + 1]
    else:
        # x=16*mx, previous macroblock on left, current MB on right.
        cross = right[..., :, 0] - left[..., :, 15]
        low = left[..., :, 14] - left[..., :, 13]
        high = right[..., :, 2] - right[..., :, 1]
    comps = np.stack((low, high), axis=-1)
    plain = np.abs(cross).mean(axis=-1) - np.abs(comps).mean(axis=(-1, -2))
    robust = 0
    for parity in (0, 1):
        a = cross[..., parity::2]
        b = comps[..., parity::2, :]
        robust = robust + np.abs(a.mean(axis=-1) - b.mean(axis=(-1, -2))) / (np.abs(b).mean(axis=(-1, -2)) + 1.0) / 2.0
    return plain, robust


def _score_horizontal(blk, kind, prev_blk=None):
    # Signed steps lower-upper; each parity and each 8-column chunk has its own robust score.
    if kind == 'mid':
        pairs = ((6, 8, 4, 6, 8, 10), (7, 9, 5, 7, 9, 11))
    elif kind == 'c4':
        pairs = ((2, 4, 0, 2, 4, 6), (3, 5, 1, 3, 5, 7))
    elif kind == 'c12':
        pairs = ((10, 12, 8, 10, 12, 14), (11, 13, 9, 11, 13, 15))
    elif kind == 'outer':
        if prev_blk is None:
            raise ValueError('outer horizontal requires upper MB')
        pairs = None
    else:
        raise ValueError('invalid horizontal class')
    robust = np.zeros(blk.shape[:2], dtype=np.float64)
    abs_cross = 0.0
    abs_comp = 0.0
    for parity in (0, 1):
        if kind == 'outer':
            if parity == 0:
                cross = blk[..., 0, :] - prev_blk[..., 14, :]
                a = prev_blk[..., 14, :] - prev_blk[..., 12, :]
                b = blk[..., 2, :] - blk[..., 0, :]
            else:
                cross = blk[..., 1, :] - prev_blk[..., 15, :]
                a = prev_blk[..., 15, :] - prev_blk[..., 13, :]
                b = blk[..., 3, :] - blk[..., 1, :]
        else:
            above, below, a0, a1, b0, b1 = pairs[parity]
            cross = blk[..., below, :] - blk[..., above, :]
            a = blk[..., a1, :] - blk[..., a0, :]
            b = blk[..., b1, :] - blk[..., b0, :]
        abs_cross = abs_cross + np.abs(cross).mean(axis=-1) / 2.0
        abs_comp = abs_comp + (np.abs(a).mean(axis=-1) + np.abs(b).mean(axis=-1)) / 4.0
        for start in (0, 8):
            u = cross[..., start:start + 8]
            v = np.stack((a[..., start:start + 8], b[..., start:start + 8]), axis=-1)
            robust += np.abs(u.mean(axis=-1) - v.mean(axis=(-1, -2))) / (np.abs(v).mean(axis=(-1, -2)) + 1.0) / 4.0
    return abs_cross - abs_comp, robust


def _none_subclass(rec, c):
    if c == 1:
        return 'NONE-SKIPPED-P' if rec.picture_type == 'P' else 'NONE-SKIPPED-B' if rec.picture_type == 'B' else 'NONE-SKIPPED-OTHER'
    if c == 3:
        return 'NONE-INTER-CBP0'
    return 'NONE-OTHER'


def scored_segments(y, rec, labels):
    """Yield (orientation, class, plain, robust, picture, q, frame, owner states).

    Arrays are per segment (MB). No decoded images or pixel maps persist.
    """
    t, coding, qp = labels
    h, w = y.shape
    blk = y.reshape(h // 16, 16, w // 16, 16).transpose(0, 2, 1, 3)
    # Numeric categorical codes to keep bounded memory, convert to text on aggregation.
    # Standard non-seam controls: local x=4,12; horizontal 3|4,11|12.
    for x, name in ((4, 'CONTROL_4'), (8, 'MID'), (12, 'CONTROL_12')):
        plain, robust = _score_vertical(blk, x)
        yield 'V', name, plain, robust, t, coding, qp, None, None, None
    # Outer edge attributed to right MB, states from immediate left and right.
    a, b = _score_vertical(blk[:, 1:], 0, blk[:, :-1])
    yield 'V', 'OUTER', a, b, t[:, 1:], coding[:, 1:], qp[:, 1:], t[:, :-1], coding[:, :-1], qp[:, :-1]
    for kind, name in (('c4', 'CONTROL_4'), ('mid', 'MID'), ('c12', 'CONTROL_12')):
        a, b = _score_horizontal(blk, kind)
        yield 'H', name, a, b, t, coding, qp, None, None, None
    a, b = _score_horizontal(blk[1:], 'outer', blk[:-1])
    yield 'H', 'OUTER', a, b, t[1:], coding[1:], qp[1:], t[:-1], coding[:-1], qp[:-1]


def segment_category(rec, orientation, name, t, coding):
    if name.startswith('CONTROL'):
        return 'CONTROL'
    if name == 'OUTER':
        return 'OUTER'
    if t == 0:
        return _none_subclass(rec, coding)
    if orientation == 'H' and t == 2:
        return 'MID-FIELD-NO-CODED-SEAM'
    return 'INTERNAL-' + TRANSFORM[t]


def auc_vs_sorted(pos, sorted_controls):
    """Tie-aware AUC with one pre-sorted control population per orientation/metric."""
    p = np.asarray(pos, np.float64)
    n = sorted_controls
    if not len(p) or not len(n):
        return float('nan')
    less = np.searchsorted(n, p, side='left')
    equal = np.searchsorted(n, p, side='right') - less
    return float(np.mean((less + 0.5 * equal) / len(n)))


def auc_rank(pos, neg):
    return auc_vs_sorted(pos, np.sort(np.asarray(neg, np.float64)))


def percentile95_nearest(vals):
    # Select smallest score with at least 95% of controls <= it. Hit: strictly > threshold.
    if not len(vals):
        return float('nan')
    vals = np.sort(np.asarray(vals, np.float64))
    return float(vals[math.ceil(0.95 * len(vals)) - 1])


def _none_subclass_name(picture_code, t, coding):
    if t != 0:
        return ''
    if coding == 1 and picture_code == 2:
        return 'NONE-SKIPPED-P'
    if coding == 1 and picture_code == 3:
        return 'NONE-SKIPPED-B'
    if coding == 3:
        return 'NONE-INTER-CBP0'
    return 'NONE-OTHER'


def quantile(values, fraction):
    return float(np.quantile(values, fraction)) if len(values) else float('nan')


def groups_by(entries, field):
    if not len(entries):
        return
    for key in np.unique(entries[field]):
        yield int(key), entries[entries[field] == key]


def groups_by_multiple(entries, fields):
    if not len(entries):
        return
    keys = np.stack([entries[f] for f in fields], axis=1)
    uniques, codes = np.unique(keys, axis=0, return_inverse=True)
    for j, key in enumerate(uniques):
        yield tuple(map(int, key)), entries[codes == j]


def clean_json(obj):
    if isinstance(obj, dict):
        return {k: clean_json(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [clean_json(x) for x in obj]
    if isinstance(obj, (float, np.floating)) and not math.isfinite(float(obj)):
        return None
    if isinstance(obj, np.generic):
        return obj.item()
    return obj


class RegistrationRun:
    def __init__(self, index, outdir, src, decoder_id, kind, runtime_info=None):
        self.index = index
        self.outdir = Path(outdir)
        self.outdir.mkdir(parents=True, exist_ok=True)
        self.src = str(src)
        self.decoder_id = decoder_id
        self.runtime_info = runtime_info or {}
        self.kind = kind
        self.offset_data = {o: self._empty() for o in OFFSETS}
        self.entries = []
        self.frame_stats = []
        self.seam_counts = Counter()
        self.gop = -1
        self.processed = 0

    @staticmethod
    def _empty():
        return {'frame_sums': np.zeros(9), 'field_sums': np.zeros(9),
                'frame_counts': np.zeros(9, int), 'field_counts': np.zeros(9, int),
                'norm_frame_sums': np.zeros(9), 'norm_field_sums': np.zeros(9),
                'col_sums': np.zeros(8), 'col_counts': np.zeros(8, int),
                'row_sums': np.zeros(8), 'row_counts': np.zeros(8, int),
                'shift_wins': 0, 'shift_eligible': 0, 'row_wins': 0,
                'row_eligible': 0, 'col_wins': 0, 'col_eligible': 0}

    def process(self, ordinal, y):
        rec = self.index.records[ordinal]
        check_luma(y, rec)
        if self.index.quality_excluded(ordinal):
            return
        if rec.picture_type == 'I':
            self.gop += 1
        # Trailing B after the last I count in its I-started display-order GOP.
        labels = mb_labels(rec)
        for offset, data in self.offset_data.items():
            z = displaced(y, *offset)
            draw, dn, _, _, _ = d_maps(z)
            C, Cn = [], []
            for dx, dy in SHIFTS:
                raw, fc, bc, fm, bm = contrast_for_shift(draw, labels[0], dx, dy)
                norm, _, _, fn, bn = contrast_for_shift(dn, labels[0], dx, dy)
                C.append(raw)
                Cn.append(norm)
                i = SHIFTS.index((dx, dy))
                if fc and bc:
                    data['frame_sums'][i] += fm * fc
                    data['field_sums'][i] += bm * bc
                    data['norm_frame_sums'][i] += fn * fc
                    data['norm_field_sums'][i] += bn * bc
                    data['frame_counts'][i] += fc
                    data['field_counts'][i] += bc
            col_s, col_n, row_s, row_n = phase_stats(z)
            data['col_sums'] += col_s
            data['col_counts'] += col_n
            data['row_sums'] += row_s
            data['row_counts'] += row_n
            if np.all(np.isfinite(C)):
                data['shift_eligible'] += 1
                if C[4] > max(v for j, v in enumerate(C) if j != 4):
                    data['shift_wins'] += 1
            row_m = row_s / np.maximum(row_n, 1)
            data['row_eligible'] += 1
            if rank_top(row_m, (6, 7)):
                data['row_wins'] += 1
            col_m = col_s / np.maximum(col_n, 1)
            data['col_eligible'] += 1
            if rank_top(col_m, (0,)):
                data['col_wins'] += 1
            if offset == (0, 0):
                self.frame_stats.append({'frame': ordinal, 'gop': self.gop, 'picture': rec.picture_type,
                                         'contrast_c0': C[4], 'contrast_c0_norm': Cn[4],
                                         'contrast_best_other': max(v for j, v in enumerate(C) if j != 4),
                                         'col_phase0': col_m[0], 'col_best_other': max(col_m[1:]),
                                         'row_q6': row_m[6], 'row_q7': row_m[7], 'row_best_other': max(row_m[:6])})
        # Descriptive segment observations only on correctly registered luma.
        for orient, name, plain, robust, t, coding, qp, adjacent_t, adjacent_c, adjacent_q in scored_segments(y, rec, labels):
            flat_t, flat_c = t.ravel(), coding.ravel()
            data = np.empty(flat_t.size, dtype=ENTRY_DTYPE)
            data['o'] = 1 if orient == 'V' else 2
            data['p'] = PICTURE_CODES[rec.picture_type]
            data['q'] = qp.ravel()
            data['frame'] = ordinal
            data['gop'] = self.gop
            data['plain'] = plain.ravel()
            data['robust'] = robust.ravel()
            data['t'], data['coding'] = flat_t, flat_c
            data['nt'] = -1 if adjacent_t is None else adjacent_t.ravel()
            data['nc'] = -1 if adjacent_c is None else adjacent_c.ravel()
            data['nq'] = -1 if adjacent_q is None else adjacent_q.ravel()
            if name.startswith('CONTROL'):
                data['cat'] = 0
            elif name == 'OUTER':
                data['cat'] = 8
            else:
                data['cat'] = np.where(flat_t == 1, 1,
                                np.where(flat_t == 2, 2 if orient == 'V' else 3,
                                np.where((flat_c == 1) & (rec.picture_type == 'P'), 4,
                                np.where((flat_c == 1) & (rec.picture_type == 'B'), 5,
                                np.where(flat_c == 3, 6, 7)))))
            self.entries.append(data)
            categories, counts = np.unique(data['cat'], return_counts=True)
            for cat, n in zip(categories, counts):
                self.seam_counts[(orient, CATEGORIES[int(cat)], rec.picture_type)] += int(n)
        self.processed += 1

    def finalise(self):
        if not self.processed:
            raise ValueError('no eligible frames processed')
        out = self.outdir
        reports = []
        for offset, data in self.offset_data.items():
            counts = data['frame_counts']
            fieldcounts = data['field_counts']
            ff = np.divide(data['frame_sums'], counts, out=np.full(9, np.nan), where=counts > 0)
            bb = np.divide(data['field_sums'], fieldcounts, out=np.full(9, np.nan), where=fieldcounts > 0)
            fn = np.divide(data['norm_frame_sums'], counts, out=np.full(9, np.nan), where=counts > 0)
            bn = np.divide(data['norm_field_sums'], fieldcounts, out=np.full(9, np.nan), where=fieldcounts > 0)
            c, cn = ff - bb, fn - bn
            cf = data['shift_wins'] / data['shift_eligible'] if data['shift_eligible'] else 0
            rf = data['row_wins'] / data['row_eligible'] if data['row_eligible'] else 0
            xf = data['col_wins'] / data['col_eligible'] if data['col_eligible'] else 0
            assessment = gates(c, cf, data['col_sums'], data['col_counts'], data['row_sums'], data['row_counts'], xf, rf)
            reports.append({'cx': offset[0], 'ry': offset[1], **assessment,
                            'c_norm': cn.tolist(), 'c_counts': counts.tolist(), 'field_counts': fieldcounts.tolist(),
                            'col_counts': data['col_counts'].tolist(), 'row_counts': data['row_counts'].tolist(),
                            'row_frame_n': data['row_eligible'], 'shift_frame_n': data['shift_eligible']})
        aligned = reports[0]
        offsets_pass = all(any(v != 'PASS' for v in (r['shift'], r['column'], r['row'])) for r in reports[1:])
        structural_pass = self.processed == self.index.frame_count - len(self.index.leading_b_ordinals)
        gate = ('PASS' if aligned['shift'] == aligned['column'] == aligned['row'] == 'PASS'
                and offsets_pass and structural_pass else 'BLOCKED')
        write_csv(out / 'shifted_label_contrast.csv',
                  ({'cx': r['cx'], 'ry': r['ry'], 'dx': dx, 'dy': dy,
                    'contrast': r['c'][i],
                    'contrast_norm': r['c_norm'][i], 'frame_fraction': r['shift_frame_fraction'],
                    'count_frame_MBs': r['c_counts'][i], 'count_field_MBs': r['field_counts'][i], 'gate': r['shift']} for r in reports for i, (dx, dy) in enumerate(SHIFTS)),
                  ['cx', 'ry', 'dx', 'dy', 'contrast', 'contrast_norm', 'frame_fraction', 'count_frame_MBs', 'count_field_MBs', 'gate'])
        for which in ('column', 'row'):
            write_csv(out / f'{which}_phase.csv',
                      ({'cx': r['cx'], 'ry': r['ry'], 'phase': i, 'mean': r[f'{which}_means'][i],
                        'n': r[f'{"col" if which=="column" else "row"}_counts'][i],
                        'margin': r[f'{which}_margin'], 'frame_fraction': r[f'{which}_frame_fraction'], 'gate': r[which]}
                       for r in reports for i in range(8)),
                      ['cx', 'ry', 'phase', 'mean', 'n', 'margin', 'frame_fraction', 'gate'])
        write_csv(out / 'known_bad_offsets.csv',
                  ({'cx': r['cx'], 'ry': r['ry'], 'shift': r['shift'], 'column': r['column'],
                    'row': r['row'], 'caught': r['cx'] == r['ry'] == 0 or
                    any(r[k] != 'PASS' for k in ('shift', 'column', 'row'))} for r in reports),
                  ['cx', 'ry', 'shift', 'column', 'row', 'caught'])
        write_csv(out / 'seam_counts.csv',
                  ({'orientation': o, 'class': c, 'picture': p, 'segments': n}
                   for (o, c, p), n in sorted(self.seam_counts.items())),
                  ['orientation', 'class', 'picture', 'segments'])
        self._detectability_reports()
        write_csv(out / 'frame_gop_uncertainty.csv', self.frame_stats,
                  ['frame', 'gop', 'picture', 'contrast_c0', 'contrast_c0_norm', 'contrast_best_other',
                   'col_phase0', 'col_best_other', 'row_q6', 'row_q7', 'row_best_other'])
        from stage2_index_reader_v0_2 import __file__ as frozen_reader_file
        manifest = {'label': self.kind, 'source': self.src, 'source_sha256': sha256(self.src),
                    'index': str(self.index.path), 'index_sha256': sha256(self.index.path),
                    'decoded_with': self.decoder_id, 'runtime_identity': self.runtime_info,
                    'statistics_engine_sha256': sha256(Path(__file__).resolve()),
                    'frozen_reader_sha256': sha256(Path(frozen_reader_file).resolve()),
                    'frame_count': self.index.frame_count,
                    'quality_excluded': list(self.index.leading_b_ordinals), 'eligible_frames': self.processed,
                    'offset_convention': 'pixels moved right/down by k; index unchanged; Y_shift(x,y)=Y_original(x-cx,y-ry)',
                    'frame_interior_border_px': BORDER, 'thresholds': {'shift_margin': OTHER_MARGIN,
                    'shift_frames': FRAME_FRACTION, 'column_margin': OTHER_MARGIN,
                    'row_margin': ROW_MARGIN, 'row_frames': FRAME_FRACTION},
                    'sample_pair_contract': {
                      'horizontal_frame_mid': {'cross': [[6,8],[7,9]],
                        'comparators': [[4,6],[5,7],[8,10],[9,11]]},
                      'horizontal_outer': {'cross': [[-2,0],[-1,1]],
                        'comparators': [[-4,-2],[-3,-1],[0,2],[1,3]],
                        'reference': 'b is top row of lower macroblock'},
                      'horizontal_control_4': {'cross': [[2,4],[3,5]],
                        'comparators': [[0,2],[1,3],[4,6],[5,7]]},
                      'horizontal_control_12': {'cross': [[10,12],[11,13]],
                        'comparators': [[8,10],[9,11],[12,14],[13,15]]},
                      'horizontal_signed_step': 'lower minus upper; never cross field',
                      'horizontal_robust': 'two field parities x two 8-column chunks, equal mean of 4 ratios; per-group abs(mean signed cross - mean signed comparators)/(mean abs comparators+1)',
                      'vertical_relative_to_right_column': {'cross':[[-1,0]],
                        'comparators':[[-3,-2],[1,2]]},
                      'vertical_signed_step': 'right minus left',
                      'vertical_robust': 'two 8-row parity groups, equal mean of 2 ratios'},
                    'descriptive_proxy_false_alarm_target': 0.05,
                    'declared_qp_bands': [dict(name=n, min=lo, max=hi) for n, lo, hi in QP_BANDS],
                    'gate': gate, 'aligned': aligned, 'known_bad_all_caught': offsets_pass,
                    'structural_frame_count_pass': structural_pass}
        (out / 'run_manifest.json').write_text(json.dumps(clean_json(manifest), indent=2, allow_nan=False, default=str) + '\n', encoding='utf-8')
        (out / f'S2_I2_{self.kind}_result.txt').write_text(
            'S2-I2 registration gate: ' + gate + '\n' +
            '3x3=' + aligned['shift'] + '; column=' + aligned['column'] + '; row=' + aligned['row'] + '\n' +
            'seven known-bad controls caught=' + str(offsets_pass) + '\n' +
            'Descriptive seam/control strength is NOT a registration gate or visible-artifact ground truth.\n', encoding='utf-8')
        return {'gate': gate, 'aligned': aligned, 'known_bad_all_caught': offsets_pass,
                'processed': self.processed}

    def _detectability_reports(self):
        entries = np.concatenate(self.entries)
        output_rows = []
        outer = defaultdict(list)
        for orient, oc in (('V', 1), ('H', 2)):
            pool = entries[entries['o'] == oc]
            controls = pool[pool['cat'] == 0]
            for metric in ('plain', 'robust'):
                ctrl = controls[metric].astype(np.float64)
                sorted_ctrl = np.sort(ctrl)
                threshold = percentile95_nearest(sorted_ctrl)
                fa = float(np.mean(ctrl > threshold)) if ctrl.size else float('nan')
                # Each stratum uses the SAME clip/orientation/metric threshold and control set.
                for cat in np.unique(pool['cat']):
                    group = pool[pool['cat'] == cat]
                    for pict in (0, *np.unique(group['p']).tolist()):
                        picture_group = group if pict == 0 else group[group['p'] == pict]
                        for qname, qlo, qhi in [('ALL', -1, 127), *QP_BANDS]:
                            selected = picture_group[(picture_group['q'] >= qlo) & (picture_group['q'] <= qhi)]
                            if not len(selected):
                                continue
                            scores = selected[metric].astype(np.float64)
                            is_seam = int(cat) in (1, 2, 8)
                            auc = auc_vs_sorted(scores, sorted_ctrl) if is_seam else float('nan')
                            hit = float(np.mean(scores > threshold))
                            # Frame/GOP dispersion is cluster-level descriptive uncertainty.
                            frame_rates = []
                            gop_rates = []
                            for _, sub in groups_by(selected, 'frame'):
                                frame_rates.append(float(np.mean(sub[metric] > threshold)))
                            for _, sub in groups_by(selected, 'gop'):
                                gop_rates.append(float(np.mean(sub[metric] > threshold)))
                            output_rows.append({'orientation': orient, 'metric': metric,
                              'class': CATEGORIES[int(cat)], 'picture': 'ALL' if pict == 0 else PICTURE_NAMES[pict],
                              'qp_band': qname,
                              'threshold': threshold, 'achieved_control_fa': fa,
                              'n_segments': len(scores), 'n_standard_controls': ctrl.size,
                              'hit_above_threshold': hit, 'auc_proxy': auc,
                              'score_mean': float(scores.mean()), 'score_median': float(np.median(scores)),
                              'n_frames': len(frame_rates), 'frame_hit_q1': quantile(frame_rates, .25),
                              'frame_hit_median': quantile(frame_rates, .50),
                              'frame_hit_q3': quantile(frame_rates, .75),
                              'n_gops': len(gop_rates), 'gop_hit_q1': quantile(gop_rates, .25),
                              'gop_hit_median': quantile(gop_rates, .50),
                              'gop_hit_q3': quantile(gop_rates, .75)})
            outer_rows = pool[pool['cat'] == 8]
            # Aggregation only; each outer boundary retains both neighbouring states.
            for key, sub in groups_by_multiple(outer_rows, ('p','t','coding','q','nt','nc','nq')):
                outer[(orient, *key)] = (len(sub), float(sub['plain'].mean()), float(sub['robust'].mean()))
        write_csv(self.outdir / 'boundary_detectability.csv', output_rows,
                  ['orientation', 'metric', 'class', 'picture', 'qp_band', 'threshold', 'achieved_control_fa',
                   'n_segments', 'n_standard_controls', 'hit_above_threshold', 'auc_proxy',
                   'score_mean', 'score_median', 'n_frames', 'frame_hit_q1', 'frame_hit_median',
                   'frame_hit_q3', 'n_gops', 'gop_hit_q1', 'gop_hit_median', 'gop_hit_q3'])
        write_csv(self.outdir / 'outer_mb_edge_diagnostics.csv',
                  ({'orientation': k[0], 'picture': PICTURE_NAMES[k[1]],
                    'right_or_lower_transform': TRANSFORM[k[2]],
                    'right_or_lower_coding': CODING[k[3]],
                    'right_or_lower_qp': k[4],
                    'left_or_upper_transform': TRANSFORM[k[5]],
                    'left_or_upper_coding': CODING[k[6]],
                    'left_or_upper_qp': k[7],
                    'right_or_lower_none_class': _none_subclass_name(k[1], k[2], k[3]),
                    'left_or_upper_none_class': _none_subclass_name(k[1], k[5], k[6]),
                    'n': v[0],
                    'mean_plain': v[1], 'mean_robust': v[2]}
                   for k, v in sorted(outer.items())),
                  ['orientation', 'picture', 'right_or_lower_transform', 'right_or_lower_coding',
                   'right_or_lower_qp', 'left_or_upper_transform', 'left_or_upper_coding',
                   'left_or_upper_qp', 'right_or_lower_none_class', 'left_or_upper_none_class',
                   'n', 'mean_plain', 'mean_robust'])
