#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from gamemap import GameMap, Boulder
from animaux import Animal
import numpy as np

class testGameMap(unittest.TestCase):
    def testSize(self):
        m = GameMap()
        self.assertEqual(m.xmax, 5)
        self.assertEqual(m.ymax, 5)

    def testBoulderInit(self):
        m = GameMap()
        self.assertIsInstance(m[1][2],Boulder)
        self.assertIsInstance(m[2][2], Boulder)
        self.assertIsInstance(m[3][2], Boulder)

    def testNbBoulder(self):
        m = GameMap()
        self.assertEqual(m.nb_boulders,3)

    def testNbElephant(self):
        m = GameMap()
        for k in range (5) :
            m.add(Animal(0,k, np.array([0,1]), 'Elephant'))
        self.assertEqual(m.nb_elephants, 5)
        m.add(Animal(1, 0, np.array([0,1]), 'Elephant'))
        self.assertEqual(m.nb_elephants, 5)
        self.assertEqual(m[1][0], 0)

    def testNbRhinoceros(self):
        m = GameMap()
        for k in range(5):
            m.add(Animal(0,k, np.array([0,1]), 'Rhinoceros'))
        self.assertEqual(m.nb_rhinoceros, 5)
        m.add(Animal(0,k, np.array([0,1]), 'Rhinoceros'))
        self.assertEqual(m.nb_rhinoceros, 5)
        self.assertEqual(m[1][0], 0)

    def testChangingNbElephant(self):
        m = GameMap()
        self.assertEqual(m.nb_elephants, 0)
        m.nb_elephants += 1
        self.assertEqual(m.nb_elephants, 0)

    def testChangingNbRinoceros(self):
        m = GameMap()
        self.assertEqual(m.nb_rhinoceros, 0)
        m.nb_rhinoceros += 1
        self.assertEqual(m.nb_rhinoceros, 0)

    def testAdd(self):
        m = GameMap()
        m.add(Animal(0, 2, np.array([0, 1]), 'Rhinoceros'))
        self.assertIsInstance(m[0][2], Animal)
        m.add(Animal(1, 1, np.array([0, 1]), 'Rhinoceros'))
        self.assertEqual(m[1][1], 0)

    def testDelete(self):
        m = GameMap()
        m.add(Animal(0, 2, np.array([0, 1]), 'Rhinoceros'))
        m.add(Animal(0, 1, np.array([0, 1]), 'Rhinoceros'))
        m.move(m[0][1], (1,1))
        self.assertIsInstance(m[0][2], Animal)
        self.assertIsInstance(m[1][1], Animal)
        self.assertEqual(m.nb_rhinoceros, 2)
        self.assertEqual(m.nb_rhinoceros, 2)
        m.delete(Animal(0, 2, np.array([0, 1]), 'Rhinoceros'))
        m.delete(Animal(1, 1, np.array([0, 1]), 'Rhinoceros'))
        self.assertEqual(m[0][2], 0)
        self.assertIsInstance(m[1][1], Animal)
        self.assertEqual(m.nb_rhinoceros, 1)


if __name__ == '__main__':
    unittest.main()
