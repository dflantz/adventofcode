enum Move {
    Rock,
    Paper,
    Scissors,
}

fn decrypt_move(s: &str) -> Move {
    match s {
        "A" => Move::Rock,
        "B" => Move::Paper,
        "C" => Move::Scissors,

        "X" => Move::Rock,
        "Y" => Move::Paper,
        "Z" => Move::Scissors,

        _ => unreachable!(),
    }
}

fn calculate_points(their_move: Move, your_move: Move) -> usize {
    let move_points = match your_move {
        Move::Rock => 1,
        Move::Paper => 2,
        Move::Scissors => 3,
    };

    let match_points = match your_move {
        Move::Rock => match their_move {
            Move::Paper => 0,
            Move::Rock => 3,
            Move::Scissors => 6,
        },
        Move::Paper => match their_move {
            Move::Paper => 3,
            Move::Rock => 6,
            Move::Scissors => 0,
        },
        Move::Scissors => match their_move {
            Move::Paper => 6,
            Move::Rock => 0,
            Move::Scissors => 3,
        },
    };

    move_points + match_points
}

fn main() {
    println!(
        "{}",
        include_str!("../input.txt")
            .lines()
            .map(|n| n.split_once(" ").unwrap())
            .map(|(them, you)| (decrypt_move(them), decrypt_move(you)))
            .map(|(them, you)| calculate_points(them, you))
            .sum::<usize>(),
    );
}
