import random
import na2degrees
import networkx as nx

def create_group_graph(m, k, p, q):

    group_graph = {}

    # Fill the group_graph dictionary with nodes
    for i in range(m * k):
        group_graph[i] = []

    # Add edges between vertices of the same group with probability p
    for i in range(m):
        for j in range(k):
            for l in range(j, k):
                if j == l:
                    continue
                else:
                    if random.random() < p:
                        group_graph[k * i + j].append(k * i + l)
                        group_graph[k * i + l].append(k * i + j)

    # Add edges between vertices of different groups with probability q
    for i in range(m):
        for j in range(k):
            if i < m:
                for l in range((i + 1) * k, m * k):
                    if random.random() < q:
                        group_graph[k * i + j].append(l)
                        group_graph[l].append(k * i + j)

    return group_graph

if __name__ == "__main__":

    m = 50
    k = 50
    p = 0.3
    q = 0.2

    group_graph = create_group_graph(m, k, p, q)

    nx_group_graph = nx.Graph()

    for node in group_graph:
        for i in group_graph[node]:
            nx_group_graph.add_edge(node, i)

    nx_group_graph_distribution = nx_group_graph.degree()

    group_graph_distribution = na2degrees.degree_distribution(group_graph)

    print(nx_group_graph_distribution)

    normalized_distribution = {}
    for degree in nx_group_graph_distribution:
        normalized_distribution[degree] = (nx_group_graph_distribution[degree] / float((m * k)))

    # create arrays for plotting
    x_data = []
    y_data = []
    for degree in normalized_distribution:
        x_data += [degree]
        y_data += [normalized_distribution[degree]]

    import matplotlib.pyplot as plt

    # plot degree distribution
    plt.xlabel('Degree')
    plt.ylabel('Normalized Rate')
    plt.title('Degree Distribution of Group Graph')
    plt.plot(x_data, y_data, marker='.', linestyle='None', color='b')
    plt.savefig('nx_group_graph_' + str(p) + "_" + str(q) + '_' + str(m) + "_" + str(k) + ".pdf")

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
