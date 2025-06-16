# main.py
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import os


def flood_fill(grid, x, y, color):
    n, m = len(grid), len(grid[0]) 
    if grid[x][y] != 0: # Verifica se a posição inicial precisa de preenchimento
        return

    queue = deque() # Usa deque para eficiência em operações FIFO (BFS)
    queue.append((x, y))
    grid[x][y] = color

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Direções: cima, baixo, esquerda, direita (4-vizinhança)

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                grid[nx][ny] = color
                queue.append((nx, ny))


def fill_all_regions(grid, start_x, start_y):
    grid = [row[:] for row in grid]
    color = 2
    if grid[start_x][start_y] == 0:
        flood_fill(grid, start_x, start_y, color)
        color += 1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                flood_fill(grid, i, j, color)
                color += 1
    return grid

def plot_grid(grid, title="Grid"):
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib
    import os

    grid_np = np.array(grid)
    cmap = plt.cm.get_cmap('hot', np.max(grid_np) + 1)

    fig, ax = plt.subplots()
    ax.matshow(grid_np, cmap=cmap)

    n, m = grid_np.shape
    ax.set_xticks(np.arange(m))
    ax.set_yticks(np.arange(n))
    ax.set_xticklabels(range(m))
    ax.set_yticklabels(range(n))
    ax.set_xlabel("Colunas")
    ax.set_ylabel("Linhas")
    ax.set_title(title)
    plt.grid(True)

    if matplotlib.get_backend() in ["TkAgg", "QtAgg", "MacOSX"]:
        plt.show()
    else:
        output_file = f"{title}.png"
        plt.savefig(output_file)
        print(f"[INFO] Salvou imagem: {output_file}")
    plt.close(fig)




def main():
    grid = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0],
    ]
    start_x, start_y = 0, 0
    print("Grid original:")
    plot_grid(grid, "Entrada")
    filled = fill_all_regions(grid, start_x, start_y)
    print("Grid preenchido:")
    plot_grid(filled, "Saída")


if __name__ == "__main__":
    main()
