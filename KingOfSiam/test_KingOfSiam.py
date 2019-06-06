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
from GameMap import GameMap
from GamePieces import Animal, Boulder, Cross
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


class testRegle(unittest.TestCase):
    def setUp(self):
        self.g = GameMap()

    def testPushBoulder(self):
        a = Animal(1, 1, np.array([1, 0]), "Elephant")
        self.g[1][1] = a
        self.g.move(a, (2, 1), np.array([1, 0]))
        self.assertIsInstance(self.g[2][1], Animal)
        self.assertIsInstance(self.g[2][2], Boulder)

    def testPushAnimalNeutral(self):
        e = Animal(1, 1, np.array([1, 0]), "Elephant")
        r = Animal(1, 2, np.array([0, -1]), "Rhinoceros")
        self.g[1][1] = e
        self.g[1][2] = r
        self.g.move(r, (1, 1), np.array([1, 0])) # Changing the direction during a push do not have any effect if the bearing was good before the push

        # Test for the Elephant
        self.assertIsInstance(self.g[1][0], Animal)
        self.assertEqual(self.g[1][0].species, 'Elephant')
        self.assertEqual(self.g[1][0].coords[0], 1)
        self.assertEqual(self.g[1][0].coords[1], 0)
        self.assertEqual(self.g[1][0].direction[0], 1)
        self.assertEqual(self.g[1][0].direction[1], 0)

        # Test for the Rhinoceros
        self.assertIsInstance(self.g[1][1], Animal)
        self.assertEqual(self.g[1][1].species, 'Rhinoceros')
        self.assertEqual(self.g[1][1].coords[0], 1)
        self.assertEqual(self.g[1][1].coords[1], 1)
        self.assertEqual(self.g[1][1].direction[0], 0)
        self.assertEqual(self.g[1][1].direction[1], -1)

    def testPushAnimalOpponent(self):
        e = Animal(1, 1, np.array([0, 1]), "Elephant")
        r = Animal(1, 2, np.array([0, -1]), "Rhinoceros")
        self.g[1][1] = e
        self.g[1][2] = r
        self.g.move(e, (1, 2), np.array([1, 0])) # Changing the direction during a push do not have any effect if the bearing was good before the push

        # Test for the Elephant
        self.assertIsInstance(self.g[1][1], Animal)
        self.assertEqual(self.g[1][1].species, 'Elephant')
        self.assertEqual(self.g[1][1].coords[0], 1)
        self.assertEqual(self.g[1][1].coords[1], 1)
        self.assertEqual(self.g[1][1].direction[0], 0)
        self.assertEqual(self.g[1][1].direction[1], 1)

        # Test for the Rhinoceros
        self.assertIsInstance(self.g[1][2], Animal)
        self.assertEqual(self.g[1][2].species, 'Rhinoceros')
        self.assertEqual(self.g[1][2].coords[0], 1)
        self.assertEqual(self.g[1][2].coords[1], 2)
        self.assertEqual(self.g[1][2].direction[0], 0)
        self.assertEqual(self.g[1][2].direction[1], -1)

    def testPushHeavy(self):
        e = Animal(2, 0, np.array([0, 1]), "Elephant")
        self.g[2][0] = e
        print(self.g)
        self.g.move(e, (2, 1), np.array([1, 0])) # Changing the direction during a push do not have any effect if the bearing was good before the push
        print(self.g)
        # Test for the Elephant
        self.assertIsInstance(self.g[2][0], Animal)
        self.assertEqual(self.g[2][0].species, 'Elephant')
        self.assertEqual(self.g[2][0].coords[0], 2)
        self.assertEqual(self.g[2][0].coords[1], 0)
        self.assertEqual(self.g[2][0].direction[0], 0)
        self.assertEqual(self.g[2][0].direction[1], 1)

        # Test for the Boulder
        self.assertIsInstance(self.g[2][1], Boulder)
        self.assertEqual(self.g[2][1].coords[0], 2)
        self.assertEqual(self.g[2][1].coords[1], 1)


if __name__ == '__main__':
    unittest.main()
