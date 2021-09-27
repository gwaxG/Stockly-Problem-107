#!/usr/local/bin/python

def solve(network):
    print(network, type(network))

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
                elif element == "-":
                    int_row.append(-1)
            data.append(int_row)
    return data

def main():
    net = get_data("p107_network.txt")
    print(net)

if __name__ == "__main__":
    main()