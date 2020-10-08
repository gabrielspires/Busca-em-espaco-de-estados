import sys
from bfs import bfs
from dfs import dfs
from ids import ids
from astar import a_star


def mostra_mapa(mapa):
    for linha in mapa:
        for caractere in linha:
            print(caractere, end="")
        print()


if __name__ == "__main__":
    largura_galpao, altura_galpao, max_passos = list(map(int, input().split()))
    mapa = []
    algoritmo = sys.argv[1]

    for linha in sys.stdin:
        mapa.append(list(linha[0:-1]))

    # mostra_mapa(mapa)

    if algoritmo == "BFS":
        bfs(mapa)
    elif algoritmo == "DFS":
        dfs(mapa)
    elif algoritmo == "IDS":
        ids(mapa)
    elif algoritmo == "A*":
        a_star(mapa)
