import heapq
from typing import List, Optional, Tuple, Dict, Set
from dataclasses import dataclass, field


@dataclass(order=True, unsafe_hash=True)
class Pos:
    x: int
    y: int


@dataclass(order=True)
class Node:
    priority: int
    pos: Pos = field(compare=False)


def heuristica(a: Pos, b: Pos) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


def encontrar_posicao(labirinto: List[List[str]], alvo: str) -> Optional[Pos]:
    for x, linha in enumerate(labirinto):
        for y, celula in enumerate(linha):
            if celula == alvo:
                return Pos(x, y)
    return None


def vizinhos_validos(pos: Pos, labirinto: List[List[str]]) -> List[Pos]:
    vizinhos = []
    direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    linhas = len(labirinto)
    colunas = len(labirinto[0]) if linhas > 0 else 0

    for dx, dy in direcoes:
        nx, ny = pos.x + dx, pos.y + dy
        if 0 <= nx < linhas and 0 <= ny < colunas:
            if labirinto[nx][ny] != '1':
                vizinhos.append(Pos(nx, ny))

    print(f"Vizinhos de ({pos.x}, {pos.y}): {[ (v.x, v.y) for v in vizinhos ]}")
    return vizinhos


def reconstruir_caminho(atual: Pos, veio_de: Dict[Pos, Pos]) -> List[Pos]:
    caminho = [atual]
    while atual in veio_de:
        atual = veio_de[atual]
        caminho.append(atual)
    caminho.reverse()
    return caminho


def a_estrela(labirinto: List[List[str]]) -> Optional[List[Pos]]:
    inicio = encontrar_posicao(labirinto, 'S')
    fim = encontrar_posicao(labirinto, 'E')

    if inicio is None or fim is None:
        return None

    open_set = []
    heapq.heappush(open_set, Node(0, inicio))

    g_score: Dict[Pos, int] = {inicio: 0}
    f_score: Dict[Pos, int] = {inicio: heuristica(inicio, fim)}
    veio_de: Dict[Pos, Pos] = {}

    while open_set:
        atual = heapq.heappop(open_set).pos
        if atual == fim:
            return reconstruir_caminho(atual, veio_de)

        for vizinho in vizinhos_validos(atual, labirinto):
            tentativa_g = g_score.get(atual, float('inf')) + 1
            if tentativa_g < g_score.get(vizinho, float('inf')):
                veio_de[vizinho] = atual
                g_score[vizinho] = tentativa_g
                f = tentativa_g + heuristica(vizinho, fim)
                f_score[vizinho] = f
                heapq.heappush(open_set, Node(f, vizinho))

    return None


def imprimir_labirinto_com_caminho(labirinto: List[List[str]], caminho: List[Pos]):
    labirinto_mod = [linha.copy() for linha in labirinto]
    for pos in caminho:
        if labirinto_mod[pos.x][pos.y] not in ('S', 'E'):
            labirinto_mod[pos.x][pos.y] = '*'

    for linha in labirinto_mod:
        print(' '.join(linha))


def main():
    labirinto = [
        ['S', '0', '1', '0', '0'],
        ['0', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '0'],
        ['1', '0', '0', 'E', '1'],
    ]

    caminho = a_estrela(labirinto)
    if caminho:
        print("Caminho encontrado:")
        for pos in caminho:
            print(f"({pos.x},{pos.y})")
        print("\nLabirinto com caminho:")
        imprimir_labirinto_com_caminho(labirinto, caminho)
    else:
        print("Nenhum caminho encontrado.")


if __name__ == "__main__":
    main()
