import unittest
from src.Betweeeness import *


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
        nodes = []
        for i in range(7):
            nodes.append(Node(i))
        self.graph = Graph(mat, nodes)

    def test_init_0(self):
        directed_graph = DirectedGraph(self.graph, 0)
        betweenness = BetweennessOneNode(directed_graph)
        test_res = betweenness.betweenness_mat
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

    def test_init_1(self):
        directed_graph = DirectedGraph(self.graph, 1)
        betweenness = BetweennessOneNode(directed_graph)
        test_res = betweenness.betweenness_mat
        wanted_res = [
            [0, Fraction(13, 6), Fraction(7, 6), 0, 0, 0, 0],
            [Fraction(13, 6), 0, 0, Fraction(23, 6), 0, 0, 0],
            [Fraction(7, 6), 0, 0, Fraction(7, 6), Fraction(4, 3), 0, 0],
            [0, Fraction(23, 6), Fraction(7, 6), 0, 0, Fraction(5, 3), 0],
            [0, 0, Fraction(4, 3), 0, 0, Fraction(2, 3), 1],
            [0, 0, 0, Fraction(5, 3), Fraction(2, 3), 0, 0],
            [0, 0, 0, 0, 1, 0, 0]
        ]
        self.assertEqual(test_res, wanted_res)

if __name__ == "__main__":
    unittest.main()
