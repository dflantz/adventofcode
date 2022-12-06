use std::collections::HashSet;

fn main() {
    let window_size = 14;
    let buffer = include_str!("../input.txt").chars().collect::<Vec<char>>();
    let mut i = 0;

    while i + window_size < buffer.len() {
        let window = &buffer[i..i + window_size];
        let s: HashSet<&char> = HashSet::from_iter(window.iter());
        if s.len() == window_size {
            // all are unique
            println!("{}", i + window_size);
            return;
        }
        i += 1;
    }
}
