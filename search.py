import networkx as nx
import random
import collections
import nx_group_graph as group_graph_gen
import time
import pickle
import matplotlib


def random_search(pairs):
    nx_random_graph = nx.erdos_renyi_graph(1559, 0.0337)
    random_graph = nx.to_dict_of_lists(nx_random_graph)

    pair_steps = 0

    for i in range(pairs):
        current, goal = random.sample(random_graph.keys(), 2)

        deque = collections.deque()
        deque.append(current)
        seen = set()

        while current != goal:
            current = deque.pop()

            if goal in random_graph[current]:
                current = goal
            else:
                deque.extend([neighbour for neighbour in random_graph[current] if neighbour not in seen])
                for neighbour in random_graph[current]:
                    seen.add(neighbour)

            pair_steps += 1

    avg_pair_steps = pair_steps/pairs

    return avg_pair_steps


def group_search(pairs):
    m, k, p, q = 75, 20, 0.3, 0.033
    nx_group_graph = group_graph_gen.create_group_graph(m, k, p, q)
    print(nx_group_graph.number_of_nodes())
    print(nx_group_graph.number_of_edges())
    group_graph = nx.to_dict_of_lists(nx_group_graph)

    pair_steps = 0

    expected_inter_group_edges = p * k * ((k - 1)/2) * m
    expected_intra_group_edges = q * m * k * ((m - 1)/2) * k

    if expected_inter_group_edges > expected_intra_group_edges:
        for i in range(pairs):
            current, goal = random.sample(group_graph.keys(), 2)
            deque = collections.deque()
            deque.append(current)
            seen = set()
            goal_group = goal // k

            while current != goal:
                current = deque.pop()

                if goal in group_graph[current]:
                    current = goal
                else:
                    deque.extend([neighbour for neighbour in group_graph[current] if (neighbour not in seen and not
                        neighbour // k == goal_group)])

                    if len(deque) == 0:
                        deque.extend([neighbour for neighbour in group_graph[current] if neighbour not in seen])

                    for neighbour in group_graph[current]:
                        seen.add(neighbour)

                pair_steps += 1

    else:
        for i in range(pairs):
            current, goal = random.sample(group_graph.keys(), 2)
            deque = collections.deque()
            deque.append(current)
            seen = set()
            goal_group = goal // k

            while current != goal:
                current = deque.pop()

                if goal in group_graph[current]:
                    current = goal
                else:
                    deque.extend([neighbour for neighbour in group_graph[current] if (neighbour not in seen and
                        neighbour // k == goal_group)])

                    if len(deque) == 0:
                        deque.extend([neighbour for neighbour in group_graph[current] if neighbour not in seen])

                    for neighbour in group_graph[current]:
                        seen.add(neighbour)

                pair_steps += 1

    avg_pair_steps = pair_steps / pairs

    return avg_pair_steps


if __name__ == "__main__":

    print(group_search(10))

    # step_avgs_1000 = []
    #
    # for i in range(1000):
    #     print(i)
    #     step_avgs_1000.append(random_search(1000))
    #
    # with open('random_search_dfs_1000', 'wb') as fp:
    #     pickle.dump(step_avgs_1000, fp)

    # with open('random_search_dfs_1000', 'rb') as fp:
    #     step_avgs_1000 = pickle.load(fp)
    #
    # matplotlib.pyplot.hist(step_avgs_1000, 20, normed=1, facecolor='red', alpha=1)
    # matplotlib.pyplot.show()

    #     result = random_search(100)
    #     with open('random_search_dfs_backtrack_100_' + str(i), 'wb') as fp:
    #         pickle.dump(result, fp)

    # instance_averages = []
    # for i in range(100):
    #     with open('random_search_dfs_backtrack_100_' + str(i), 'rb') as fp:
    #         result_100 = pickle.load(fp)
    #         avg = 0
    #         for result in result_100:
    #             avg += result
    #         instance_averages.append(avg/100)
    #
    # matplotlib.pyplot.hist(instance_averages)
    # matplotlib.pyplot.show()

    # with open('random_search_dfs_backtrack', 'rb') as fp:
    #     result_1000 = pickle.load(fp)
    #     avg = 0
    #     for result in result_1000:
    #         avg += result
    #     print(avg/1000)
    #
    # with open('random_search_dfs_backtrack_100', 'rb') as fp:
    #     result_100 = pickle.load(fp)
    #     avg = 0
    #     for result in result_100:
    #         avg += result
    #     print(avg/100)