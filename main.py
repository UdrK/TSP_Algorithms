import txt_reader
import graph
from algorithms import Algorithms
import os
import time

directory_name = 'tsp_dataset'
tot = len(os.listdir(directory_name))
for file in os.listdir(directory_name):
    filename = os.fsdecode(file)
    if filename.endswith(".tsp"):
        file_path = os.path.join(directory_name, filename)
        print("Processing: {}".format(file_path))

        gr = txt_reader.file_to_graph(file_path)
        alg = Algorithms()

        beginning = time.time()
        exact_res = alg.HK_TSP(gr, 1)
        ending = time.time()

        heuristic_res = alg.nearest_neighbor_heuristic_TSP(gr)
        ending2 = time.time()

        two_approx_res = alg.two_approx_TSP(gr)
        ending3 = time.time()

        f_exact = open('exact_results.txt', 'a+')
        f_exact.write('{}, {}, {}\n'.format(filename, ending - beginning, exact_res))
        f_exact.close()

        f_heuristic = open('heuristic_results.txt', 'a+')
        f_heuristic.write('{}, {}, {}\n'.format(filename, ending - ending2, heuristic_res))
        f_heuristic.close()

        f_two_approx = open('two_approx_results.txt', 'a+')
        f_two_approx.write('{}, {}, {}\n'.format(filename, ending3 - ending2, two_approx_res))
        f_two_approx.close()
