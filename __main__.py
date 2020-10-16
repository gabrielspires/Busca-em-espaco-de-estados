import argparse

from bfs import bfs
from dfs import dfs
from ids import ids
from astar import a_star

# from funcs import show_map

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-algoritmo", type=str, help="Algortimo de busca a usar")
    parser.add_argument("-entrada", type=str, help="Arquivo contendo o mapa")
    args = parser.parse_args()

    algoritmo = args.algoritmo.lower()
    mapa = []

    with open(args.entrada) as entrada:
        altura_galpao, largura_galpao, max_passos = list(map(int, entrada.readline().split()))
        for linha in entrada:
            mapa.append(list(linha[0:-1]))

    if algoritmo == "bfs":
        bfs(mapa, max_passos)
    elif algoritmo == "dfs":
        dfs(mapa, max_passos)
    elif algoritmo == "ids":
        ids(mapa, max_passos)
    elif algoritmo == "a_star":
        a_star(mapa, max_passos)

    # show_map(mapa)
