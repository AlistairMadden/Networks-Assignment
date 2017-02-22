import random
import networkx as nx


def make_ws_graph(num_nodes, clockwise_neighbours, rewiring_prob):
    """Returns a dictionary to a undirected graph with num_nodes nodes;
    keys are nodes, values are list of neighbours.
    The nodes of the graph are numbered 0 to num_nodes - 1.
    Node i initially joined to i+1, i+2, ... , i+d mod N and i-1, i-2, ... , i-d mod N
    where d is the no. of clockwise neighbours.
    Each edge from i to j replaced with probability given with edge from i to randomly chosen k
    """
    # initialize empty graph
    ws_graph = nx.Graph()
    for vertex in range(num_nodes):
        ws_graph.add_node(vertex)

    # add each vertex to clockwise neighbours
    for vertex in range(num_nodes):  # consider each vertex
        for neighbour in range(vertex + 1, vertex + clockwise_neighbours + 1):  # consider each clockwise neighbour
            neighbour = neighbour % num_nodes  # correct node label if value too high
            ws_graph.add_edge(vertex, neighbour)

    # rewiring
    for vertex in range(num_nodes):  # consider each vertex
        for neighbour in range(vertex + 1, vertex + clockwise_neighbours + 1):  # consider each clockwise neighbour
            neighbour = neighbour % num_nodes  # correct node label if value too high
            random_number = random.random()  # generate random number
            if random_number < rewiring_prob:  # decide whether to rewire
                random_node = random.randint(0, num_nodes - 1)  # choose random node
                # make sure no loops or duplicates edges
                if random_node != vertex and random_node not in ws_graph[vertex]:
                    ws_graph.remove_edge(vertex, neighbour)
                    ws_graph.add_edge(vertex, random_node)

    return ws_graph

if __name__ == "__main__":
    ws_graph = make_ws_graph(50, 5, 0.6)

    num_of_edges = 0

    for node in ws_graph:
        num_of_edges += len(ws_graph[node])

    print(num_of_edges)
