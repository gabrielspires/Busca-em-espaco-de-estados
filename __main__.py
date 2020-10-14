import argparse

from bfs import bfs
from dfs import dfs
from ids import ids
from astar import a_star
from funcs import show_map, find_start_points, find_neighbors

from pprint import pp

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-algoritmo", type=str, help="Algortimo de busca a usar")
    parser.add_argument("-entrada", type=str, help="Arquivo contendo o mapa")
    args = parser.parse_args()

    algoritmo = args.algoritmo
    mapa = []

    with open(args.entrada) as entrada:
        altura_galpao, largura_galpao, max_passos = list(map(int, entrada.readline().split()))
        for linha in entrada:
            mapa.append(list(linha[0:-1]))

    # show_map(mapa)
    start_points = find_start_points(mapa, largura_galpao, altura_galpao)
    # print("Starting points: ", start_points)
    # pp(find_neighbors(mapa))

    if algoritmo == "BFS":
        bfs(mapa, max_passos, altura_galpao, largura_galpao)
    elif algoritmo == "DFS":
        dfs(mapa, max_passos, altura_galpao, largura_galpao)
    elif algoritmo == "IDS":
        ids(mapa, max_passos, altura_galpao, largura_galpao)
    elif algoritmo == "A*":
        a_star(mapa, max_passos, altura_galpao, largura_galpao)
