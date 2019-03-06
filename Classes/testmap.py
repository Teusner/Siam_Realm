#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import map
from animaux import *


class testmap(unittest):
    def testSize(self):
        m = map()
        self.assertEqual(m.xmax, 4)
        self.assertEqual(m.ymax, 4)

    def testNbBoulder(self):
        m = map()
        self.assertEqual(m.nb_boulder,3)

    def testNbElephant(self):
        m = map()
        for k in range (5) :
            m.add(Elephant(0,k))
        self.assertEqual(m.nb_elephant, 5)
        m.add(Elephant(1,0))
        self.assertEqual(m.nb_elephant, 5)

    def testNbRhinoceros(self):
        m = map()
        for k in range(5):
            m.add(Rhinoceros(0, k))
        self.assertEqual(m.nb_rhinoceros, 5)
        m.add(Rhinoceros(1, 0))
        self.assertEqual(m.nb_rhinoceros, 5)


if __name__ == '__main__':
    unittest . main ()
