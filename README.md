# TSP_Algorithms
As exercise for the advanced algorithms class i'm taking, i need to implement 3 algorithms that given a graph return a minimum hamiltonian cycle over the graph.

The language i've choosen for this exercise is python, the decision is based on the fact that the exercise is thought for groups of 3 students but i've decided to do it on my own, and i prefer speed of development over performances.

The graphs to be used for testing are in the **tsp_dataset** folder.

## What is an Hamiltonian Cycle?

Let a graph G be a couple (V, E) where V is a set of vertices and E is a set of edges, where each edge is a triplet (u, v, w) where u and v are vertices and w is an integer representing the weight of the edge between u and v.

Then, an Hamiltonian Cycle H is a cycle (non-empty list of adjacent vertices connected by edges where the first and last are the same vertex) over all vertices such that its weight is minimum.

## The algorithms:

The algorithms implemented are:

* Held-Karp's algorithm
* Nearest neighbor euristic
* 2-Approximation algorithm

Since this problem is NP-Hard, all known algorithms that solve optimally the problem are computationally complex. Held-Karp's algorithm is one of these. 

Nearest neighbor is an euristic: it returns a good result without guarantess of its goodness.

The 2-Approximation algorithm returns a solution which is in the worst case 2 times worse than the optimal solution (in this case 2 times the optimal weight).

## Results:

The biggest result: **python is slow**.

Compared to implementations in other languages python's execution time is orders of magnitude bigger.

The second biggest result: **Held-Karp's algorithm is very slow, nearest neighbor behaves very well**.

Held-Karp's algorithm is very slow, and generally isn't suitable for big graphs. NN behaves better than the 2-approximation algorithm most of the times, giving better cycles in less time.

Complete results can be found in report.pdf.
