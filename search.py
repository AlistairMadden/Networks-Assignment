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

    pair_steps = []

    for i in range(pairs):
        start, goal = random.sample(random_graph.keys(), 2)
        seen_nodes = set()
        stack = collections.deque()
        stack.append((start, None))
        path = []

        while len(stack) > 0:
            current_node, current_parent = stack.pop()
            path.append(current_node)

            if current_node == goal:
                break

            unvisited_nodes = 0

            for neighbour_node in random_graph[current_node]:
                if neighbour_node not in seen_nodes:
                    seen_nodes.add(neighbour_node)
                    stack.append((neighbour_node, current_node))

                if neighbour_node not in path:
                    unvisited_nodes += 1

            # all neighbours already visited --> move to next node in stack's parent
            if unvisited_nodes == 0:
                backtrack_to = stack.pop()
                path_index = -2
                backtrack_list = []
                while not backtrack_to[1] == current_node:
                    current_node = path[path_index]
                    backtrack_list.append(current_node)
                    path_index -= 1
                path.append(backtrack_list)
                stack.append(backtrack_to)

        pair_steps.append(len(path))

    return pair_steps


def group_search(pairs):
    m, k, p, q = 75, 20, 0.3, 0.033
    nx_group_graph = group_graph_gen.create_group_graph(m, k, p, q)
    group_graph = nx.to_dict_of_lists(nx_group_graph)

    pair_steps = []

    # Group graph is intra-group dominated
    if (q * ((m - 1) * k)) > (p * (k - 1)):
        for i in range(pairs):
            start, goal = random.sample(group_graph.keys(), 2)
            print(start)
            print(goal)
            seen_nodes = set()
            stack = collections.deque()
            stack.append((start, None))
            path = []
            goal_node_group = goal / k

            while len(stack) > 0:
                current_node, current_parent = stack.pop()
                path.append(current_node)

                if current_node == goal:
                    break

                unvisited_nodes = 0

                for neighbour_node in group_graph[current_node]:
                    if neighbour_node not in seen_nodes and (neighbour_node / k != goal_node_group):
                        seen_nodes.add(neighbour_node)
                        stack.append((neighbour_node, current_node))

                    if neighbour_node not in path:
                        unvisited_nodes += 1

                # all neighbours already visited --> move to next node in stack's parent
                if unvisited_nodes == 0:
                    for neighbour_node in group_graph[current_node]:
                        if neighbour_node not in seen_nodes:
                            seen_nodes.add(neighbour_node)
                            stack.append((neighbour_node, current_node))

                        if neighbour_node not in path:
                            unvisited_nodes += 1

                    if(unvisited_nodes == 0):
                        backtrack_to = stack.pop()
                        path_index = -2
                        backtrack_list = []
                        while not backtrack_to[1] == current_node:
                            current_node = path[path_index]
                            backtrack_list.append(current_node)
                            path_index -= 1
                        path.append(backtrack_list)
                        stack.append(backtrack_to)

            print("completed one")
            pair_steps.append(len(path))


    # pair_steps = []
    #
    # for i in range(pairs):
    #     start, goal = random.sample(group_graph.keys(), 2)
    #     seen_nodes = set()
    #     q = queue.Queue()
    #     q.put(start)
    #     steps = 0
    #     goal_group = goal/k     # number between 0 and 74 indicating the group of the goal node
    #
    #     while not q.empty():
    #         current_node = q.get()
    #
    #         if current_node == goal:
    #             break
    #
    #         neighbour_node_is_goal = False
    #
    #         for neighbour_node in group_graph[current_node]:
    #             if neighbour_node == goal:
    #                 neighbour_node_is_goal = True
    #                 steps += 1
    #                 break
    #
    #         if neighbour_node_is_goal:
    #             break
    #
    #         neighbour_node_is_in_goal_group = False
    #
    #         for neighbour_node in group_graph[current_node]:
    #             if neighbour_node/k == goal_group:
    #                 neighbour_node_is_in_goal_group = True
    #                 steps += 1
    #                 q.put(neighbour_node)
    #                 break
    #
    #         if neighbour_node_is_in_goal_group:
    #             continue
    #
    #         # No neighbours have been found in the goal group
    #
    #         q.put
    #
    # return group_graph


if __name__ == "__main__":

    print(group_search(20))

    # for i in range(100):
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