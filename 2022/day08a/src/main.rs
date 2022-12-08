use std::collections::HashSet;

fn main() {
    let grid = include_str!("../input.txt")
        .lines()
        .map(|line| {
            line.chars()
                .map(|c| c.to_digit(10).unwrap())
                .collect::<Vec<u32>>()
        })
        .collect::<Vec<Vec<u32>>>();


    let mut visible: HashSet<(usize, usize)> = HashSet::new();

    //  move left to right
    for y in 0..grid.len() {
        let mut max_height: i32 = -1;
        for x in 0..grid[y].len() {
            if grid[y][x] as i32 > max_height {
                visible.insert((y, x));
                max_height = grid[y][x] as i32;
            }
        }
    }

    //  move right to left
    for y in 0..grid.len() {
        let mut max_height: i32 = -1;
        for x in (0..grid[y].len()).rev() {
            if grid[y][x] as i32 > max_height {
                visible.insert((y, x));
                max_height = grid[y][x] as i32;
            }
        }
    }

    // move top to bottom
    for x in 0..grid[0].len() {
        let mut max_height: i32 = -1;
        for y in 0..grid.len() {
            if grid[y][x] as i32 > max_height {
                visible.insert((y, x));
                max_height = grid[y][x] as i32;
            }
        }
    }

    // bottom to top
    for x in 0..grid[0].len() {
        let mut max_height: i32 = -1;
        for y in (0..grid.len()).rev() {
            if grid[y][x] as i32 > max_height {
                visible.insert((y, x));
                max_height = grid[y][x] as i32;
            }
        }
    }

    println!("{:?}", visible.len())
}
