def find_neighbors(mapa):
    graph = {}
    valid_points = [".", "#", "$"]

    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] in valid_points:
                node = str([i, j])
                graph[node] = []

                up_neighbor = [i - 1, j]
                down_neighbor = [i + 1, j]
                left_neighbor = [i, j - 1]
                right_neighbor = [i, j + 1]

                if i != 0 and mapa[up_neighbor[0]][up_neighbor[1]] in valid_points:
                    graph[node].append(up_neighbor)
                if i < len(mapa) - 1 and mapa[down_neighbor[0]][down_neighbor[1]] in valid_points:
                    graph[node].append(down_neighbor)
                if j != 0 and mapa[left_neighbor[0]][left_neighbor[1]] in valid_points:
                    graph[node].append(left_neighbor)
                if (
                    j < len(mapa[i]) - 1
                    and mapa[right_neighbor[0]][right_neighbor[1]] in valid_points
                ):
                    graph[node].append(right_neighbor)

    return graph


def find_start_points(mapa, largura_galpao, altura_galpao):
    start_points = []
    valid_points = [".", "#", "$"]

    # Primeira e última linha
    for i in range(largura_galpao):
        if mapa[0][i] in valid_points:
            start_points.append([0, i])
        if mapa[altura_galpao - 1][i] in valid_points:
            start_points.append([altura_galpao - 1, i])

    for i in range(altura_galpao):
        if mapa[i][0] in valid_points:
            start_points.append([i][0])
        if mapa[i][largura_galpao - 1] in valid_points:
            start_points.append([i, largura_galpao - 1])

    return start_points


def show_map(mapa):
    num_linha = 0
    num_coluna = 0
    print(3 * " ", end="")
    for _ in range(len(mapa[0])):
        print("{:<2}".format(num_coluna), end=" ")
        num_coluna += 1
    print()
    for linha in mapa:
        print(num_linha, end="  ")
        num_linha += 1
        for caractere in linha:
            print("{:<2}".format(caractere), end=" ")
        print()
