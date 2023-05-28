import unittest
from lab1.solution import Solution


class _TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.SUT = Solution.insert


class TestSolution(_TestSuite):
    def test_solution_with_lists_of_int(self):
        """
        Example 1:

        Input: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]
        Output: [[1, 2], [3, 10], [12, 16]]
        """
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        expected = [[1, 2], [3, 10], [12, 16]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))

    def test_solution_with_new_interval_more_borders(self):
        """
        Example 2:

        Input: intervals = [[1, 2], [4, 5], [7, 10]], newInterval = [0, 11]
        Output: [[0, 11]]
        """
        intervals = [[1, 2], [4, 5], [7, 10]]
        newInterval = [0, 11]
        expected = [[0, 11]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))

    def test_solution_with_new_interval_included_in_intervals(self):
        """
        Example 3:

        Input: intervals = [[1, 5], [8, 10]], newInterval = [2, 4]
        Output: [[1, 5], [8, 10]]
        """
        intervals = [[1, 5], [8, 10]]
        newInterval = [2, 4]
        expected = [[1, 5], [8, 10]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))


class TestListLengthValidation(_TestSuite):
    """
    Constraints:

    0 <= intervals.length <= 10**4
    newInterval.length == 2
    """

    def test_intervals_length_equals_0(self):
        intervals = []
        newInterval = [2, 4]
        expected = [[2, 4]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))

    def test_intervals_length_greater_than_1(self):
        intervals = [[5, 7]]
        newInterval = [2, 4]
        expected = [[2, 4], [5, 7]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))

    def test_intervals_length_equals_10000(self):
        intervals = [[1, 2]] * 10000
        newInterval = [2, 4]
        expected = [[1, 4]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))

    def test_intervals_length_less_than_10000(self):
        intervals = [[1, 2]] * 9999
        newInterval = [2, 4]
        expected = [[1, 4]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))

    def test_intervals_length_greater_than_10000(self):
        intervals = [[1, 2]] * 10001
        newInterval = [2, 4]

        with self.assertRaises(IndexError):
            self.SUT(self, intervals, newInterval)

    def test_new_interval_length_equals_2(self):
        intervals = [[1, 5]]
        newInterval = [0, 4]
        expected = [[0, 5]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))

    def test_new_interval_length_less_then_2(self):
        intervals = [[1, 5]]
        newInterval = [0]

        with self.assertRaises(IndexError):
            self.SUT(self, intervals, newInterval)

    def test_new_interval_length_more_then_2(self):
        intervals = [[1, 5]]
        newInterval = [0, 2, 5]

        with self.assertRaises(IndexError):
            self.SUT(self, intervals, newInterval)


class TestListElementLengthValidation(_TestSuite):
    """
    Constraints:

    intervals[i].length == 2
    0 <= starti <= endi <= 10**5
    0 <= start <= end <= 10**5
    """

    def test_intervals_element_length_equals_2(self):
        intervals = [[5, 5]]
        newInterval = [2, 4]
        expected = [[2, 4], [5, 5]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))

    def test_intervals_element_length_greater_than_2(self):
        intervals = [[1, 7, 9]]
        newInterval = [2, 4]

        with self.assertRaises(IndexError):
            self.SUT(self, intervals, newInterval)

    def test_intervals_element_length_less_than_2(self):
        intervals = [[1]]
        newInterval = [2, 4]

        with self.assertRaises(IndexError):
            self.SUT(self, intervals, newInterval)

    def test_intervals_element_start_or_end_equals_0(self):
        intervals = [[0, 1]]
        newInterval = [2, 4]
        expected = [[0, 1], [2, 4]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))

    def test_intervals_element_start_or_end_greater_then_0(self):
        intervals = [[1, 2]]
        newInterval = [2, 4]
        expected = [[1, 4]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))

    def test_intervals_element_start_or_end_less_then_0(self):
        intervals = [[-1, 2]]
        newInterval = [2, 4]

        with self.assertRaises(ValueError):
            self.SUT(self, intervals, newInterval)

    def test_intervals_element_start_or_end_equals_100000(self):
        intervals = [[100000, 100000]]
        newInterval = [2, 4]
        expected = [[2, 4], [100000, 100000]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))

    def test_intervals_element_start_or_end_greater_then_100000(self):
        intervals = [[100001, 100001]]
        newInterval = [2, 4]

        with self.assertRaises(ValueError):
            self.SUT(self, intervals, newInterval)

    def test_new_interval_element_start_or_end_equals_0(self):
        intervals = [[0, 1]]
        newInterval = [0, 4]
        expected = [[0, 4]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))

    def test_new_interval_element_start_or_end_greater_then_0(self):
        intervals = [[1, 2]]
        newInterval = [2, 4]
        expected = [[1, 4]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))

    def test_new_interval_element_start_or_end_less_then_0(self):
        intervals = [[1, 2]]
        newInterval = [-2, 4]

        with self.assertRaises(ValueError):
            self.SUT(self, intervals, newInterval)

    def test_new_interval_element_start_or_end_equals_100000(self):
        intervals = [[2, 4]]
        newInterval = [100000, 100000]
        expected = [[2, 4], [100000, 100000]]

        self.assertEqual(expected, self.SUT(self, intervals, newInterval))

    def test_new_intervals_element_start_or_end_greater_then_100000(self):
        intervals = [[2, 4]]
        newInterval = [100001, 100001]

        with self.assertRaises(ValueError):
            self.SUT(self, intervals, newInterval)


class TestVariableTypes(_TestSuite):

    def test_empty_lists(self):
        intervals = [[]]
        newInterval = []

        with self.assertRaises(ValueError):
            self.SUT(self, intervals, newInterval)

