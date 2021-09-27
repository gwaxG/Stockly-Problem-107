#!/usr/local/bin/python

import sys
import numpy as np

def create_set(arr):
    """
    Create a set of elements with the next profile (edge weight, node1, node2)
    :param arr: 2D array
    :return: 1D array without -1 values
    """
    s = []
    for i, row in enumerate(arr):
        for j, weight in enumerate(row):
            if weight != -1:
                s.append([weight, i, j])
    return s

def are_trees_different(vertices, r, c):
    """
    Find out if connected vertices r and c belong to different trees.
    :param vertices: constructing reduced graph
    :param r: node 1
    :param c: node 2
    :return: are nodes r and c belong to different trees
    """
    # if sum(vertices[r]) == 0:
    #     return True
    # Figure out if r and c nodes are located in the same trees.
    # We start by the node r and look for a connection to the node c.
    indexes = [r]
    mem = [r]
    while len(indexes) != 0:
        row = vertices[indexes.pop(0)]
        if sum(row) == 0:
            return True
        # go through the row and find not null elements
        for i, el in enumerate(row):
            if i == c and el != 0:
                return False
            if el != 0:
                if i not in mem:
                    indexes.append(i)
                    mem.append(i)
    return True

def reduce(graph):
    """
    Remove redundant edges through Kruskal's algorithm.
    :param graph: full graph
    :return: graph with removed edges
    """
    # 1 create a forest f where each vertex is a separate tree
    reduced_graph = np.zeros((len(graph), len(graph[0])))
    # 2 create a set s containing all edges in the graph
    s = create_set(graph)
    s.sort(key = lambda cell: cell[0])
    # 3 while S is not empty and f is not spanning
    while len(s) != 0:
        # remove an edge with minimum weight from S
        value, r, c = s.pop(0)
        # if the edge connects two different trees then add it to the forest F, combining two trees in the single tree
        if are_trees_different(reduced_graph, r, c):
            reduced_graph[r][c] = value
            reduced_graph[c][r] = value
    return reduced_graph

def calculate_weight(graph):
    """
    Calculate the sum of all edges in the graph.
    :param graph: matrix graph representation.
    :return: graph weight weight
    """
    return np.sum(graph)/2

def get_data(fname):
    """
    Rertrieve data from fname in the form of 2D array.
    :param fname: file name of raw data
    :return: 2D array-alike matrix representation
    """
    data = []
    with open(fname, "r") as f:
        for row in f.readlines():
            split_row = row.split(",")
            int_row = []
            for element in split_row:
                if element != "-" and element != "-\n":
                    int_row.append(int(element))
                else:
                    int_row.append(-1)
            data.append(int_row)
    return data

def main(fname):
    """
    Entry point of the program.
    :fname: data file name
    :return:
    """
    graph = get_data(fname)
    reduced_graph = reduce(graph)
    weight = calculate_weight(reduced_graph)
    print(f"Weight is {int(weight)}")

if __name__ == "__main__":
    main(sys.argv[1])
