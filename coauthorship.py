import csv
import networkx as nx
import na3pa
import nx_ws_graph
import nx_group_graph
import pickle
import random
import matplotlib.pyplot as plt


def create_coauthorship_graph():

    reader = csv.reader(open("coauthorship_edges.txt"), delimiter=' ')

    nx_coauthorship_graph = nx.Graph()

    for vertex in range(1559):
        nx_coauthorship_graph.add_node(vertex)

    for row in reader:
        nx_coauthorship_graph.add_edge(int(row[0]) - 1, int(row[1]) - 1)

    return nx_coauthorship_graph


if __name__ == "__main__":

    nx_coauthorship_graph = create_coauthorship_graph()
    nx_random_graph = nx.erdos_renyi_graph(1559, 0.0337)
    nx_PA_graph = na3pa.make_PA_Graph(1559, 36)
    nx_group_graph = nx_group_graph.create_group_graph(75, 20, 0.3, 0.033)
    nx_ws_graph = nx_ws_graph.make_ws_graph(1559, 26, 0.3)

    print("coauthorship nodes: " + str(nx_coauthorship_graph.number_of_nodes()) + ", edges: " +
          str(nx_coauthorship_graph.number_of_edges()))
    print("random nodes: " + str(nx_random_graph.number_of_nodes()) + ", edges: " +
          str(nx_random_graph.number_of_edges()))
    print("PA nodes: " + str(nx_PA_graph.number_of_nodes()) + ", edges: " +
          str(nx_PA_graph.number_of_edges()))
    print("group nodes: " + str(nx_group_graph.number_of_nodes()) + ", edges: " +
          str(nx_group_graph.number_of_edges()))
    print("WS nodes: " + str(nx_ws_graph.number_of_nodes()) + ", edges: " +
          str(nx_ws_graph.number_of_edges()))

    coauthorship_graph = nx.to_dict_of_lists(nx_coauthorship_graph)
    PA_graph = nx.to_dict_of_lists(nx_PA_graph)
    random_graph = nx.to_dict_of_lists(nx_random_graph)
    group_graph = nx.to_dict_of_lists(nx_group_graph)
    ws_graph = nx.to_dict_of_lists(nx_ws_graph)

    graphs = [coauthorship_graph, random_graph, PA_graph, group_graph, ws_graph]

    graph_4cycles = []

    num_samples = 50

    for graph in graphs:

        adjacency_matrix = []

        for u in range(len(graph)):
            row = []
            for v in range(len(graph)):
                if v in graph[u]:
                    row.append(1)
                else:
                    row.append(0)
            adjacency_matrix.append(row)

        print("finished making adjacency matrix")

        vertices = random.sample(graph.keys(), num_samples)

        four_cycle_dict = {}

        for vertex in vertices:
            count = 0
            for idx1 in range(len(graph[vertex])):
                for idx2 in range(idx1 + 1, (len(graph[vertex]))):  # find all distinct pairs of neighbours of vertex
                    neighbour1 = graph[vertex][idx1]
                    neighbour2 = graph[vertex][idx2]
                    for dist2_neighbour in graph[neighbour1]:  # look at neighbours of neighbour1
                        if dist2_neighbour != vertex and adjacency_matrix[dist2_neighbour][
                                neighbour2] == 1:  # see if they are also neighbours of neighbour2
                            count += 1  # if so a 4-cycle has been found
            four_cycle_dict[vertex] = count

        graph_4cycles.append(four_cycle_dict)

    with open('4cycles', 'wb') as fp:
        pickle.dump(graph_4cycles, fp)

    graph_5cycles = []

    for graph in graphs:

        adjacency_matrix = []

        for u in range(len(graph)):
            row = []
            for v in range(len(graph)):
                if v in graph[u]:
                    row.append(1)
                else:
                    row.append(0)
            adjacency_matrix.append(row)

        print("finished making adjacency matrix")

        vertices = random.sample(graph.keys(), num_samples)

        cycle_dict = {}

        for vertex in vertices:
            print(vertex)
            count = 0
            for idx1 in range(len(graph[vertex])):
                neighbour1 = graph[vertex][idx1]
                for idx2 in range(idx1 + 1, (len(graph[vertex]))):  # find all distinct pairs of neighbours of vertex
                    neighbour2 = graph[vertex][idx2]
                    for dist2_neighbour1 in graph[neighbour1]:  # look at neighbours of neighbour1
                        if vertex != dist2_neighbour1:
                            for dist2_neighbour2 in graph[neighbour2]:  # and neighbours of neighbour2
                                if adjacency_matrix[dist2_neighbour1][
                                        dist2_neighbour2] == 1 and vertex != dist2_neighbour2:  # see if they are adjacent
                                    count += 1  # if so a 5-cycle has been found
            cycle_dict[vertex] = count

        graph_5cycles.append(cycle_dict)

    with open('5cycles', 'wb') as fp:
        pickle.dump(graph_5cycles, fp)

    with open('4cycles', 'rb') as fp:
        graph_4cycles = pickle.load(fp)

    ydata = [1 for i in range(num_samples)] + [2 for i in range(num_samples)] + [3 for i in range(num_samples)] + [4 for i in range(num_samples)] + \
            [5 for i in range(num_samples)]

    coauthorship = [graph_4cycles[0][k] for k in graph_4cycles[0]]
    random = [graph_4cycles[1][k] for k in graph_4cycles[1]]
    PA = [graph_4cycles[2][k] for k in graph_4cycles[2]]
    group = [graph_4cycles[3][k] for k in graph_4cycles[3]]
    WS = [graph_4cycles[4][k] for k in graph_4cycles[4]]
    xdata = coauthorship + random + PA + group + WS
    plt.figure()
    plt.ylim(0, 6)
    plt.yticks((1, 2, 3, 4, 5), ('Coauthorship', 'Random', 'PA', 'Group', 'WS'))
    plt.semilogx(xdata, ydata, marker='s', linestyle='None', color='r')
    plt.subplots_adjust(left=0.2)
    plt.xlabel("Number of 4-cycles")
    plt.savefig("4cycles.pdf")

    with open('5cycles', 'rb') as fp:
        graph_5cycles = pickle.load(fp)

    ydata = [1 for i in range(num_samples)] + [2 for i in range(num_samples)] + [3 for i in range(num_samples)] + [4 for i in range(num_samples)] + \
            [5 for i in range(num_samples)]

    coauthorship = [graph_5cycles[0][k] for k in graph_5cycles[0]]
    random = [graph_5cycles[1][k] for k in graph_5cycles[1]]
    PA = [graph_5cycles[2][k] for k in graph_5cycles[2]]
    group = [graph_5cycles[3][k] for k in graph_5cycles[3]]
    WS = [graph_5cycles[4][k] for k in graph_5cycles[4]]
    xdata = coauthorship + random + PA + group + WS
    plt.figure()
    plt.ylim(0, 6)
    plt.yticks((1, 2, 3, 4, 5), ('Coauthorship', 'Random', 'PA', 'Group', 'WS'))
    plt.semilogx(xdata, ydata, marker='s', linestyle='None', color='r')
    plt.subplots_adjust(left=0.2)
    plt.xlabel("Number of 5-cycles")
    plt.savefig("5cycles.pdf")
