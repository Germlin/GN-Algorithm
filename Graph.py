# 定义GN算法用到的数据结构，以及介数的计算

from UniqueQueue import UniqueQueue


class Node:
    def __init__(self, id, distance=-1, weight=0):
        self.id = id
        self.distance = distance
        self.weight = weight

    def __eq__(self, other):
        if self.id == other.id and self.distance == other.distance and self.weight == other.weight:
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


def calculate_distance_and_weight(graph, src):
    nodes = []
    for i in range(graph.num_node):
        nodes.append(Node(i))

    nodes[src].distance = 0
    nodes[src].weight = 1
    visit = UniqueQueue()
    visit.append(nodes[src])
    while len(visit) != 0:
        node = visit.pop()
        for j in range(graph.num_node):
            if graph.connection_mat[node.id][j] == 1:
                if nodes[j].distance == -1:
                    nodes[j].distance = node.distance + 1
                    nodes[j].weight = node.weight
                    visit.append(nodes[j])
                elif nodes[j].distance == node.distance + 1:
                    nodes[j].weight += node.weight
                    visit.append(nodes[j])

    return nodes


def dijkstra(graph, src):
    visited = []
    distance = []
    parent = []
    num = graph.num_node

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
            if graph.connection_mat[src][i] != 0:
                distance[i] = graph.connection_mat[src][i]
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
            if graph.connection_mat[min_index][i] != 0:
                if distance[i] == -1:
                    distance[i] = graph.connection_mat[min_index][i] + distance[min_index]
                    parent[i] = min_index
                elif distance[i] > graph.connection_mat[min_index][i] + distance[min_index]:
                    distance[i] = graph.connection_mat[min_index][i] + distance[min_index]
                    parent[i] = min_index

    return [visited, distance, parent]


def find_leaves(graph,src):
    not_leaves = []
    leaves = []
    for i in range(graph.num_node):
        not_leaves.append(False)

    distance_from_src = dijkstra(graph, src)[1]
    for i in range(graph.num_node):
        if i != src:
            distance_from_i = dijkstra(graph, i)[1]
            distance_src_to_i = distance_from_src[i]
            for j in range(graph.num_node):
                if j != i:
                    if distance_from_src[j] + distance_from_i[j] == distance_src_to_i:
                        not_leaves[j] = True

    for i in range(graph.num_node):
        if not_leaves[i] is False:
            leaves.append(i)

    return leaves
