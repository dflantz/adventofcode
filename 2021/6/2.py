from typing import Dict, List


def run_cycle(lanternfish: List[int]):
    output = [0] * 9

    for age, count in enumerate(lanternfish):
        if age == 0:
            output[6] += count
            output[8] += count
        else:
            output[age - 1] += count

    return output


if __name__ == "__main__":
    fish_counts = [0] * 9
    with open("2021/6/input.txt", "r") as f:
        for age_str in f.read().strip().split(","):
            fish_counts[int(age_str)] += 1

    print(fish_counts)

    for _ in range(256):
        fish_counts = run_cycle(fish_counts)

    print(sum(fish_counts))
