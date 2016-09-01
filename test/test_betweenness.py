import unittest

from src.Graph import *
from src.betweeeness import *


class TestBetweennessOneNode(unittest.TestCase):
    def setUp(self):
        mat = [
            [1, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 0, 0],
            [1, 0, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 1]
        ]
        self.graph = Graph(mat)
        self.directed_graph = DirectedGraph(self.graph, 0)
        self.betweenness = BetweennessOneNode(self.directed_graph)

    def test_init(self):
        test_res = self.betweenness.betweenness_mat
        wanted_res = [
            [0, Fraction(11, 6), Fraction(25, 6), 0, 0, 0, 0],
            [Fraction(11, 6), 0, 0, Fraction(5, 6), 0, 0, 0],
            [Fraction(25, 6), 0, 0, Fraction(5, 6), Fraction(7, 3), 0, 0],
            [0, Fraction(5, 6), Fraction(5, 6), 0, 0, Fraction(2, 3), 0],
            [0, 0, Fraction(7, 3), 0, 0, Fraction(1, 3), 1],
            [0, 0, 0, Fraction(2, 3), Fraction(1, 3), 0, 0],
            [0, 0, 0, 0, 1, 0, 0]
        ]
        self.assertEqual(test_res, wanted_res)


if __name__ == "__main__":
    unittest.main()
