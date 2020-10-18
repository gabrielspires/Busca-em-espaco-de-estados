from funcs import find_start_points, find_neighbors, show_path

paths_found = []


def dls(mapa, graph, max_passos, node, path, max_depth, visited):
    if node not in visited:
        visited.append(node)

        # Max_passos--
        path[0] -= 1

        if mapa[node[0]][node[1]] == "#":
            path[1] += 1
            path[0] = max_passos

        if mapa[node[0]][node[1]] == "$":
            # print("Objetivo encontrado!")
            return path

        if max_depth <= 0:
            return

        for neighbour in graph[str(node)]:
            if path[0] <= 0 and mapa[neighbour[0]][neighbour[1]] != "#":
                continue
            new_path = list(path)
            new_path.append(neighbour)
            if valid_path := dls(
                mapa, graph, max_passos, neighbour, new_path, max_depth - 1, visited
            ):
                paths_found.append(valid_path)
                return valid_path

    return


def ids(mapa, max_passos):
    start_points = find_start_points(mapa)
    graph = find_neighbors(mapa)
    max_depth = len(graph)

    for node in start_points:
        for limit in range(max_depth):
            visited = []
            test = dls(mapa, graph, max_passos, node, [max_passos, 0, node], limit, visited)
            if test is not None:
                break

    shortest_path = paths_found[0]
    for path in paths_found:
        # print(path)
        if len(path) < len(shortest_path):
            shortest_path = path

    show_path(mapa, shortest_path)
    print(len(shortest_path) - 2, shortest_path[1], shortest_path[2])
