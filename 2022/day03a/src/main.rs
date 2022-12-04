use std::collections::HashSet;

fn get_duplicate_item(rucksack: (&str, &str)) -> char {
    let mut items = HashSet::new();

    for c in rucksack.0.chars() {
        items.insert(c);
    }

    for c in rucksack.1.chars() {
        if items.contains(&c) {
            return c;
        } else {
            continue;
        }
    }

    panic!("No Duplicate Found")
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
            .map(|s| (&s[0..s.len() / 2], &s[s.len() / 2..]))
            .map(|rucksack| get_duplicate_item(rucksack))
            .map(|item| get_item_priority(item))
            .sum::<usize>(),
    )
}
