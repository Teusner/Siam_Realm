#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from Module.KingOfSiam import GameMap, Animal, Boulder, Cross
import numpy as np


class testGameMap(unittest.TestCase):
    def setUp(self):
        self.m = GameMap()

    def testSize(self):
        self.assertEqual(self.m.xmax, 5)
        self.assertEqual(self.m.ymax, 5)

    def testBoulderInit(self):
        self.assertIsInstance(self.m[1][2], Boulder)
        self.assertIsInstance(self.m[2][2], Boulder)
        self.assertIsInstance(self.m[3][2], Boulder)

    def testNbBoulders(self):
        self.assertEqual(self.m.nb_boulders, 3)

    def testNbElephants(self):
        for k in range(5):
            self.m.add(Animal(0, k, np.array([0, 1]), 'Elephant'))
        self.assertEqual(self.m.nb_elephants, 5)
        self.m.add(Animal(1, 0, np.array([0, 1]), 'Elephant'))
        self.assertEqual(self.m.nb_elephants, 5)
        self.assertEqual(self.m[1][0], 0)

    def testNbRhinoceros(self):
        for k in range(5):
            self.m.add(Animal(0, k, np.array([0, 1]), 'Rhinoceros'))
        self.assertEqual(self.m.nb_rhinoceros, 5)
        self.m.add(Animal(0, 1, np.array([0, 1]), 'Rhinoceros'))
        self.assertEqual(self.m.nb_rhinoceros, 5)
        self.assertEqual(self.m[1][0], 0)

    def testChangingNbElephant(self):
        self.assertEqual(self.m.nb_elephants, 0)
        self.m.nb_elephants += 1
        self.assertEqual(self.m.nb_elephants, 0)

    def testChangingNbRinoceros(self):
        self.assertEqual(self.m.nb_rhinoceros, 0)
        self.m.nb_rhinoceros += 1
        self.assertEqual(self.m.nb_rhinoceros, 0)

    def testAdd(self):
        self.m.add(Animal(0, 2, np.array([0, 1]), 'Rhinoceros'))
        self.assertIsInstance(self.m[0][2], Animal)
        self.m.add(Animal(1, 1, np.array([0, 1]), 'Rhinoceros'))
        self.assertEqual(self.m[1][1], 0)

    def testDelete(self):
        self.m.add(Animal(0, 2, np.array([0, 1]), 'Rhinoceros'))
        self.m.add(Animal(0, 1, np.array([0, 1]), 'Rhinoceros'))
        self.m.move(self.m[0][1], (1, 1))
        self.assertIsInstance(self.m[0][2], Animal)
        self.assertIsInstance(self.m[1][1], Animal)
        self.assertEqual(self.m.nb_rhinoceros, 2)
        self.assertEqual(self.m.nb_rhinoceros, 2)
        self.m.delete(Animal(0, 2, np.array([0, 1]), 'Rhinoceros'))
        self.m.delete(Animal(1, 1, np.array([0, 1]), 'Rhinoceros'))
        self.assertEqual(self.m[0][2], 0)
        self.assertIsInstance(self.m[1][1], Animal)
        self.assertEqual(self.m.nb_rhinoceros, 1)


class testAnimal(unittest.TestCase):
    def setUp(self):
        self.a = Animal(0, 1, np.array([0, 1]), "Elephant")

    def testType(self):
        self.assertIsInstance(self.a, Animal)
        self.assertNotIsInstance(self.a, Boulder)
        self.assertNotIsInstance(self.a, Cross)

    def testPosition(self):
        self.assertEqual(self.a.coords, (0, 1))


class testBoulder(unittest.TestCase):
    def setUp(self):
        self.b = Boulder(1, 2)

    def testType(self):
        self.assertNotIsInstance(self.b, Animal)
        self.assertIsInstance(self.b, Boulder)
        self.assertNotIsInstance(self.b, Cross)

    def testPosition(self):
        self.assertEqual(self.b.coords, (1,2))


class testCross(unittest.TestCase):
    def setUp(self):
        self.c = Cross(1, 2)

    def testType(self):
        self.assertNotIsInstance(self.c, Animal)
        self.assertNotIsInstance(self.c, Boulder)
        self.assertIsInstance(self.c, Cross)

    def testPosition(self):
        self.assertEqual(self.c.coords, (1, 2))


class testRegles(unittest.TestCase):
    def setUp(self):
        self.m = GameMap()


if __name__ == '__main__':
    unittest.main()
