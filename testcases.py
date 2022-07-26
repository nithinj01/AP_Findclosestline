import unittest
import findnearestlinewithdirection

class Testlinesegment(unittest.TestCase):
    def test_closest_line(self):
        actual = findnearestlinewithdirection.findlinesegment(0, [((9, -1), (1, 1)), ((2, -1), (2, 1))])
        expected = ((2, -1), (2, 1))
        self.assertEqual(actual, expected)
        actual1 = findnearestlinewithdirection.findlinesegment(0, [((1, -1), (1, 1)), ((2, -1), (2, 1))])
        expected1 = ((1, -1), (1, 1))
        self.assertEqual(actual1, expected1)