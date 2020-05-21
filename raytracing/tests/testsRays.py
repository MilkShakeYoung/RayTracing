import unittest
import envtest  # modifies path
from raytracing import *

inf = float("+inf")


class TestRays(unittest.TestCase):

    def testRaysInitDifferentInputs(self):
        listOfRays = [Ray(), Ray(1, 1), Ray(1, -2), Ray(0, -1)]
        tupleOfRays = tuple(listOfRays)
        npArrayOfRays = array(listOfRays)
        raysFromList = Rays(listOfRays)
        raysFromTuple = Rays(tupleOfRays)
        raysFromArray = Rays(npArrayOfRays)
        self.assertListEqual(raysFromList.rays, listOfRays)
        self.assertTupleEqual(raysFromTuple.rays, tupleOfRays)
        self.assertTrue(all(raysFromArray.rays == npArrayOfRays))

        with self.assertRaises(Exception):
            # This should raise an exception
            Rays("Ray(), Ray(1), Ray(1,1)")

    def testRayCountHist(self):
        r = Rays([Ray()])
        init = r.rayCountHistogram()
        self.assertIsNotNone(init)  # First time compute
        final = r.rayCountHistogram()
        self.assertIsNotNone(final)  # Second time compute, now works

        self.assertTupleEqual(init, final)
        final = r.rayCountHistogram(10)
        self.assertNotEqual(init, final)

    def testRayAnglesHist(self):
        r = Rays([Ray()])
        init = r.rayAnglesHistogram()
        self.assertIsNotNone(init)  # First time compute
        final = r.rayAnglesHistogram()
        self.assertIsNotNone(final)  # Second time compute, now works

        self.assertTupleEqual(init, final)
        final = r.rayAnglesHistogram(10)
        self.assertNotEqual(init, final)


if __name__ == '__main__':
    unittest.main()
