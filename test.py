import networkx as nx

test = nx.Graph()
test.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 6), (2, 7), (7, 6), (6, 4), (2, 4), (3, 9), (3, 8)])

adjacency_matrix = nx.adjacency_matrix(test)

print(adjacency_matrix)

for vertex in [1]:
    for n in test[vertex]:
        if n not in [vertex]:
            for nn in test[n]:
                if nn not in [vertex, n]:
                    for nnn in test[nn]:
                        if nnn not in [vertex, n, nn]:
                            if adjacency_matrix[vertex, nnn]:
                                print(vertex, n, nn, nnn)

# test_vertex_nn = {}
#
# four_cycles = 0
#
#
# for n in test[1]:
#     test_vertex_nn[n] = [nn for nn in test[n]]
#     for n in test_vertex_nn:
#         for nn in test_vertex_nn[n]:
#             for n2 in test_vertex_nn:
#                 if nn in test_vertex_nn[n2]:
#                     print()
#                     four_cycles += 1

# print(four_cycles)