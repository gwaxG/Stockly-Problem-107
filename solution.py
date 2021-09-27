#!/usr/local/bin/python

import sys
import numpy as np

def get_list(arr):
    """
    :param arr: 2D array
    :return: 1D array without -1 values
    """
    l = []
    for i, row in enumerate(arr):
        for j, element in enumerate(row):
            if element != -1:
                # array containing edge weight and two vertices
                l.append([element, i, j])
    return l

def are_trees_different(vertices, r, c):
    """
    FInd out if connected vertices r and c belong to different trees in f
    :param vertices: matrice of values
    :param r: node A
    :param c: node B
    :return: are nodes r and c belong to different trees
    """
    if sum(vertices[r]) == 0:
        return True
    return False

def remove_connections(net):
    """
    Remove redundant edges through Kruskal's algorithm.
    :param net: full network
    :return: network with removed edges
    """
    # 1 create a forest f where each vertex is a separate tree
    f = np.zeros((len(net), len(net[0])))
    # 2 create a set s containing all edges in the graph
    s = get_list(net)
    s.sort(key = lambda cell: cell[0])
    # 3 while S is not empty and f is not spanning
    while len(s) != 0:
        # remove an edge with minimum weight from S
        value, r, c = s.pop(0)
        # if the edge connects two different trees then add it to the forest F, combining two trees in the single tree
        if are_trees_different(f, r,c ):
            f[r][c] = value
    return f

def calculate_weight(resized_net):
    """
    Go through network and count weight.
    :param resized_net: network passed through Kruskal' algorithm.
    :return: network weight
    """
    return np.sum(resized_net)

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
    net = get_data(fname)
    resized_net = remove_connections(net)
    print(resized_net)
    weight = calculate_weight(resized_net)
    print(weight)

if __name__ == "__main__":
    main(sys.argv[1])
