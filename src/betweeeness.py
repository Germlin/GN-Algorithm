from .Graph import *
from fractions import Fraction


class BetweennessOneNode:
    def __init__(self, directed_graph):
        assert isinstance(directed_graph, DirectedGraph)
        self.betweenness_mat = []
        for i in range(directed_graph.num_node):
            self.betweenness_mat.append([])
            for j in range(directed_graph.num_node):
                self.betweenness_mat[i].append(0)

        out_degrees = []
        nodes_id = []
        for i in range(directed_graph.num_node):
            node = directed_graph.nodes[i]
            if node.connected is True:
                nodes_id.append(node.id)
                out_degrees.append(node.out_degree)

        index = 0
        while index < len(nodes_id):
            if out_degrees[index] == 0:
                out_degrees[index] -= 1
                for i in range(directed_graph.num_node):
                    if directed_graph.connection_mat[i][index] == 1:
                        out_degrees[i] -= 1
                        w = Fraction(
                            (directed_graph.nodes[index].betweenness + 1) * directed_graph.nodes[i].weight,
                            directed_graph.nodes[index].weight)
                        self.betweenness_mat[index][i] = self.betweenness_mat[i][index] = w
                        directed_graph.nodes[i].betweenness += w
                index = 0
            index += 1


class Betweenness:
    def __init__(self, graph):
        self.num_node = num_node = graph.num_node
        self.betweenness = []
        for i in range(num_node):
            self.betweenness.append([])
            for j in range(num_node):
                self.betweenness[i].append(0)

        for i in range(num_node):
            directed_graph = DirectedGraph(graph, i)
            betweenness_mat = BetweennessOneNode(directed_graph)

            for i in range(num_node):
                for j in range(num_node):
                    self.betweenness[i][j] += betweenness_mat[i][j]

    def max_betweenness_edges(self):
        max = node_1 = node_2 = 0
        for i in range(self.num_node):
            for j in range(i, self.num_node):
                if self.betweenness[i][j] > max:
                    max = self.betweenness[i][j]
                    node_1 = i
                    node_2 = j
        return max, node_1, node_2
