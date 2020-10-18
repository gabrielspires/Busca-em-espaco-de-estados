import argparse

from bfs import bfs
from dfs import dfs
from ids import ids
from astar import a_star
from funcs import show_path

# from funcs import show_map

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-algoritmo", type=str, help="Algortimo de busca a usar")
    parser.add_argument("-entrada", type=str, help="Arquivo contendo o mapa")
    parser.add_argument("-map", type=str, help="Mostra o caminho encontrado (True/False)")
    args = parser.parse_args()
    if args.map is None:
        args.map = "false"

    algoritmo = args.algoritmo.lower()
    mapa = []

    with open(args.entrada) as entrada:
        altura_galpao, largura_galpao, max_passos = list(map(int, entrada.readline().split()))
        for linha in entrada:
            mapa.append(list(linha[0:-1]))

    import time

    start = time.time()
    if algoritmo == "bfs":
        path = bfs(mapa, max_passos)
        if args.map.lower() == "true":
            show_path(mapa, path)
    elif algoritmo == "dfs":
        path = dfs(mapa, max_passos)
        if args.map.lower() == "true":
            show_path(mapa, path)
    elif algoritmo == "ids":
        path = ids(mapa, max_passos)
        if args.map.lower() == "true":
            show_path(mapa, path)
    elif algoritmo == "a_star":
        a_star(mapa, max_passos)

    end = time.time()
    # print(algoritmo + ", " + args.entrada.split("/")[-1] + ", " + str(end - start))
