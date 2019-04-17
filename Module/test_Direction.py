#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from Direction import Direction
import numpy as np


class testDirection(unittest.TestCase):
    def setUp(self):
        self.a = Direction([0, 1])
        self.b = Direction([1, 0])
        self.c = Direction([0, -1])
        self.d = Direction([-1, 0])

    def testSetup(self):
        self.assertEqual(self.a[0], 0)
        self.assertEqual(self.a[1], 1)
        self.assertEqual(self.d[0], -1)
        self.assertEqual(self.d[1], 0)

    def testType(self):
        self.assertIsInstance(self.a, Direction)

    def testUnitary(self):
        self.assertEqual(np.linalg.norm(self.a), 1)

    def testBearing(self):
        self.assertEqual(self.a.bearing(self.a), 1)
        self.assertEqual(self.a.bearing(self.b), 0)
        self.assertEqual(self.a.bearing(self.c), -1)

    def testScalar(self):
        self.assertEqual(self.a.scalar([self.b, self.c, self.d]), (-1, True))
        self.assertEqual(self.a.scalar([self.a, self.b, self.a, self.c]), (1, False))

if __name__ == '__main__':
    unittest.main()