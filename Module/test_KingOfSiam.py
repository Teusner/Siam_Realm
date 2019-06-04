#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Brateaqu, Farolflu"
__copyright__ = "Copyright 2019"
__credits__ = ["Quentin BRATEAU", "Luca FAROLFI"]

__license__ = "GPL"
__version__ = "1.0"
__email__ = ["quentin.brateau@ensta-bretagne.org", "luca.farolfi@ensta-bretagne.org"]


# Importing Modules
import unittest
from KingOfSiam import GameMap, Animal, Boulder, Cross
import numpy as np


class testGameMap(unittest.TestCase):
    def setUp(self):
        self.m = GameMap()

    def testSize(self):
        self.assertEqual(self.m.xmax, 5)
        self.assertEqual(self.m.ymax, 5)

    def testBoulderInit(self):
        self.assertIsInstance(self.m[2][1], Boulder)
        self.assertIsInstance(self.m[2][2], Boulder)
        self.assertIsInstance(self.m[2][3], Boulder)

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
        self.m.move(self.m[0][1], (1, 1), np.array([0, 1]))
        self.assertIsInstance(self.m[0][2], Animal)
        self.assertIsInstance(self.m[1][1], Animal)
        self.assertEqual(self.m.nb_rhinoceros, 2)
        self.assertEqual(self.m.nb_elephants, 0)
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

    def testPositionInGameMap(self):
        c = [(-1, 0), (0, -1), (5, 0), (0, 5)]
        for coord in c:
            self.a.coords = coord
            self.assertEqual(self.a.coords, (0, 1))

    def testDirectionInGameMap(self):
        d = [np.array([0, 2]), np.array([2, 0]), np.array([-2, 0]), np.array([0, -2]), np.array([1, 1]), np.array([-1, -1]), np.array([1/2, np.sqrt(3)/2])]
        for dir in d:
            self.a.direction = dir
            self.assertEqual(self.a.direction[0], 0)
            self.assertEqual(self.a.direction[1], 1)

    def testSpecies(self):
        self.assertEqual(self.a.species, "Elephant")
        self.a.species = "Rhinoceros"
        self.assertEqual(self.a.species, "Rhinoceros")
        self.a.species = "TheCakeIsALie"
        self.assertEqual(self.a.species, "Rhinoceros")


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

    def pushBoulder(self):
        a = Animal(1, 1, np.array([1, 0]), "Elephant")
        self.m[1][1] = a
        self.m.move(a, (2, 1), np.array([1, 0]))
        self.assertIsInstance(self.g[2][1], Animal)
        self.assertIsInstance(self.g[2][2], Boulder)


if __name__ == '__main__':
    unittest.main()
    #suite = unittest.TestLoader().loadTestsFromTestCase(testGameMap)
    #unittest.TextTestRunner(verbosity=0).run(suite)