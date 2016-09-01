# 定义GN算法用到的数据结构，以及介数的计算

from src.UniqueQueue import UniqueQueue
import copy

class Node:
    def __init__(self, id, distance=-1, weight=0, in_degree=0, out_degree=0, connected = False, betweenness=0):
        self.id = id
        self.distance = distance
        self.weight = weight
        self.betweenness = betweenness
        self.in_degree = in_degree
        self.out_degree = out_degree
        self.connected = connected

    def __eq__(self, other):
        if self.id == other.id and self.distance == other.distance and self.weight == other.weight\
                and self.in_degree == other.in_degree and self.out_degree == other.out_degree:
            return True
        else:
            return False

    def __repr__(self):
        return "Node %d: %d %d" % (self.id, self.distance, self.weight)

    def same_element(self, other):
        if self.id == other.id:
            return True
        else:
            return False


class Graph:
    def __init__(self, mat, nodes_list):
        self.connection_mat = mat
        self.num_node = len(mat)
        self.nodes = nodes_list

    def remove_edge(self, src, dst):
        self.connection_mat[src][dst] = 0

    def isolated(self):
        for i in range(self.num_node):
            for j in range(self.num_node):
                if self.connection_mat[i][j] != 0:
                    return False
        return True


class DirectedGraph:
    def __init__(self, graph, src):
        """
        calculate the distance and the weight for every node from given source node.
        :param graph: the connection matrix of the graph
        :param src: the source node.
        """
        self.connection_mat = []
        for i in range(graph.num_node):
            self.connection_mat.append([])
            for j in range(graph.num_node):
                self.connection_mat[i].append(0)

        self.nodes = copy.deepcopy(graph.nodes)

        self.num_node = graph.num_node

        self.nodes[src].distance = 0
        self.nodes[src].weight = 1
        self.nodes[src].connected = True

        visit = UniqueQueue()
        visit.append(self.nodes[src])
        while len(visit) != 0:
            node = visit.pop()
            for j in range(graph.num_node):
                if graph.connection_mat[node.id][j] == 1:
                    if self.nodes[j].distance == -1:
                        self.nodes[j].distance = node.distance + 1
                        self.nodes[j].weight = node.weight
                    elif self.nodes[j].distance == node.distance + 1:
                        self.nodes[j].weight += node.weight
                    else:
                        continue

                    visit.append(self.nodes[j])
                    self.connection_mat[node.id][j] = 1
                    self.nodes[node.id].out_degree += 1
                    self.nodes[j].in_degree += 1
                    self.nodes[j].connected = True

        self.nodes.sort(key=lambda node: node.id)

    def leaves(self):
        leaves = []
        for i in range(self.num_node):
            if self.nodes[i].out_degree == 0 and self.nodes[i].connected is True:
                leaves.append(i)
        return leaves

