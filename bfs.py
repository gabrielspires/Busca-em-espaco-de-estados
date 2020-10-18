from funcs import find_start_points, find_neighbors, show_path


def bfs(mapa, max_passos):
    start_points = find_start_points(mapa)
    graph = find_neighbors(mapa)
    visited = []
    queue = []

    paths = []

    for entrance in start_points:
        passos_restantes = max_passos
        visited.clear()
        queue.clear()
        pts_loc_visitados = 0

        visited.append(entrance)
        queue.append([passos_restantes, pts_loc_visitados, entrance])

        while queue:
            path = queue.pop(0)
            node = path[-1]
            path[0] -= 1

            if mapa[node[0]][node[1]] == "#":
                path[1] += 1
                path[0] = max_passos

            if mapa[node[0]][node[1]] == "$":
                # Objetivo encontrado!
                paths.append(path)
                break

            for neighbor in graph[str(node)]:
                if path[0] <= 0 and mapa[neighbor[0]][neighbor[1]] != "#":
                    continue
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    visited.append(neighbor)
                    queue.append(new_path)

    shortest_path = paths[0]
    for path in paths:
        # print(path, len(path) - 2, end="\n\n\n")
        if len(path) < len(shortest_path):
            shortest_path = path

    print(len(shortest_path) - 2, shortest_path[1], shortest_path[2])
    # show_path(mapa, shortest_path)
    return shortest_path
