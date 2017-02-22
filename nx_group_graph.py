import random
import na2degrees
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def create_group_graph(m, k, p, q):

    group_graph = nx.Graph()

    # Fill the group_graph dictionary with nodes
    group_graph.add_nodes_from(range(m * k))

    # Add edges between vertices of the same group with probability p
    for i in range(m):
        for j in range(k):
            for l in range(j, k):
                if j == l:
                    continue
                else:
                    if random.random() < p:
                        group_graph.add_edge(k * i + j, k * i + l)
                        # group_graph.add_edge(k * i + l, k * i + j)

    # Add edges between vertices of different groups with probability q
    for i in range(m):
        for j in range(k):
            if i < m:
                for l in range((i + 1) * k, m * k):
                    if random.random() < q:
                        group_graph.add_edge(k * i + j, l)
                        # group_graph.add_edge(l, k * i + j)

    return group_graph

if __name__ == "__main__":

    m = 5
    k = 100
    # p = 0.3
    # q = 0.2
    #
    # nx_group_graph = create_group_graph(m, k, p, q)
    #
    # nx_group_graph_distribution = {}
    #
    # nx_group_graph_degree = nx_group_graph.degree()
    #
    # for node in nx_group_graph_degree:
    #     if nx_group_graph_degree[node] in nx_group_graph_distribution:
    #         nx_group_graph_distribution[nx_group_graph_degree[node]] += 1
    #     else:
    #         nx_group_graph_distribution[nx_group_graph_degree[node]] = 1
    #
    # normalized_distribution = {}
    # for degree in nx_group_graph_distribution:
    #     normalized_distribution[degree] = (nx_group_graph_distribution[degree] / float((m * k)))
    #
    # # create arrays for plotting
    # x_data = []
    # y_data = []
    # for degree in normalized_distribution:
    #     x_data += [degree]
    #     y_data += [normalized_distribution[degree]]
    #
    # # plot degree distribution
    # plt.xlabel('Degree')
    # plt.ylabel('Normalized Rate')
    # # plt.title('Degree Distribution of Group Graph')
    # plt.plot(x_data, y_data, marker='s', linestyle='None', color='r')
    # plt.savefig('nx_group_graph_degree_distribution_' + str(p) + "_" + str(q) + '_' + str(m) + "_" + str(k) + ".pdf")

    # q = 0.5
    #

    y_data = []
    for p in np.linspace(0, 1, 21):
        nx_group_graph = create_group_graph(m, k, p, 0.5)
        y_data.append(nx.average_clustering(nx_group_graph))

    plt.xlabel('p')
    plt.ylabel('Clustering Coefficient')
    plt.plot(np.linspace(0, 1, 21), y_data, marker='s', linestyle='None', color='r')
    plt.savefig('nx_group_graph_clustering_coefficient.pdf')

    # y_data = []
    #
    # for p in np.linspace(0, 1, 21):
    #     nx_group_graph = create_group_graph(m, k, p, q)
    #     y_data += [nx.diameter(nx_group_graph)]
    #
    # plt.xlabel('p')
    # plt.ylabel('Diameter')
    # plt.title('Diameter of Group Graph')
    # plt.plot(np.linspace(0, 1, 21), y_data, marker='.', linestyle='None', color='b')
    # plt.savefig('nx_group_graph_diameter_' + str(p) + "_" + str(q) + '_' + str(m) + "_" + str(k) + ".pdf")
    #
    # for m in range(2, 20):
    #     for k in range(2, 20):
    #         m = 50
    #         k = 50
    #
    #         for p in range(50, 25, -5):
    #             p /= 100.0
    #             q = 0.5 - p
    #             group_graph = create_group_graph(m, k, p, q)
    #             group_graph_distribution = na2degrees.degree_distribution(group_graph)
    #
    #             normalized_distribution = {}
    #             for degree in group_graph_distribution:
    #                 normalized_distribution[degree] = (group_graph_distribution[degree] / float((m * k)))
    #
    #             # create arrays for plotting
    #             x_data = []
    #             y_data = []
    #             for degree in normalized_distribution:
    #                 x_data += [degree]
    #                 y_data += [normalized_distribution[degree]]
    #
    #             import matplotlib.pyplot as plt
    #
    #             # plot degree distribution
    #             plt.xlabel('Degree')
    #             plt.ylabel('Normalized Rate')
    #             plt.title('Degree Distribution of Group Graph')
    #             plt.plot(x_data, y_data, marker='.', linestyle='None', color='b')
    #             plt.savefig('group_graph_' + str(p) + "_" + str(q) + '_' + str(m) + "_" + str(k) + ".pdf")
