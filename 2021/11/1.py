from typing import List


def run_cycle(octopuses: List[List[int]]):
    flashes = 0
    # first, increment everyone
    for i, row in enumerate(octopuses):
        for j, octo_energy in enumerate(row):
            octopuses[i][j] = octo_energy + 1

    for i, row in enumerate(octopuses):
        for j, octo_energy in enumerate(row):
            if octo_energy > 9:
                flashes += play_flash(octopuses, i, j, 0)
    return flashes


def play_flash(octopuses: List[List[int]], row: int, col: int, count: int):
    octopuses[row][col] = 0
    count += 1

    def rip_it(r: int, c: int):
        nonlocal count
        if octopuses[r][c] != 0:
            octopuses[r][c] += 1
            if octopuses[r][c] > 9:
                count += play_flash(octopuses, r, c, 0)

    # down
    if row < (len(octopuses) - 1):
        r, c = row + 1, col
        rip_it(r, c)

    # up
    if row > 0:
        r, c = row - 1, col
        rip_it(r, c)

    # left
    if col > 0:
        r, c = row, col - 1
        rip_it(r, c)

    # right
    if col < (len(octopuses[0]) - 1):
        r, c = row, col + 1
        rip_it(r, c)

    # top and left:
    if row > 0 and col > 0:
        r, c = row - 1, col - 1
        rip_it(r, c)

    # top and right:
    if row > 0 and col < (len(octopuses[0]) - 1):
        r, c = row - 1, col + 1
        rip_it(r, c)

    # bottom and left:
    if row < (len(octopuses) - 1) and col > 0:
        r, c = row + 1, col - 1
        rip_it(r, c)

    # bottom and right:
    if row < (len(octopuses) - 1) and col < (len(octopuses[0]) - 1):
        r, c = row + 1, col + 1
        rip_it(r, c)

    return count


if __name__ == "__main__":
    octopuses = []
    for line in open("2021/11/input.txt", "r"):
        octopuses.append([int(c) for c in line.strip()])

    # for l in octopuses:
    #     print(l)

    total_flashes = 0
    for i in range(1000):
        flashes = run_cycle(octopuses)
        if flashes == 100:
            print(f" all flashed in step {i}")
            exit(0)
        total_flashes += flashes
    print("after cycle:")
    for l in octopuses:
        print("".join([str(n) for n in l]))
    print(total_flashes)
