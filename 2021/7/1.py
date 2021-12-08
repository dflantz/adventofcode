import statistics

if __name__ == "__main__":
    with open("2021/7/input.txt", "r") as f:
        crab_positions = [int(l) for l in f.read().strip().split(",")]

    median = statistics.median(crab_positions)
    m = round(median)

    s = sum([abs(m - n) for n in crab_positions])

    print(s)
