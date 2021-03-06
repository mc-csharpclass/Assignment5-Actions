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
        self.assertAlmostEqual(expected, task.calc_circle_area(1), 5)

        # test the function is accurate for a radius of 5
        expected2 = 78.53982
        self.assertAlmostEqual(expected2, task.calc_circle_area(5), 5)

    """def test_get_first_and_last(self):
        # test that we get the correct items in a 3 item list
        testList = ['first', 'second', 'third']
        self.assertEqual(testList[0], task.get_first_and_last(testList)[0])
        self.assertEqual(testList[2], task.get_first_and_last(testList)[1])

    def test_days_between(self):
        # test that the function returns the correct differnce in days
        # start = datetime.datetime(2020,1,1)
        # end = datetime.datetime(2020,1,2)
        start = [2020, 1, 1]
        end = [2020, 1, 2]
        self.assertEqual(1, task.days_between(start, end))
        # test with differnt year
        start2 = [2020, 1, 1]
        end2 = [2021, 1, 1]
        self.assertEqual(366, task.days_between(start2, end2))"""


if __name__ == '__main__':
    unittest.main()
