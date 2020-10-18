from funcs import find_start_points, find_neighbors, show_path


def goal_location(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == "$":
                return [i, j]


def manhattan_distance(node, goal):
    # [2,5] -> [0,10] abs
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def a_star(mapa, max_passos):
    goal = goal_location(mapa)
    start_points = find_start_points(mapa)
    graph = find_neighbors(mapa)

    paths = []

    # Initialize open and close lists
    open_list = []
    close_list = []
    pts_loc_visitados = 0
    for entrance in start_points:
        passos_restantes = max_passos
        passos = 0
        open_list.clear()
        close_list.clear()
        pts_loc_visitados = 0

        goal_is_found = False
        # Put the starting point on the open list with f=0
        open_list.append([0, 0, 0, passos_restantes, pts_loc_visitados, passos, entrance, entrance])

        while open_list:
            # find the node with the least f on the open list
            q = open_list[0]
            for node in open_list:
                if node[0] < q[0]:
                    q = node
            open_list.remove(q)
            q[3] -= 1
            if goal_is_found:
                # print(q, entrance)
                break

            # return
            # print(q[-2])
            if mapa[q[-1][0]][q[-1][1]] == "#":
                q[5] += 1
                q[4] += 1
                q[3] = max_passos
                # print(q[-1][0], q[-1][1])
            elif mapa[q[-1][0]][q[-1][1]] == "$":
                q[5] += 1
                # print("Objetivo encontrado! Posição:", q[5], q[4], q[-2])
                paths.append(q)
                goal_is_found = True
            else:
                q[5] += 1

            for neighbor in graph[str(q[-1])]:

                if q[3] <= 0 and mapa[neighbor[0]][neighbor[1]] != "#":
                    continue

                g = q[1] + 1
                h = manhattan_distance(neighbor, goal)
                f = g + h
                successor = [f, g, h, q[3], q[4], q[5], q[-2], neighbor]
                openlist_have_better_node = False
                closelist_have_better_node = False
                for node in open_list:
                    if node[-1] == neighbor and node[0] < f:
                        openlist_have_better_node = True
                for node in close_list:
                    if node[-1] == neighbor and node[0] < f:
                        closelist_have_better_node = True
                if openlist_have_better_node or closelist_have_better_node:
                    continue
                else:
                    open_list.append(successor)
            close_list.append(q)
            # print(open_list, pts_loc_visitados)

    shortest_path = paths[0]
    for solution in paths:
        # print(solution[5], shortest_path[5])
        # print(path, len(path) - 2, end="\n\n\n")
        if solution[5] < shortest_path[5]:
            shortest_path = solution

    print(shortest_path[5], shortest_path[4], shortest_path[-2])
