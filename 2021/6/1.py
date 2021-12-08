from typing import List


def run_cycle(lanternfish: List[int]):
    i = 0
    generation_len = len(lanternfish)
    while i < generation_len:
        if lanternfish[i] == 0:
            lanternfish[i] = 6
            lanternfish.append(8)
        else:
            lanternfish[i] -= 1
        i += 1


if __name__ == "__main__":
    with open("2021/6/input.txt", "r") as f:
        ages = f.read().strip().split(",")
        fish = [int(age) for age in ages]

    for _ in range(80):
        run_cycle(fish)

    print(len(fish))
