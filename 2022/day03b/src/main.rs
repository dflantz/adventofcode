#![feature(iter_array_chunks)]

use std::collections::{HashMap, HashSet};

fn get_badge(rucksacks: [&str; 3]) -> char {
    let mut counts = HashMap::new();

    for rucksack in rucksacks {
        let char_set: HashSet<char> = HashSet::from_iter(rucksack.chars());
        for c in char_set {
            counts.entry(c).and_modify(|count| *count += 1).or_insert(1);
            if *counts.get(&c).unwrap() == 3 {
                return c;
            }
        }
    }
    panic!()
}

fn get_item_priority(item: char) -> usize {
    if item.is_uppercase() {
        return usize::from(item.to_string().as_bytes()[0] - b'A') + 27;
    } else {
        return usize::from(item.to_string().as_bytes()[0] - b'a') + 1;
    }
}

fn main() {
    println!(
        "{}",
        include_str!("../input.txt")
            .lines()
            .array_chunks::<3>()
            .map(|rucksack_group| get_badge(rucksack_group))
            .map(|c| get_item_priority(c))
            .sum::<usize>()
    )
}
