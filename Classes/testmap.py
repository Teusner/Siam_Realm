import unittest
import map
import animaux


class testmap(unittest):
    def testSize(self):
        M = map()
        self.assertEqual(M.xmax, 4)
        self.assertEqual(M.ymax, 4)

    def testNbBoulder(self):
        M = map()
        self.assertEqual(M.nb_boulder,3)

    def testNbElephant(self):
        M = map()
        for k in range (5) :
            M.add(Elephant(0,k))
        self.assertEqual(M.nb_elephant, 5)
        M.add(Elephant(1,0))
        self.assertEqual(M.nb_elephant, 5)

    def testNbRhinoceros(self):
        M = map()
        for k in range(5):
            M.add(Rhinoceros(0, k))
        self.assertEqual(M.nb_rhinoceros, 5)
        M.add(Rhinoceros(1, 0))
        self.assertEqual(M.nb_rhinoceros, 5)


if __name__ == '__main__':
    unittest . main ()
