#!/usr/bin/env python3
"""Pure S2-I3 P0 adversarial unit tests. No VapourSynth/media required."""
from __future__ import annotations
import unittest
from types import SimpleNamespace as O
import numpy as np
from stage2_i3_pskip_core_v0_1 import (
    run_pskip, inspect_record_order, AdmissionStructureError, OFFSETS,
)

W=128
H=128
class Rec:
    def __init__(self, n, typ, codings=None, ord_override=None):
        self.output_ordinal=n if ord_override is None else ord_override
        self.picture_type=typ
        self.picture_structure=3
        self.chroma_format=1
        self.coded_width=W
        self.coded_height=H
        self.mb_width=W//16
        self.mb_height=H//16
        self.codings=codings or []
    def iter_macroblocks(self):
        return iter(O(coding=c) for c in self.codings)

class CoreTests(unittest.TestCase):
    def setUp(self):
        self.rng=np.random.default_rng(42)
    def frames(self, data):
        result=[]
        for x in data:
            a=np.array(x,copy=True,dtype=np.uint8)
            a.setflags(write=False)
            result.append(a)
        return result
    def idx(self, recs):
        return O(records=tuple(recs),width=W,height=H,frame_count=len(recs))
    def test_offsets(self):
        self.assertEqual(len(OFFSETS),24)
        self.assertEqual(len(set(OFFSETS)),24)
        for ofs in ((4,0),(8,0),(16,0),(0,1),(0,2),(0,8),(0,16)):
            self.assertIn(ofs,OFFSETS)
    def test_last_anchor_across_bs_and_true_exact(self):
        i=self.idx([Rec(0,'I'), Rec(1,'B'), Rec(2,'B'),Rec(3,'P',[1]*64),Rec(4,'B'),Rec(5,'P',[1]*64)])
        frames=self.frames([self.rng.integers(0,256,(H,W),dtype=np.uint8) for _ in range(6)])
        frames[3]=frames[0]
        frames[5]=frames[3]
        a=inspect_record_order(i)
        self.assertEqual(a,[None,0,0,0,3,3])
        r=run_pskip(i,frames.__getitem__)
        self.assertEqual(r['true_position'],{'compared':128,'identical':128})
        self.assertEqual(r['per_P_picture'][0]['anchor'],0)
        self.assertEqual(r['per_P_picture'][1]['anchor'],3)
        self.assertEqual(r['status'],'INCONCLUSIVE') # 2 P pictures < 10
    def test_true_position_mismatch_precedes_inconclusive(self):
        i=self.idx([Rec(0,'I'),Rec(1,'P',[1]*64)])
        a=np.full((H,W),28,np.uint8)
        b=a.copy();b[0,0]=29
        fr=self.frames([a,b])
        r=run_pskip(i,fr.__getitem__)
        self.assertEqual(r['status'],'FAIL')
        self.assertEqual(r['true_position']['identical'],63)
    def test_static_negative_control_inconclusive_not_fail(self):
        i=self.idx([Rec(0,'I')]+[Rec(n,'P',[1]*64) for n in range(1,12)])
        frames=self.frames([np.full((H,W),77,np.uint8) for _ in range(12)])
        r=run_pskip(i,frames.__getitem__)
        self.assertEqual(r['true_position']['compared'],11*64)
        self.assertEqual(r['status'],'INCONCLUSIVE')
        self.assertIn('nondiscriminating',r['reason'])
    def test_inter_cbp0_not_a_pskip(self):
        i=self.idx([Rec(0,'I'),Rec(1,'P',[3]*20+[1]*20+[3]*24)])
        f=self.frames([np.full((H,W),42,np.uint8),np.full((H,W),42,np.uint8)])
        r=run_pskip(i,f.__getitem__)
        self.assertEqual(r['true_position']['compared'],20)
    def test_p_without_anchor_excluded(self):
        i=self.idx([Rec(0,'P',[1]*64),Rec(1,'I'),Rec(2,'P',[1]*64)])
        f=self.frames([np.full((H,W),22,np.uint8)]*3)
        r=run_pskip(i,f.__getitem__)
        self.assertEqual(r['P_pictures_without_anchor_excluded'],1)
        self.assertEqual(r['true_position']['compared'],64)
    def test_display_ordinal_integrity(self):
        i=self.idx([Rec(0,'I'),Rec(1,'P',ord_override=6)])
        with self.assertRaises(AdmissionStructureError):inspect_record_order(i)
    def test_wrong_luma_dtype_rejected(self):
        i=self.idx([Rec(0,'I'),Rec(1,'P',[1]*64)])
        wrong=np.zeros((H,W),np.int16)
        wrong.setflags(write=False)
        with self.assertRaises(AdmissionStructureError):run_pskip(i,lambda n:wrong)
    def test_writable_input_rejected(self):
        i=self.idx([Rec(0,'I'),Rec(1,'P',[1]*64)])
        with self.assertRaises(AdmissionStructureError):run_pskip(i,lambda n:np.zeros((H,W),np.uint8))

if __name__=='__main__': unittest.main()
