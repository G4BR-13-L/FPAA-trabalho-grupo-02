
# FPAA-trabalho-grupo-02 - Flood Fill
> Mapeamento de Regiões com Obstáculos

## GRUPO
- Gabriel Victor Couto Martins de Paula
- Luís Antônio de Souza e Sousa

---

## 📌 Descrição

Este projeto implementa o **Algoritmo Flood Fill** para identificação e preenchimento automático de **regiões conectadas** em um **terreno 2D**, representado como um grid de células.

O objetivo é simular um sistema de mapeamento inteligente, utilizado por **robôs autônomos**, que precisam identificar áreas navegáveis separadas por obstáculos, preenchendo-as com cores distintas para posterior análise e navegação.

---

## 🔍 Problema Resolvido

Dado um grid 2D onde:

- `0` representa **espaço livre** (navegável)
- `1` representa **obstáculos** (paredes, barreiras)
- `2, 3, 4,...` representam **regiões já preenchidas**

O algoritmo deve:

1. Identificar a **região conectada** à partir de uma **posição inicial (x, y)**.
2. Preencher essa região com uma **cor numérica única**.
3. Repetir o processo para todas as demais regiões livres do grid, utilizando cores incrementais.

O preenchimento respeita obstáculos e apenas considera conexões **ortogonais** (cima, baixo, esquerda, direita).

---

## 💡 Funcionamento do Algoritmo Flood Fill

O **Flood Fill** é um algoritmo de propagação em **largura** ou **profundidade**, semelhante ao usado em editores gráficos para preencher áreas com uma cor.

### Etapas:

1. Começa a partir da célula inicial `(x, y)`.
2. Verifica se ela é um espaço livre (`0`).
3. Se for, colore com uma nova cor (ex: `2`) e coloca na fila.
4. Itera sobre seus vizinhos ortogonais (não diagonais).
5. Se o vizinho for `0`, colore com a mesma cor e adiciona à fila.
6. Repete até esvaziar a fila.
7. Após preencher a primeira região, o algoritmo busca por outros `0`s no grid e repete o processo com cores crescentes.

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

O resultado será salvo automaticamente como imagens:

* `Entrada.png` — o grid original
* `Saída.png` — o grid com as regiões preenchidas em cores

---

## 🐳 Executar com Docker (Opcional)

Executa os testes automaticamente usando ambientes isolados:

```bash
sudo docker compose up --build -d
```

---

## 📸 Exemplos

### 🧪 Exemplo 1

#### Grid de Entrada:

```
0 0 1 0 0  
0 1 1 0 0  
0 0 1 1 1  
1 1 0 0 0  
```

**Coordenada inicial:** `(0, 0)`

#### Grid de Saída:

```
2 2 1 3 3  
2 1 1 3 3  
2 2 1 1 1  
1 1 4 4 4  
```

---

### 🧪 Exemplo 2

#### Grid de Entrada:

```
0 1 0 0 1  
0 1 0 0 1  
0 1 1 1 1  
0 0 0 1 0  
```

**Coordenada inicial:** `(0, 2)`

#### Grid de Saída:

```
3 1 2 2 1  
3 1 2 2 1  
3 1 1 1 1  
3 3 3 1 4  
```

---

## Plot de Imagens

### Entrada:

![](/flood_fill_python/Entrada.png)

### Saida:

![](/flood_fill_python/Saída.png)

## 🧪 Testes Unitários

O arquivo `test_flood_fill.py` contém testes automáticos com `pytest` para validar o algoritmo com diferentes configurações de entrada:

* Grids simples com e sem obstáculos
* Cenários sem caminho disponível
* Casos onde a célula inicial já está preenchida
* Casos com múltiplas regiões desconectadas

### Rodar testes:

```bash
pytest test_flood_fill.py
```
---

## 📁 Estrutura do Projeto

```sh
.  
├── flood_fill_python  
│   ├── Entrada.png  
│   ├── main.py  
│   ├── mazegen.py  
│   ├── requirements.txt  
│   ├── Saída.png  
│   ├── test_flood_fill.py  
│   └── venv/  
├── flood_fill_rust  
│   └── ...  
├── docker-compose.yml  
├── Dockerfile.python  
├── Dockerfile.rust  
├── README.md  
├── pseudocodigo.txt  
├── test.sh  
```

---

## 📚 Referências

* Algoritmo Flood Fill: [https://en.wikipedia.org/wiki/Flood\_fill](https://en.wikipedia.org/wiki/Flood_fill)
* Documentação do `matplotlib`: [https://matplotlib.org/stable/](https://matplotlib.org/stable/)
* `deque` em Python: [https://docs.python.org/3/library/collections.html#collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)

---

