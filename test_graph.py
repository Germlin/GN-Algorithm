import unittest
from Graph import *


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


class TestCDAM(TestGraph):
    def test_CDAW(self):
        test_res = calculate_distance_and_weight(self.graph, 0)
        wanted_res = [Node(0, 0, 1), Node(1, 1, 1), Node(2, 1, 1), Node(3, 2, 2),
                      Node(4, 2, 1), Node(5, 3, 3), Node(6, 3, 1)]
        self.assertEqual(test_res, wanted_res)


class TestDijkstra(TestGraph):
    def test_dijkstra(self):
        test_res = dijkstra(self.graph, 0)
        wanted_res = [[True, True, True, True, True, True, True],
                      [0, 1, 1, 2, 2, 3, 3],
                      [0, 0, 0, 1, 2, 3, 4]]
        self.assertEqual(test_res[0], wanted_res[0])
        self.assertEqual(test_res[1], wanted_res[1])
        self.assertEqual(test_res[2], wanted_res[2])


class TestFindLeaves(TestGraph):
    def test_find_leaves(self):
        test_res = find_leaves(self.graph, 0)
        wanted_res = [5, 6]
        self.assertEqual(test_res, wanted_res)


if __name__ == "__main__":
    unittest.main()
