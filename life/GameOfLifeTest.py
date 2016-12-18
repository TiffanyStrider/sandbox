import GameOfLife
import unittest

class FindNeighborsTestCase(unittest.TestCase):
    def test_middle(self):
        pair = (3, 7)
        expected = {(2, 6), (2, 7), (2, 8), (3, 6), (3, 8), (4, 6), (4, 7), (4, 8)}
        actual = GameOfLife.find_neighbors(pair)
        self.assertEqual(actual, expected)
        
    def test_corner(self):
        pair = (0, 0)
        expected = {(1, 0), (0, 1), (1, 1)}
        actual = GameOfLife.find_neighbors(pair)
        self.assertEqual(actual, expected)

unittest.main()

