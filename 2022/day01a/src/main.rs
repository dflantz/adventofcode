fn main() {
    println!(
        "{}",
        include_str!("../input.txt")
            .split("\n\n")
            .map(|calorie_group| {
                calorie_group
                    .split("\n")
                    .map(|n| n.parse::<u32>().unwrap())
                    .sum::<u32>()
            })
            .max().unwrap()
    );
}
