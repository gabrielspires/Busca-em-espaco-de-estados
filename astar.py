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
    queue = []
    # Initialize open and close lists
    open_list = []
    close_list = []
    pts_loc_visitados = 0
    for entrance in start_points:
        # Put the starting point on the open list with f=0
        open_list.clear()
        close_list.clear()
        open_list.append([0, 0, 0, entrance])

        queue.clear()
        passos_restantes = max_passos
        pts_loc_visitados = 0
        queue.append([passos_restantes, pts_loc_visitados, entrance])

        while open_list:
            # find the node with the least f on the open list
            q = open_list[0]
            for node in open_list:
                if node[0] < q[0]:
                    q = node
            open_list.remove(q)

            for neighbor in graph[str(q[3])]:
                if mapa[neighbor[0]][neighbor[1]] == "$":
                    print("Objetivo encontrado! Posição:", neighbor)
                    return
                if mapa[neighbor[0]][neighbor[1]] == "#":
                    pts_loc_visitados += 1

                g = q[1] + 1
                h = manhattan_distance(neighbor, goal)
                f = g + h
                successor = [f, g, h, neighbor]
                openlist_have_better_node = False
                closelist_have_better_node = False
                for node in open_list:
                    if node[3] == neighbor and node[0] < f:
                        openlist_have_better_node = True
                for node in close_list:
                    if node[3] == neighbor and node[0] < f:
                        closelist_have_better_node = True
                if openlist_have_better_node or closelist_have_better_node:
                    continue
                else:
                    open_list.append(successor)
            close_list.append(q)
            # print(open_list, pts_loc_visitados)
