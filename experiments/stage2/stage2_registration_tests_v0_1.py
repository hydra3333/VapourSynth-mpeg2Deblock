"""Synthetic tests of S2-I2 numerical and geometry invariants. No media required."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from stage2_registration_stats_v0_1 import (
    auc_rank, percentile95_nearest, gates, phase_stats, displaced,
    _score_vertical, _score_horizontal, rank_top, OFFSETS, SHIFTS, BORDER,
)


def test(name, result):
    if not result:
        raise AssertionError(name)
    print('PASS ' + name)


def main():
    test('seven defined offsets', len(OFFSETS) == 8 and (0, 0) in OFFSETS and len(set(OFFSETS)) == 8)
    test('nine shifted-label hypotheses', len(SHIFTS) == 9 and SHIFTS.index((0,0)) == 4)
    n = np.array([1, 1, 1, 3, 3, 5], float)
    test('95th empirical percentile, strict >', percentile95_nearest(n) == 5)
    test('tie-aware AUC', auc_rank([1, 2], [1, 2]) == 0.5)
    test('perfect AUC', auc_rank([3, 4], [1, 2]) == 1)
    y = np.arange(64*64, dtype=np.int16).reshape(64,64)
    moved = displaced(y, 4, 2)
    test('positive x,y moves pixels right/down', moved[20, 23] == y[18, 19])
    test('outside fixed interior unaffected by padding', moved[16,16] == y[14,12])
    yc = np.zeros((64,64), dtype=np.int16)
    # All rows have a 32-count discontinuity at column phase 0.
    yc[:, 16:] += 32
    cs, cn, _, _ = phase_stats(yc)
    test('column phase uses right-side x coordinate', cs[0] > cs[1:].max())
    yr = np.zeros((64,64), dtype=np.int16)
    # Inject even and odd row-phase 6 and 7 impulses in the absolute same-field step.
    for x in range(64):
        yr[8::8,x] = 50
        yr[9::8,x] = 50
    _,_,rs,rn = phase_stats(yr)
    test('same-field row-phase peaks at q6 q7', set(np.argsort(rs / rn)[-2:]) == {6,7})
    # The row verdict deliberately FAILs when any outside phase breaks the top two,
    # even if a deliberately selected other threshold would make it pass.
    colsum, coln = np.array([200., 10, 10, 10, 10, 10, 10, 10]), np.ones(8)
    rowsum, rown = np.array([95.,0,0,0,0,0,105,106]),np.ones(8)
    cs9 = np.array([.2,.3,.2,.3,1,.3,.2,.3,.2])
    g = gates(cs9, .8, colsum, coln, rowsum, rown, .8, .8)
    test('all three registered gates PASS', (g['shift'],g['column'],g['row']) == ('PASS',)*3)
    col_tie = np.array([100.,110.,110.,0.,0.,0.,0.,0.])
    test('column tie returns INCONCLUSIVE, not FAIL',
         gates(cs9,.8,col_tie,coln,rowsum,rown,.8,.8)['column']=='INCONCLUSIVE')
    rowsum[0] = 107
    test('outside row-phase aggregate top two FAIL', gates(cs9,.8,colsum,coln,rowsum,rown,.8,.8)['row']=='FAIL')
    # Signed robust sampling: single discontinuity; compare against exact pixel math.
    b = np.zeros((1,1,16,16), dtype=np.int16)
    b[..., :,8:] = 20
    vplain, vrob = _score_vertical(b, 8)
    test('vertical robust perfect flat step', vplain[0,0] == 20 and vrob[0,0] == 20)
    b = np.zeros((1,1,16,16), dtype=np.int16)
    b[..., 8:,:] = 20
    hplain, hrob = _score_horizontal(b, 'mid')
    test('horizontal parity-safe robust perfect flat step', hplain[0,0] == 20 and hrob[0,0] == 20)
    test('row margin and column margin distinct', BORDER == 16)
    print('PASS S2-I2 all synthetic checks')


if __name__ == '__main__':
    main()
