# 定义GN算法用到的数据结构，以及介数的计算

from src.UniqueQueue import UniqueQueue


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
    def __init__(self, mat):
        self.connection_mat = mat
        self.num_node = len(mat)

    def remove_edge(self, src, dst):
        self.connection_mat[src][dst] = 0

    def shortest_path(self, src):
        visited = []
        distance = []
        parent = []
        num = self.num_node

        # initial
        for i in range(num):
            visited.append(False)
            distance.append(-1)
            parent.append(-1)

        # insert the source node
        visited[src] = True
        distance[src] = 0
        parent[src] = src
        for i in range(num):
            if i != src:
                if self.connection_mat[src][i] != 0:
                    distance[i] = self.connection_mat[src][i]
                    parent[i] = src

        while True:
            index = 0
            while index < num:
                if visited[index] is False and distance[index] != -1:
                    min_index = index
                    min_distance = distance[index]
                    break
                index += 1

            if index == num:
                break

            while index < num:
                if visited[index] is False and distance[index] != -1:
                    if distance[index] < min_distance:
                        min_index = index
                        min_distance = distance[index]
                index += 1

            visited[min_index] = True

            for i in range(num):
                if self.connection_mat[min_index][i] != 0:
                    if distance[i] == -1:
                        distance[i] = self.connection_mat[min_index][i] + distance[min_index]
                        parent[i] = min_index
                    elif distance[i] > self.connection_mat[min_index][i] + distance[min_index]:
                        distance[i] = self.connection_mat[min_index][i] + distance[min_index]
                        parent[i] = min_index

        return [visited, distance, parent]

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

        self.nodes = []
        for i in range(graph.num_node):
            self.nodes.append(Node(i))

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

