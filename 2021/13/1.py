from collections import defaultdict
from typing import DefaultDict, Dict, List, Tuple

Paper = DefaultDict[Tuple[int, int], bool]


def calculate_fold(axis: str, n: int, paper: Paper) -> Paper:
    match axis:
        case "x":
            # x = 7
            # x1 = 2
            # x - x1 = 5
            # x + 5
            # x1 = 9
            # x2 = 
            pass
        case "y":
            pass
    pass


if __name__ == "__main__":
    paper: Paper = defaultdict(bool)
    with open("2021/13/example.txt", "r") as f:
        coords, folds = f.read().split("\n\n")

    for l in coords.split("\n"):
        x, y = l.split(",")
        paper[(int(x), int(y))] = True

    print(paper)

    for l in folds.split("\n")[:1]:
        command = l.split()[-1]
        dir, n = command.split("=")

    print(dir, n)
