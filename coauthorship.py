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

    PA_graph = nx.to_dict_of_lists(na3pa.make_PA_Graph(1486, 39))
    nx_coauthorship_graph = nx.to_dict_of_lists(create_coauthorship_graph())
    random_graph = nx.to_dict_of_lists(nx.erdos_renyi_graph(1486, 0.04))
    group_graph = nx.to_dict_of_lists(nx_group_graph.create_group_graph(75, 20, 0.3, 0.033))
    ws_graph = nx.to_dict_of_lists(nx_ws_graph.make_ws_graph(1486, 28, 0.5))

    coauthorship_graph = create_coauthorship_graph()
    print(coauthorship_graph.number_of_nodes())
    print(coauthorship_graph.number_of_edges())

    graphs = [nx_coauthorship_graph, random_graph, PA_graph, group_graph, ws_graph]

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

    ydata = [1 for i in range(num_samples)] + [2 for i in range(num_samples)] + [3 for i in range(num_samples)] + [4 for i in range(num_samples)] + \
            [5 for i in range(num_samples)]

    coauthorship = [graph_4cycles[0][k] for k in graph_4cycles[0]]
    random = [graph_4cycles[1][k] for k in graph_4cycles[1]]
    PA = [graph_4cycles[2][k] for k in graph_4cycles[2]]
    group = [graph_4cycles[3][k] for k in graph_4cycles[3]]
    WS = [graph_4cycles[4][k] for k in graph_4cycles[4]]
    xdata = coauthorship + random + PA + group + WS
    plt.ylim(0, 6)
    plt.yticks((1, 2, 3, 4, 5), ('Coauthorship', 'Random', 'PA', 'Group', 'WS'))
    plt.semilogx(xdata, ydata, marker='s', linestyle='None', color='r')
    plt.savefig("4cycles.pdf")

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

    ydata = [1 for i in range(num_samples)] + [2 for i in range(num_samples)] + [3 for i in range(num_samples)] + [4 for i in range(num_samples)] + \
            [5 for i in range(num_samples)]

    coauthorship = [graph_5cycles[0][k] for k in graph_5cycles[0]]
    random = [graph_5cycles[1][k] for k in graph_5cycles[1]]
    PA = [graph_5cycles[2][k] for k in graph_5cycles[2]]
    group = [graph_5cycles[3][k] for k in graph_5cycles[3]]
    WS = [graph_5cycles[4][k] for k in graph_5cycles[4]]
    xdata = coauthorship + random + PA + group + WS
    plt.ylim(0, 6)
    plt.yticks((1, 2, 3, 4, 5), ('Coauthorship', 'Random', 'PA', 'Group', 'WS'))
    plt.semilogx(xdata, ydata, marker='s', linestyle='None', color='r')
    plt.savefig("5cycles.pdf")

    # for vertex in vertices:
    #     print(vertex)
    #     count = 0
    #     for idx1 in graph[vertex]:
    #         neighbour1 = idx1
    #         for idx2 in graph[vertex]:  # find all distinct pairs of neighbours of vertex
    #             neighbour2 = idx2
    #             if neighbour1 != neighbour2:
    #                 for dist2_neighbour1 in graph[neighbour1]:  # look at neighbours of neighbour1
    #                     if vertex != dist2_neighbour1:
    #                         for dist2_neighbour2 in graph[neighbour2]:  # and neighbours of neighbour2
    #                             if adjacency_matrix[dist2_neighbour1][
    #                                 dist2_neighbour2] == 1 and vertex != dist2_neighbour2:  # see if they are adjacent
    #                                 count += 1  # if so a 5-cycle has been found
    #     cycle_dict[vertex] = count
    #
    # graph_5cycles.append(cycle_dict)



    # five_cycle_dict = {}
    #
    # for vertex in nx_coauthorship_graph.nodes_iter():
    #     five_cycle_dict[vertex] = 0
    #     for neighbour in nx_coauthorship_graph.neighbors_iter(vertex):
    #         for nn in nx_coauthorship_graph.neighbors_iter(neighbour):
    #             for nnn in nx_coauthorship_graph.neighbors_iter(nn):
    #                 for nnnn in nx_coauthorship_graph.neighbors_iter(nnn):
    #                     if vertex in nx_coauthorship_graph.neighbors_iter(nnnn):
    #                         five_cycle_dict[vertex] += 1
    #
    # print(five_cycle_dict)

    # four_cycle_dict = {}
    #
    # # maybe look at making non-directed?
    # for vertex in nx_coauthorship_graph.nodes_iter():
    #     four_cycle_dict[vertex] = 0
    #     for neighbour in nx_coauthorship_graph.neighbors_iter(vertex):
    #         for nn in nx_coauthorship_graph.neighbors_iter(neighbour):
    #             for nnn in nx_coauthorship_graph.neighbors_iter(nn):
    #                 if vertex in nx_coauthorship_graph.neighbors_iter(nnn):
    #                     four_cycle_dict[vertex] += 1
    #
    # print(four_cycle_dict)


    #cycle_gen = nx.simple_cycles(nx_coauthorship_graph)
    #print(list(cycle_gen))
