import unittest
import map

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

        self.assertEqual(M.nb_elephant, 3)
    def testNbRhinoceros(self):
if __name__ == '__main__':
    unittest . main ()
