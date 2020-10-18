from funcs import find_start_points, find_neighbors

paths_found = []


def dfs_search(mapa, graph, max_passos, visited, node, path):
    if node not in visited:
        visited.append(node)
        path[0] -= 1

        if mapa[node[0]][node[1]] == "#":
            path[1] += 1
            path[0] = max_passos

        if mapa[node[0]][node[1]] == "$":
            # print("Objetivo encontrado!")
            return path

        for neighbour in graph[str(node)]:
            if path[0] <= 0 and mapa[neighbour[0]][neighbour[1]] != "#":
                continue
            new_path = list(path)
            new_path.append(neighbour)
            if valid_path := dfs_search(mapa, graph, max_passos, visited, neighbour, new_path):
                paths_found.append(valid_path)


def dfs(mapa, max_passos):
    start_points = find_start_points(mapa)
    graph = find_neighbors(mapa)

    for node in start_points:
        visited = []
        dfs_search(mapa, graph, max_passos, visited, node, [max_passos, 0, node])

    shortest_path = paths_found[0]
    for path in paths_found:
        # print(path, end="\n\n")
        if len(path) < len(shortest_path):
            shortest_path = path

    print(len(shortest_path) - 2, shortest_path[1], shortest_path[2])
    return shortest_path
