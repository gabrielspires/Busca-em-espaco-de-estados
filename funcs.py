from colorama import Back, Fore, Style


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


def find_start_points(mapa):
    start_points = []
    valid_points = [".", "#", "$"]
    largura_galpao = len(mapa[0])
    altura_galpao = len(mapa)

    # Primeira e última linha
    for i in range(largura_galpao):
        # Primeira e ultima linha
        if mapa[0][i] in valid_points:
            start_points.append([0, i])
        if mapa[altura_galpao - 1][i] in valid_points:
            start_points.append([altura_galpao - 1, i])

    for i in range(altura_galpao):
        # Primeira e ultima coluna
        if mapa[i][0] in valid_points:
            start_points.append([i, 0])
        if mapa[i][largura_galpao - 1] in valid_points:
            start_points.append([i, largura_galpao - 1])

    return start_points


def show_map(mapa):
    num_linha = 0
    num_coluna = 0
    print(3 * " ", end="")
    for _ in range(len(mapa[0])):
        print("{:<3}".format(num_coluna), end=" ")
        num_coluna += 1
    print()
    for linha in mapa:
        print(num_linha, end=" ")
        num_linha += 1
        for caractere in linha:
            print("{:<3}".format(caractere), end=" ")
        print()


def show_path(mapa, path):
    num_linha = 0
    num_coluna = 0
    print(3 * " ", end="")
    for _ in range(len(mapa[0])):
        print("{:<3}".format(num_coluna), end="")
        num_coluna += 1
    print()
    for i in range(len(mapa)):
        print("{:<3}".format(num_linha), end="")
        num_linha += 1
        for j in range(len(mapa[i])):
            if [i, j] in path:
                print(
                    Back.LIGHTWHITE_EX + Fore.BLACK + "{:<3}".format(mapa[i][j]),
                    end="",
                )
                print(Style.RESET_ALL, end="")
            else:
                print("{:<3}".format(mapa[i][j]), end="")
        print("")
    print()
