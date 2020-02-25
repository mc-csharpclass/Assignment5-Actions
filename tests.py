# tests file


import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_calc_circ_area(self):
        # test the function is accurate for a radius of 1
        expected = 3.14159
        self.assertAlmostEqual(expected, task.calc_circle_area(1),5)

        # test the function is accurate for a radius of 5
        expected2 = 78.53982
        self.assertAlmostEqual(expected2, task.calc_circle_area(5),5)


if __name__ == '__main__':
    unittest.main()
