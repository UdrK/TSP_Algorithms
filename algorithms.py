import math
import time
from union_find import UnionFind
from heap import Heap

class Algorithms:

    def HK_VISIT(self, v, S, max_time):
        if S == frozenset({v}):
            return self.w[v][0]
        elif (v, S) in self.d:
            return self.d[(v, S)]
        else:
            mindist = math.inf
            minprec = None

            # this line makes the algorithm occupy less space in memory
            # without the algorithm encounters a memory error when executed on "ulysses22.tsp"
            subset = S - {v}
            for u in subset:
                dist = self.HK_VISIT(u, subset, max_time)
                if dist + self.w[u][v] < mindist:
                    mindist = dist + self.w[u][v]
                    minprec = u
                if time.time() - self.starting_time > max_time:
                    break

            self.d[(v, S)] = mindist
            self.p[(v, S)] = minprec
            return mindist

    def kruskal(self, graph):
        MST = []
        MST_weight = 0

        # initializing Union Find
        U = UnionFind()
        U.initialize(graph.vertices)

        # initializing heap
        heap = Heap()
        vert_number = len(graph.vertices)
        for i in range(0, vert_number):
            for j in range(i+1, vert_number):
                heap.push([graph.adjacency_matrix[i][j], (i, j)])  # [cost, edge]

        while not (len(MST) == vert_number - 1 or heap.is_empty()):
            aux_edge = heap.pop()
            edge = [aux_edge[1][0], aux_edge[1][1], aux_edge[0]]  # v1, v2, cost
            e0_find = U.find(edge[0])
            e1_find = U.find(edge[1])

            if e0_find != e1_find:
                MST.append(edge)
                MST_weight += edge[2]  # weighting MST
                U.union(e0_find, e1_find)

        return MST, MST_weight

    def edge_list_to_adjacency_matrix(self, edge_list, vert_number):
        adjaceny_matrix = [[math.inf for i in range(vert_number)] for j in range(vert_number)]

        for edge in edge_list:
            vert1 = edge[0]
            vert2 = edge[1]
            distance = edge[2]
            adjaceny_matrix[vert1][vert2] = distance
            adjaceny_matrix[vert2][vert1] = distance

        return adjaceny_matrix

    def adjacency_matrix_DFS(self, start_vertex, adjacency_matrix):
        visited = [start_vertex]

        i = 0
        j = 0
        added_in_current_row = 0
        aux = 0
        while len(visited) < len(adjacency_matrix):
            added_in_current_row = 0
            weight = adjacency_matrix[i][j]
            j += 1
            if weight < math.inf and not j-1 in visited:
                visited.append(j-1)
                i = j-1
                j = 0
                added_in_current_row += 1
                aux = 0

            if j == len(adjacency_matrix):
                j = 0
                if added_in_current_row == 0:
                    i = visited[-2-aux]
                    aux += 1

        return visited

    def circuit_weight(self, graph, circuit):
        weight = 0
        for i in range(1, len(circuit)):
            weight += graph.adjacency_matrix[circuit[i-1]][circuit[i]]
        return weight

    def HK_TSP(self, graph, max_time):
        self.d = {}
        self.p = {}
        self.w = graph.adjacency_matrix
        self.starting_time = time.time()
        return self.HK_VISIT(0, frozenset(graph.vertices), max_time*60)     # turning minutes in seconds

    def nearest_neighbor_heuristic_TSP(self, graph):
        vertices = graph.vertices.copy()

        last_inserted = 0

        path = [last_inserted]
        TSP_weight = 0
        vertices.remove(last_inserted)

        while len(vertices) > 0:
            mindist = math.inf
            minsucc = None
            for i in vertices:
                if graph.adjacency_matrix[last_inserted][i] < mindist:
                    mindist = graph.adjacency_matrix[last_inserted][i]
                    minsucc = i
            path.append(minsucc)
            TSP_weight += mindist
            vertices.remove(minsucc)
            last_inserted = minsucc

        path.append(0)
        TSP_weight += graph.adjacency_matrix[last_inserted][0]

        return TSP_weight

    def two_approx_TSP(self, graph):
        MST, MST_weight = self.kruskal(graph)
        MST_adjacency_matrix = self.edge_list_to_adjacency_matrix(MST, len(graph.vertices))
        # since i'm not interested in the circuit itself, but in its weight, i only need the last vertex visited
        DFS_visit = self.adjacency_matrix_DFS(0, MST_adjacency_matrix)
        DFS_visit.append(0)
        TSP_weight = self.circuit_weight(graph, DFS_visit)
        return TSP_weight
