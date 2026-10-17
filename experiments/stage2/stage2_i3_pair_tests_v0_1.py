#!/usr/bin/env python3
"""Adversarial paired-frame tests, pure numpy."""
from __future__ import annotations
import unittest
import numpy as np
from stage2_i3_pair_correspondence_v0_1 import compare_pair

class PairTests(unittest.TestCase):
    def setUp(self):
        rng=np.random.default_rng(100)
        self.o=[rng.integers(0,256,(32,32),dtype=np.uint8) for _ in range(42)]
        self.b=[np.minimum(x.astype(np.int16)+2,255).astype(np.uint8) for x in self.o]
        for x in self.o+self.b:x.setflags(write=False)
    def test_aligned_pass(self):
        r=compare_pair(42,42,(32,32),self.o.__getitem__,self.b.__getitem__)
        self.assertEqual(r['status'],'PASS')
        self.assertEqual(r['decisive_violations'],0)
        self.assertEqual(r['decisive_frames'],38)
        self.assertTrue(r['strict_zero_argmin'])
    def test_slipped_fails(self):
        shifted=self.b[1:]+self.b[:1]
        r=compare_pair(42,42,(32,32),self.o.__getitem__,shifted.__getitem__)
        self.assertEqual(r['status'],'FAIL')
        self.assertFalse(r['strict_zero_argmin'])
    def test_unequal_frames_hard_fail(self):
        r=compare_pair(42,41,(32,32),self.o.__getitem__,self.b.__getitem__)
        self.assertEqual(r['status'],'FAIL')
    def test_static_inconclusive(self):
        a=np.full((32,32),19,np.uint8);a.setflags(write=False)
        r=compare_pair(42,42,(32,32),lambda n:a,lambda n:a)
        self.assertEqual(r['status'],'FAIL') # no strict clip-mean minimum at 0
    def test_wrong_bit_depth(self):
        a=np.zeros((32,32),np.int16);a.setflags(write=False)
        with self.assertRaises(ValueError):compare_pair(42,42,(32,32),lambda n:a,lambda n:a)
if __name__=='__main__':unittest.main()
