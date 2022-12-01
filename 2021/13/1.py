from typing import DefaultDict, Tuple


class Paper(DefaultDict[Tuple[int, int], bool]):
    def __init__(self):
        super().__init__()
        self.max_x = 1000000
        self.max_y = 1000000

    def calculate_fold(self, axis: str, n: int):
        match axis:
            case "x":
                # only the second value changes
                for x, y in list(paper.keys()):
                    diff = n - x
                    diff_doubled = diff * 2
                    x_new = x + diff_doubled
                    paper[x_new, y] = True
                    self.max_x = n
            case "y":
                for x, y in list(paper.keys()):
                    diff = n - y
                    diff_doubled = diff * 2
                    y_new = y + diff_doubled
                    paper[x, y_new] = True
                    self.max_y = n

    def count_dots(self) -> int:
        return len(
            [
                s
                for (x, y), s in self.items()
                if s is True and 0 <= x < self.max_x and 0 <= y < self.max_y
            ]
        )

    def __str__(self) -> str:
        print(self.max_x)
        print(self.max_y)
        to_ret = ""
        for y in range(self.max_y):
            for x in range(self.max_x):
                to_ret += "#" if self.get((x, y)) else "."
            to_ret += "\n"
        return to_ret


if __name__ == "__main__":
    paper = Paper()
    with open("13/input.txt", "r") as f:
        coords, folds = f.read().split("\n\n")

    for line in coords.split("\n"):
        x, y = line.split(",")
        paper[(int(x), int(y))] = True

    # print(paper)
    for line in folds.split("\n"):
        command = line.split()[-1]
        dir, n_str = command.split("=")
        paper.calculate_fold(dir, int(n_str))

    print(paper)
