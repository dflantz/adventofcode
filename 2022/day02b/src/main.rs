enum Move {
    Rock,
    Paper,
    Scissors,
}

enum Result {
    Win,
    Lose,
    Draw,
}

fn decrypt_move(s: &str) -> Move {
    match s {
        "A" => Move::Rock,
        "B" => Move::Paper,
        "C" => Move::Scissors,
        _ => unreachable!(),
    }
}

fn decrypt_result(s: &str) -> Result {
    match s {
        "X" => Result::Lose,
        "Y" => Result::Draw,
        "Z" => Result::Win,
        _ => unreachable!(),
    }
}

fn calculate_points(their_move: Move, needed_result: Result) -> usize {
    let your_move = match needed_result {
        Result::Win => match their_move {
            Move::Rock => Move::Paper,
            Move::Paper => Move::Scissors,
            Move::Scissors => Move::Rock,
        },
        Result::Lose => match their_move {
            Move::Rock => Move::Scissors,
            Move::Paper => Move::Rock,
            Move::Scissors => Move::Paper,
        }
        Result::Draw => their_move
    };

    let move_points = match your_move {
        Move::Rock => 1,
        Move::Paper => 2,
        Move::Scissors => 3,
    };

    let match_points = match needed_result {
        Result::Win => 6,
        Result::Draw => 3,
        Result::Lose => 0,
        _ => unreachable!(),
    };

    move_points + match_points
}

fn main() {
    println!(
        "{}",
        include_str!("../input.txt")
            .lines()
            .map(|n| n.split_once(" ").unwrap())
            .map(|(them, result)| (decrypt_move(them), decrypt_result(result)))
            .map(|(them, result)| calculate_points(them, result))
            .sum::<usize>(),
    );
}
