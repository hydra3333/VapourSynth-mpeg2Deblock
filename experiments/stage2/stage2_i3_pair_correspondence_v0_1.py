#!/usr/bin/env python3
"""S2-I3 P0 pair temporal proof (pure NumPy). No filtering or saved media."""
from __future__ import annotations
import numpy as np

OFFSETS = (-2, -1, 0, 1, 2)


def _frame(x, shape):
    if not isinstance(x, np.ndarray) or x.dtype != np.dtype('uint8') or x.shape != shape:
        raise ValueError('pair expects matching native YUV420P8 luma shapes')
    if x.flags.writeable:
        raise ValueError('pair luma input must be read-only')
    return x


def _mae(a, b):
    # uint8 -> signed integer BEFORE subtraction to avoid wrapping at 255.
    return float(np.mean(np.abs(a.astype(np.int16) - b.astype(np.int16)), dtype=np.float64))


def compare_pair(original_count, blocky_count, shape, get_original, get_blocky):
    if original_count != blocky_count:
        return {'schema':'S2-I3-P0-PAIR-1','status':'FAIL',
                'reason':'original/blocky frame count mismatch',
                'original_frames':original_count,'blocky_frames':blocky_count}
    if original_count < 5:
        return {'schema':'S2-I3-P0-PAIR-1','status':'INCONCLUSIVE',
                'reason':'fewer than five frames for +/-2 comparisons',
                'original_frames':original_count,'blocky_frames':blocky_count}
    sums = {k:0.0 for k in OFFSETS}
    decisive = violations = 0
    frames = []
    # SAME N=2..num_frames-3 in every offset for a fair strict argmin.
    for n in range(2, original_count - 2):
        b = _frame(get_blocky(n), shape)
        o = _frame(get_original(n), shape)
        dist = {k:_mae(b, _frame(get_original(n+k), shape)) for k in OFFSETS}
        oo = min(_mae(o, _frame(get_original(n+k), shape)) for k in OFFSETS if k != 0)
        is_decisive = oo >= 2.0 * dist[0]
        violation = bool(is_decisive and any(dist[k] < dist[0] for k in OFFSETS if k != 0))
        decisive += int(is_decisive)
        violations += int(violation)
        for k in OFFSETS:
            sums[k] += dist[k]
        frames.append({'frame':n,'mae_at_0':dist[0],
                       'min_original_neighbour_mae':oo,
                       'decisive':is_decisive,'violation':violation})
    tested = len(frames)
    means = {str(k):sums[k]/tested for k in OFFSETS}
    best_other = min(means[str(k)] for k in OFFSETS if k != 0)
    strict_argmin = means['0'] < best_other
    if not strict_argmin or violations:
        verdict, reason = 'FAIL', 'k=0 not strict clip-mean minimum or decisive-frame violation'
    elif decisive < 20 or 10 * decisive < original_count:
        verdict, reason = 'INCONCLUSIVE', 'insufficient decisive frames (>=20 and >=10% required)'
    else:
        verdict, reason = 'PASS', 'unique mean minimum at k=0 and sufficient decisive frames'
    return {'schema':'S2-I3-P0-PAIR-1','status':verdict,'reason':reason,
            'original_frames':original_count,'blocky_frames':blocky_count,
            'common_interior_frames':tested,
            'mean_mae_by_display_offset':means,'strict_zero_argmin':strict_argmin,
            'best_other_mean_mae':best_other,
            'decisive_frames':decisive,'decisive_fraction_of_all_frames':decisive/original_count,
            'decisive_violations':violations, 'frame_evidence':frames,
            'definition':'decisive if min_k!=0 MAE(oN,oN+k) >= 2*MAE(bN,oN); k=-2..2',
            'floor_note':'20 frames and 10 percent set after preflight visibility; documented by Claude'
            }
