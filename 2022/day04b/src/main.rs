fn between(n: usize, range_start: usize, range_end: usize) -> bool {
    range_start <= n && n <= range_end
}

fn fully_contained(a1: usize, a2: usize, b1: usize, b2: usize) -> bool {
    (a1 <= b1 && a2 >= b2) || (b1 <= a1 && b2 >= a2)
}

fn has_overlap(r1: &str, r2: &str) -> bool {
    let (a1, a2) = r1.split_once("-").unwrap();
    let (b1, b2) = r2.split_once("-").unwrap();

    let [a1, a2, b1, b2] = [a1, a2, b1, b2].map(|s| s.parse::<usize>().unwrap());

    return fully_contained(a1, a2, b1, b2) || between(a1, b1, b2) || between(a2, b1, b2);
}

fn main() {
    println!(
        "{:?}",
        include_str!("../input.txt")
            .lines()
            .map(|line| line.split_once(',').unwrap())
            .map(|(elf1, elf2)| has_overlap(elf1, elf2))
            .filter(|count| *count == true)
            .count()
    )
}
