import unittest

from src.Graph import *


class TestGraph(unittest.TestCase):
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

    def test_dijkstra(self):
        test_res = self.graph.shortest_path(0)
        wanted_res = [[True, True, True, True, True, True, True],
                      [0, 1, 1, 2, 2, 3, 3],
                      [0, 0, 0, 1, 2, 3, 4]]
        self.assertEqual(test_res[0], wanted_res[0])
        self.assertEqual(test_res[1], wanted_res[1])
        self.assertEqual(test_res[2], wanted_res[2])


class TestDirectedGraph(TestGraph):
    def setUp(self):
        super(TestDirectedGraph, self).setUp()
        self.directed_graph = DirectedGraph(self.graph, 0)

    def test_leaves(self):
        test_res = self.directed_graph.leaves()
        wanted_res = [5, 6]
        self.assertEqual(test_res, wanted_res)

    def test_init(self):
        test_res = self.directed_graph.nodes
        wanted_res = [Node(0, 0, 1, 0, 2), Node(1, 1, 1, 1, 1), Node(2, 1, 1, 1, 2), Node(3, 2, 2, 2, 1),
                      Node(4, 2, 1, 1, 2), Node(5, 3, 3, 2, 0), Node(6, 3, 1, 1, 0)]
        self.assertEqual(test_res, wanted_res)


if __name__ == "__main__":
    unittest.main()
