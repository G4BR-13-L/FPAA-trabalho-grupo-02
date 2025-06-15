use std::collections::{BinaryHeap, HashMap, HashSet};
use std::cmp::Ordering;

#[derive(Clone, Copy, Eq, PartialEq, Hash, Debug)]
struct Pos {
    x: usize,
    y: usize,
}

#[derive(Eq, PartialEq)]
struct Node {
    pos: Pos,
    priority: usize,
}

impl Ord for Node {
    fn cmp(&self, other: &Self) -> Ordering {
        // menor prioridade vem primeiro
        other.priority.cmp(&self.priority)
    }
}

impl PartialOrd for Node {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}


fn heuristica(a: Pos, b: Pos) -> usize {
    ((a.x as isize - b.x as isize).abs() + (a.y as isize - b.y as isize).abs()) as usize
}

fn encontrar_posicao(labirinto: &Vec<Vec<char>>, alvo: char) -> Option<Pos> {
    for (x, linha) in labirinto.iter().enumerate() {
        for (y, &celula) in linha.iter().enumerate() {
            if celula == alvo {
                return Some(Pos { x, y });
            }
        }
    }
    None
}

fn vizinhos_validos(pos: Pos, labirinto: &Vec<Vec<char>>) -> Vec<Pos> {
    let mut vizinhos = Vec::new();
    let direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)];
    let linhas = labirinto.len();
    let colunas = labirinto[0].len();

    for (dx, dy) in direcoes.iter() {
        let nx = pos.x as isize + dx;
        let ny = pos.y as isize + dy;
        if nx >= 0 && ny >= 0 && (nx as usize) < linhas && (ny as usize) < colunas {
            let celula = labirinto[nx as usize][ny as usize];
            if celula != '1' {
                vizinhos.push(Pos { x: nx as usize, y: ny as usize });
            }
        }
    }

    // DEBUG:
    println!("Vizinhos de ({}, {}): {:?}", pos.x, pos.y, vizinhos);

    vizinhos
}


fn reconstruir_caminho(mut atual: Pos, veio_de: &HashMap<Pos, Pos>) -> Vec<Pos> {
    let mut caminho = vec![atual];
    while let Some(&anterior) = veio_de.get(&atual) {
        atual = anterior;
        caminho.push(atual);
    }
    caminho.reverse();
    caminho
}

fn a_estrela(labirinto: &Vec<Vec<char>>) -> Option<Vec<Pos>> {
    let inicio = encontrar_posicao(labirinto, 'S')?;
    let fim = encontrar_posicao(labirinto, 'E')?;

    let mut open_set = BinaryHeap::new();
    open_set.push(Node { pos: inicio, priority: 0 });

    let mut g_score: HashMap<Pos, usize> = HashMap::new();
    g_score.insert(inicio, 0);

    let mut f_score: HashMap<Pos, usize> = HashMap::new();
    f_score.insert(inicio, heuristica(inicio, fim));

    let mut veio_de: HashMap<Pos, Pos> = HashMap::new();

    while let Some(Node { pos: atual, .. }) = open_set.pop() {
        if atual == fim {
            return Some(reconstruir_caminho(atual, &veio_de));
        }

        for vizinho in vizinhos_validos(atual, labirinto) {
            let tentativa_g = g_score.get(&atual).unwrap_or(&usize::MAX) + 1;

            if tentativa_g < *g_score.get(&vizinho).unwrap_or(&usize::MAX) {
                veio_de.insert(vizinho, atual);
                g_score.insert(vizinho, tentativa_g);
                let f = tentativa_g + heuristica(vizinho, fim);
                f_score.insert(vizinho, f);
                open_set.push(Node { pos: vizinho, priority: f });
            }
        }
    }

    None
}


fn imprimir_labirinto_com_caminho(labirinto: &Vec<Vec<char>>, caminho: &Vec<Pos>) {
    let mut labirinto = labirinto.clone();
    for &pos in caminho {
        let celula = labirinto[pos.x][pos.y];
        if celula != 'S' && celula != 'E' {
            labirinto[pos.x][pos.y] = '*';
        }
    }

    for linha in labirinto {
        for celula in linha {
            print!("{} ", celula);
        }
        println!();
    }
}

fn main() {
    let labirinto = vec![
        vec!['S', '0', '1', '0', '0'],
        vec!['0', '0', '1', '0', '1'],
        vec!['1', '0', '1', '0', '0'],
        vec!['1', '0', '0', 'E', '1'],
    ];

    if let Some(caminho) = a_estrela(&labirinto) {
        println!("Caminho encontrado:");
        for pos in &caminho {
            println!("({},{})", pos.x, pos.y);
        }
        println!("\nLabirinto com caminho:");
        imprimir_labirinto_com_caminho(&labirinto, &caminho);
    } else {
        println!("Nenhum caminho encontrado.");
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn pos(x: usize, y: usize) -> Pos {
        Pos { x, y }
    }

    #[test]
    fn teste_caminho_simples() {
        let labirinto = vec![
            vec!['S', '0', 'E'],
        ];

        let caminho = a_estrela(&labirinto);
        assert!(caminho.is_some());
        let resultado = caminho.unwrap();
        assert_eq!(resultado.first().unwrap(), &pos(0, 0));
        assert_eq!(resultado.last().unwrap(), &pos(0, 2));
    }

    #[test]
    fn teste_sem_caminho() {
        let labirinto = vec![
            vec!['S', '1', 'E'],
        ];

        let caminho = a_estrela(&labirinto);
        assert!(caminho.is_none());
    }

    #[test]
    fn teste_inicio_igual_fim() {
        let labirinto = vec![
            vec!['E'],
        ];

        // como não existe 'S', deve retornar None
        let caminho = a_estrela(&labirinto);
        assert!(caminho.is_none());

        let labirinto = vec![
            vec!['S'],
        ];

        // como não existe 'E', deve retornar None
        let caminho = a_estrela(&labirinto);
        assert!(caminho.is_none());
    }

    #[test]
    fn teste_labirinto_vazio() {
        let labirinto: Vec<Vec<char>> = vec![];
        let caminho = a_estrela(&labirinto);
        assert!(caminho.is_none());
    }
}
