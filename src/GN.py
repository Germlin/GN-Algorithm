from .Graph import *
from .betweeeness import *
import copy


class GN:
    def __init__(self,graph):
        assert isinstance(graph, Graph)
        self.mat = mat = copy.deepcopy(graph)
        self.remove_edge_order = []
        while mat.isolated() is False:
            betweenness = Betweenness(self.mat)
            remove_edge = (max, node_1, node_2) = betweenness.max_betweenness_edges()
            self.remove_edge_order.append(remove_edge)
            self.mat.remove_edge(node_1,node_2)
            self.mat.remove_edge(node_2,node_1)

    def present(self):
        """
        I will try to use a more visualized way to present the ressult.
        """
        pass