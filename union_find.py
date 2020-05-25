class UnionFind:
    def __init__(self):
        self.parents = {}
        self.size = {}

    def initialize(self, xs):
        for x in xs:
            self.parents[x] = x
            self.size[x] = 1

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            return self.find(self.parents[x])

    # expects results of find in input
    def union(self, i, j):
        size_i = self.size[i]
        size_j = self.size[j]
        if size_i >= size_j:
            self.parents[j] = i
            self.size[i] += self.size[j]
        else:
            self.parents[i] = j
            self.size[j] += self.size[i]
