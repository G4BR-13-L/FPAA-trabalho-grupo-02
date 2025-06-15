
# FPAA-trabalho-grupo-01 - A* Path Finder

## GRUPO
- Gabriel Victor Couto Martins de Paula
- Luís Antônio de Souza e Sousa

--- 

# A* Path Finder em Labirinto 2D

Este projeto implementa o **Algoritmo A\*** para encontrar o menor caminho entre dois pontos em um labirinto 2D. O algoritmo considera obstáculos, utiliza a **distância de Manhattan como heurística** e garante a solução mais eficiente, se existir.

---

## 🧩 Problema Resolvido

Dado um labirinto 2D representado como uma matriz com células livres (`0`), obstáculos (`1`), um ponto de início (`S`) e um ponto final (`E`), o objetivo é encontrar o caminho mais curto entre `S` e `E` utilizando o Algoritmo A\*.

Se não houver caminho possível, o programa retorna `"Nenhum caminho encontrado"`.

---

## 🔍 Funcionamento do Algoritmo A\*

O **Algoritmo A\*** é uma estratégia de busca heurística que combina dois fatores:

- **g(n)**: o custo do caminho percorrido do início até o nó `n`.
- **h(n)**: a estimativa do custo restante até o destino — neste caso, calculado com **distância de Manhattan**:

  \[
  h(n) = |x_1 - x_2| + |y_1 - y_2|
  \]

O algoritmo escolhe os caminhos com menor valor total `f(n) = g(n) + h(n)`, priorizando movimentos promissores.

O labirinto é explorado em quatro direções (cima, baixo, esquerda, direita), ignorando obstáculos (`1`).

---

## ▶️ Como Executar o Projeto

### Requisitos

- Python 3.7+
- `pip` instalado

### 1. Acessar o Diretório do Projeto  
```bash
cd flood_fill_python
````

### 2. Criar e Ativar um Ambiente Virtual Python

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o Projeto

```bash
python3 main.py
```

---

## 🐳 Executar com Docker (Opcional)

Executa os testes automaticamente usando ambientes isolados:

```bash
sudo docker compose up --build -d
```

---

## ✅ Validações Importantes

* O programa verifica se há um ponto de início `S` e um fim `E`.
* Caso o caminho seja impossível (devido a obstáculos), o algoritmo retorna: `Nenhum caminho encontrado.`

---

## 💡 Exemplo de Entrada

```python
labirinto = [
    ['S', '0', '1', '0', '0'],
    ['0', '0', '1', '0', '1'],
    ['1', '0', '1', '0', '0'],
    ['1', '0', '0', 'E', '1'],
]
```

## 🔎 Saída Esperada

```
Labirinto com caminho:
S * 1 0 0
0 * 1 0 1
1 * 1 0 0
1 * * E 1
```

---

## 📁 Estrutura do Projeto

```
.
├── ci_docker.sh
├── clean_docker.sh
├── docker-compose.yml
├── Dockerfile.python
├── Dockerfile.rust
├── img
│   ├── grafo_python.png
│   └── grafo_rust.png
├── flood_fill_python
│   ├── main.py
│   ├── __pycache__
│   ├── requirements.txt
│   ├── test_flood_fill.py
│   └── venv
├── flood_fill_rust
│   ├── Cargo.lock
│   ├── Cargo.toml
│   ├── README.md
│   ├── src
│   └── target
├── pseudocodigo.txt
├── README.md
├── test.sh
└── Trabalho em grupo 1 - Valor 10 pontos-1-1.pdf

```
