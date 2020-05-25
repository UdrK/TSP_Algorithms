import txt_reader
import graph
from algorithms import Algorithms
import os
import time

directory_name = 'tsp_dataset'
tot = len(os.listdir(directory_name))
for file in os.listdir(directory_name):
    filename = os.fsdecode(file)
    if filename.endswith("202.tsp"):
        file_path = os.path.join(directory_name, filename)
        print("Reading: {}".format(file_path))
        gr = txt_reader.file_to_graph(file_path)
        alg = Algorithms()
        beginning = time.time()
        #res = alg.HK_TSP(gr)
        res = alg.two_approx_TSP(gr)
        ending = time.time()
        res2 = alg.nearest_neighbor_heuristic_TSP(gr)
        ending2 = time.time()
        print("two approx time: {} res: {}".format(ending - beginning, res))
        print("nearest neighbor time: {} res: {}".format(ending2 - ending, res2))

