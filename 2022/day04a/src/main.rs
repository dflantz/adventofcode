fn fully_contained(r1: &str, r2: &str) -> bool {
    let (a1, a2) = r1.split_once("-").unwrap();
    let (b1, b2) = r2.split_once("-").unwrap();

    let [a1, a2, b1, b2] = [a1, a2, b1, b2].map(|s| s.parse::<usize>().unwrap());

    return (a1 <= b1 && a2 >= b2) || (b1 <= a1 && b2 >= a2);
}

fn main() {
    println!(
        "{:?}",
        include_str!("../input.txt")
            .lines()
            .map(|line| line.split_once(',').unwrap())
            .map(|(elf1, elf2)| fully_contained(elf1, elf2))
            .filter(|is_contained| *is_contained == true)
            .count()
    )
}
