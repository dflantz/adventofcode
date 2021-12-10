if __name__ == "__main__":
    grid = [[int(c) for c in s.strip()] for s in open("2021/9/input.txt", "r")]

    def up(row, col):
        if row > 0:
            return row - 1, col

    def down(row, col):
        if row < (len(grid) - 1):
            return row + 1, col

    def left(row, col):
        if col > 0:
            return row, col - 1

    def right(row, col):
        if col < (len(grid[row]) - 1):
            return row, col + 1

    def is_larger(row, col, n, fn):
        if (coords := fn(row, col)) is not None:
            return grid[coords[0]][coords[1]] > n
        else:
            return True

    sum = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if all(
                [
                    is_larger(row, col, grid[row][col], fn)
                    for fn in [up, down, left, right]
                ]
            ):
                print(f"found low point: {row}, {col}, value: {grid[row][col]}")
                sum += grid[row][col] + 1

    print(sum)
