from funcs import find_start_points, find_neighbors


def bfs(mapa, max_passos, altura_galpao, largura_galpao):
    start_points = find_start_points(mapa, largura_galpao, altura_galpao)
    graph = find_neighbors(mapa)
    visited = []
    queue = []

    paths = []

    for entrance in start_points:
        passos_restantes = max_passos
        passos_dados = 0
        visited.clear()
        queue.clear()

        visited.append(entrance)
        queue.append([passos_restantes, entrance])
        # print(entrance)
        while queue:
            path = queue.pop(0)
            node = path[-1]
            path[0] -= 1
            # print(visited, path[0])
            # if path[0] < 0:
            #     # if len(path) > 2:
            #     #     visited.remove(path[-1])
            #     #     visited.remove(path[-2])
            #     # else:
            #     #     visited.remove(path[-1])
            #     print("VOLTA")
            #     continue

            if mapa[node[0]][node[1]] == "#":
                path[0] = max_passos
            # print(mapa[s[0]][s[1]], end="")
            if mapa[node[0]][node[1]] == "$":
                # print()
                print("Objetivo encontrado!")
                paths.append(path)
                break

            for neighbor in graph[str(node)]:
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    visited.append(neighbor)
                    queue.append(new_path)

    for jooj in paths:
        print(jooj)
