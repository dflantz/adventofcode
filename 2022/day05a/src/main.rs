use std::collections::HashMap;

fn main() {
    let (stacks, operations) = include_str!("../input.txt").split_once("\n\n").unwrap();

    let mut stack_hash = parse_stacks(stacks);

    let _ = operations
        .lines()
        .map(|line| {
            line.split(" ")
                .filter_map(|n| n.parse::<usize>().ok())
                .collect::<Vec<usize>>()
        })
        .map(|v| {
            for _ in 0..v[0] {
                let ch = stack_hash
                    .get_mut(&v[1].to_string().chars().next().unwrap())
                    .unwrap()
                    .pop()
                    .unwrap();
                stack_hash
                    .entry(v[2].to_string().chars().next().unwrap())
                    .and_modify(|v| v.push(ch));
            }
            0
        })
        .sum::<usize>();

    for i in 1..(stack_hash.len() + 1) {
        print!(
            "{}",
            stack_hash
                .get_mut(&i.to_string().chars().next().unwrap())
                .unwrap()
                .pop()
                .unwrap()
        )
    }
}

fn parse_stacks(input: &str) -> HashMap<char, Vec<char>> {
    let mut stack_hash = HashMap::new();
    let mut stack_indices = HashMap::new();

    let mut stack_lines = input.lines().rev();
    let stack_name_line = stack_lines.next().unwrap();

    for (i, c) in stack_name_line.chars().enumerate() {
        if c != ' ' {
            stack_hash.insert(c, Vec::new());
            stack_indices.insert(c, i);
        }
    }

    for line in stack_lines {
        for (ch, stack) in stack_hash.iter_mut() {
            let char_at_index = line.chars().nth(*stack_indices.get(ch).unwrap()).unwrap();
            if char_at_index != ' ' {
                stack.push(char_at_index);
            };
        }
    }
    stack_hash
}
