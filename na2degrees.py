#na2degrees.py
#matthew johnson 18 january 2017


#####################################################

"""
We will define graphs as dictionaries where the keys are the nodes and the
values are sets containing all neighbours.  Here is an example digraph (we
can define graphs in the same way --- just need to ensure symmetry)
"""

###################################################

EXAMPLE = {0: set([1, 4, 5, 8]),
           1: set([4, 6]),
           2: set([3, 7, 9]),
           3: set([7]),
           4: set([2]),
           5: set([1]),
           6: set([]),
           7: set([3]),
           8: set([1, 2]),
           9: set([0 ,3, 4, 5, 6, 7])}

def compute_in_degrees(digraph):
    """Takes a directed graph and computes the in-degrees for the nodes in the
    graph. Returns a dictionary with the same set of keys (nodes) and the
    values are the in-degrees."""
    #initialize in-degrees dictionary with zero values for all vertices
    in_degree = {}
    for vertex in digraph:
        in_degree[vertex] = 0
    #consider each vertex
    for vertex in digraph:
        #amend in_degree[w] for each outgoing edge from v to w
        for neighbour in digraph[vertex]:
            in_degree[neighbour] += 1
    return in_degree

def in_degree_distribution(digraph):
    """Takes a directed graph and computes the unnormalized distribution of the
    in-degrees of the graph.  Returns a dictionary whose keys correspond to
    in-degrees of nodes in the graph and values are the number of nodes with
    that in-degree. In-degrees with no corresponding nodes in the graph are not
    included in the dictionary."""
    #find in_degrees
    in_degree = compute_in_degrees(digraph)
    #initialize dictionary for degree distribution
    degree_distribution = {}
    #consider each vertex
    for vertex in in_degree:
        #update degree_distribution
        if in_degree[vertex] in degree_distribution:
            degree_distribution[in_degree[vertex]] += 1
        else:
            degree_distribution[in_degree[vertex]] = 1
    return degree_distribution


def compute_degrees(digraph):
    """Takes a directed graph and computes the degrees for the nodes in the
    graph. Returns a dictionary with the same set of keys (nodes) and the
    values are the degrees."""
    # initialize degrees dictionary with zero values for all vertices
    degree = {}
    for vertex in digraph:
        degree[vertex] = 0
    # consider each vertex
    for vertex in digraph:
        # amend degree[vertex] for each vertex. digraph[vertex] gives a list of neighbouring vertices
        for neighbour in digraph[vertex]:
            degree[vertex] += 1
    return degree


def degree_distribution(digraph):
    """Takes a directed graph and computes the unnormalized distribution of the
    in-degrees of the graph.  Returns a dictionary whose keys correspond to
    in-degrees of nodes in the graph and values are the number of nodes with
    that in-degree. In-degrees with no corresponding nodes in the graph are not
    included in the dictionary."""
    # find_degrees
    degree = compute_degrees(digraph)
    # initialize dictionary for degree distribution
    degree_distribution = {}
    # consider each vertex
    for vertex in degree:
        # update degree_distribution
        if degree[vertex] in degree_distribution:
            degree_distribution[degree[vertex]] += 1
        else:
            degree_distribution[degree[vertex]] = 1
    return degree_distribution

# if __name__ == "__main__":
#     citation_graph = na2loadgraph.load_graph("alg_phys-cite.txt")
#     citation_in_degrees = compute_in_degrees(citation_graph)
#     citation_in_degree_distribution = in_degree_distribution(citation_graph)
#     maximum_key = 0
#     maximum_value = 0
#     for key in citation_in_degrees:
#         if citation_in_degrees[key] > maximum_value:
#             maximum_key = key
#             maximum_value = citation_in_degrees[key]
#     print("node = " + str(maximum_key) + " referred " + str(citation_in_degrees[maximum_key]) + " times")
#     print(citation_in_degree_distribution)
