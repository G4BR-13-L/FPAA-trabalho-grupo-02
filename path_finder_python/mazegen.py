from numpy import random

def mazegen():
    step01 = mazestart()

    maze = [step01] + mazemiddle(step01)

    maze.append(mazend(maze))

    return maze

def rowgen():
        row = []
        for i in range(5):
            if i in [0, 4]:
                val = '0' if random.random() < 0.85 else '1'  # 85% de chance de 0
            else:
                val = '0' if random.random() < 0.7 else '1'  # 70% de chance de 0
            row.append(val)
        return row

def mazestart():
    start = ['S']

    for i in range(4):
        if i == 0:  # Primeira posição após o 'S'
            # 80 de chance de ser caminho livre (0)
            start.append('0' if random.random() < 0.8 else '1')
        elif i == 3:  # Última posição do array
            # 70% de chance de ser caminho livre (0)
            start.append('0' if random.random() < 0.7 else '1')
        else:  # Posições intermediárias
            # 60% de chance de ser caminho livre (0)
            start.append('0' if random.random() < 0.6 else '1')
    
    # Garante pelo menos um caminho livre na linha inicial
    if '0' not in start[1:]:
        start[random.randint(1, 4)] = '0'

    return start

def mazemiddle(start):
    # Gera arr01 baseado no start
    if start[1] == '1':
        arr01 = ['0', '0'] + [str(random.randint(0, 1)) for _ in range(3)]
    else:
        arr01 = ['1', '0'] + [str(random.randint(0, 1)) for _ in range(3)]

    return [arr01, rowgen(), rowgen()]

def mazend(maze):
    last_row = maze[-1]
    exit_row = ['0'] * 5
    valid_positions = [i for i, val in enumerate(last_row) if val == '0']
    
    if not valid_positions:
        valid_positions = [random.randint(0, 4)]
    
    exit_pos = random.choice(valid_positions)
    
    for i in range(5):
        if i == exit_pos:
            exit_row[i] = 'E'
        else:
            exit_row[i] = '0' if random.random() < 0.8 else '1'
    
    return exit_row