# implementation of heap based on heapq.py
class Heap:
    def __init__(self):
        self.heap = []
        self.weights = {}       # used to make update, contains and weight faster

    def build_heap(self):           # heapify
        n = len(self.heap)
        for i in reversed(range(n // 2)):
            self.siftup(i)

    def siftup(self, index):
        end = len(self.heap)
        start = index
        new_item = self.heap[index]

        child_index = 2 * index + 1
        while child_index < end:
            right_index = child_index + 1

            if right_index < end:
                child = self.heap[child_index]
                right = self.heap[right_index]
                if not (self.weights[child] < self.weights[right]):
                    child_index = right_index

            self.heap[index] = self.heap[child_index]

            index = child_index
            child_index = 2 * index + 1

        self.heap[index] = new_item

        self.siftdown(start, index)

    # used in siftup
    def siftdown(self, start, index):
        new_item = self.heap[index]

        while index > start:
            parent_index = (index - 1) >> 1
            parent = self.heap[parent_index]
            if self.weights[new_item] < self.weights[parent]:
                self.heap[index] = parent
                index = parent_index
                continue
            break

        self.heap[index] = new_item

    def push(self, pushee):     # expects pushee to be [cost, vertex]
        self.heap.append(pushee[1])
        self.weights[pushee[1]] = pushee[0]     # updates dictionary of weights used to make certain operations faster
        self.siftdown(0, len(self.heap) - 1)

    def pop(self):
        returnee = self.heap.pop(0)
        weight = self.weights[returnee]
        del(self.weights[returnee])
        if len(self.heap) > 0:
            last = self.heap.pop(-1)
            self.heap.insert(0, last)
            self.siftup(0)
        return [weight, returnee]

    def is_empty(self):
        return len(self.heap) == 0

    def update(self, new_weight, vertex):
        self.weights[vertex] = new_weight
        self.build_heap()

    def contains(self, vertex):
        return vertex in self.weights

    def weight(self, vertex):
        return self.weights[vertex]