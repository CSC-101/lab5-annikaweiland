import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add(self):
        time1 =data.Time(60, 76, 80)
        time2 = data.Time(4, 5, 60)
        result = lab5.time_add(time1, time2)
        expected = data.Time(65, 23,  20)
        self.assertEqual(expected, result)

    def test_time_add_2(self):
        time1 =data.Time(1, 30, 35)
        time2 = data.Time(4, 30, 35)
        result = lab5.time_add(time1, time2)
        expected = data.Time(6, 1,  10)
        self.assertEqual(expected, result)
    # Part 4
    def test_is_descending(self):
        input = [5, 3, 7, 3, 7, 9]
        expected = False
        result = lab5.is_descending(input)
        self.assertEqual(expected, result)

    def test_is_descending_2(self):
        input = [55, 7, 5, 2, 1, 0]
        expected = True
        result = lab5.is_descending(input)
        self.assertEqual(expected, result)

    # Part 5
    def test_largest_between(self):
        list = [3, 6, 4, 2, 6, 9, 30]
        result = lab5.largest_between(list, 2, 6)
        expected = 30
        self.assertEqual(expected, result)

    def test_largest_between_2(self):
        list = [3, 6, 5, 2, 0, 6, 53]
        result = lab5.largest_between(list, 2, 10)
        expected = None
        self.assertEqual(expected, result)

    # Part 6
    def test_furthest_from_origin(self):
        point1 = data.Point(3, 5)
        point2 = data.Point(10, 10)
        point3 = data.Point(100, 100)
        expected = 2
        result = lab5.furthest_from_origin([point1, point2, point3])
        self.assertEqual(expected, result)

    def test_furthest_from_origin_2(self):
        expected = None
        result = lab5.furthest_from_origin([])
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
