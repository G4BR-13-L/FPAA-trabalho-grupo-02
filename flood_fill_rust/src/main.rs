use std::collections::VecDeque;

fn flood_fill(grid: &mut Vec<Vec<u32>>, start_x: usize, start_y: usize, color: u32) {
    let n = grid.len();
    let m = grid[0].len();

    if grid[start_x][start_y] != 0 {
        return;
    }

    let mut queue = VecDeque::new();
    queue.push_back((start_x, start_y));
    grid[start_x][start_y] = color;

    let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)];

    while let Some((x, y)) = queue.pop_front() {
        for (dx, dy) in directions {
            let nx = x as isize + dx;
            let ny = y as isize + dy;

            if nx >= 0 && nx < n as isize && ny >= 0 && ny < m as isize {
                let (nx, ny) = (nx as usize, ny as usize);
                if grid[nx][ny] == 0 {
                    grid[nx][ny] = color;
                    queue.push_back((nx, ny));
                }
            }
        }
    }
}

fn fill_all_regions(mut grid: Vec<Vec<u32>>, start_x: usize, start_y: usize) -> Vec<Vec<u32>> {
    let mut color = 2;
    let n = grid.len();
    let m = grid[0].len();

    if grid[start_x][start_y] == 0 {
        flood_fill(&mut grid, start_x, start_y, color);
        color += 1;
    }

    for i in 0..n {
        for j in 0..m {
            if grid[i][j] == 0 {
                flood_fill(&mut grid, i, j, color);
                color += 1;
            }
        }
    }

    grid
}

// Printa o grid formatado
fn print_grid(grid: &[Vec<u32>]) {
    for row in grid {
        for val in row {
            print!("{} ", val);
        }
        println!();
    }
}

fn main() {
    // Exemplo 1
    let grid1 = vec![
        vec![0, 0, 1, 0, 0],
        vec![0, 1, 1, 0, 0],
        vec![0, 0, 1, 1, 1],
        vec![1, 1, 0, 0, 0],
    ];
    let start_x1 = 0;
    let start_y1 = 0;

    println!("Resultado Exemplo 1:");
    let result1 = fill_all_regions(grid1, start_x1, start_y1);
    print_grid(&result1);

    // Exemplo 2
    let grid2 = vec![
        vec![0, 1, 0, 0, 1],
        vec![0, 1, 0, 0, 1],
        vec![0, 1, 1, 1, 1],
        vec![0, 0, 0, 1, 0],
    ];
    let start_x2 = 0;
    let start_y2 = 2;

    println!("\nResultado Exemplo 2:");
    let result2 = fill_all_regions(grid2, start_x2, start_y2);
    print_grid(&result2);
}

#[cfg(test)]
mod tests {
    use super::*;

    fn run_flood_fill(grid: Vec<Vec<u32>>, x: usize, y: usize) -> Vec<Vec<u32>> {
        fill_all_regions(grid, x, y)
    }

    #[test]
    fn test_example_1() {
        let input = vec![
            vec![0, 0, 1, 0, 0],
            vec![0, 1, 1, 0, 0],
            vec![0, 0, 1, 1, 1],
            vec![1, 1, 0, 0, 0],
        ];
        let expected = vec![
            vec![2, 2, 1, 3, 3],
            vec![2, 1, 1, 3, 3],
            vec![2, 2, 1, 1, 1],
            vec![1, 1, 4, 4, 4],
        ];

        let result = run_flood_fill(input, 0, 0);
        assert_eq!(result, expected);
    }

    #[test]
    fn test_example_2() {
        let input = vec![
            vec![0, 1, 0, 0, 1],
            vec![0, 1, 0, 0, 1],
            vec![0, 1, 1, 1, 1],
            vec![0, 0, 0, 1, 0],
        ];
        let expected = vec![
            vec![3, 1, 2, 2, 1],
            vec![3, 1, 2, 2, 1],
            vec![3, 1, 1, 1, 1],
            vec![3, 3, 3, 1, 4],
        ];

        let result = run_flood_fill(input, 0, 2);
        assert_eq!(result, expected);
    }
}

