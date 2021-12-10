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

    low_points = []

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if all(
                [
                    is_larger(row, col, grid[row][col], fn)
                    for fn in [up, down, left, right]
                ]
            ):
                low_points.append((row, col))

    def find_basin_size(row, col, visited):
        if (row, col) in visited:
            return
        else:
            # print(f"visiting coords {row}, {col}, value {grid[row][col]}")
            visited.add((row, col))

        for dir_fn in [up, down, left, right]:
            if (coords := dir_fn(row, col)) is not None and grid[coords[0]][
                coords[1]
            ] != 9:
                new_row, new_col = dir_fn(row, col)
                find_basin_size(new_row, new_col, visited)

    basin_sizes = []

    for row, col in low_points:
        basin_coords = set()
        find_basin_size(row, col, basin_coords)
        basin_sizes.append(len(basin_coords))

    top3 = sorted(basin_sizes, reverse=True)[:3]

    print(top3)

    product = 1
    for n in top3:
        product *= n

    print(product)
