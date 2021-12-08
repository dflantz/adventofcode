import statistics
from tqdm import tqdm


def calculate_crab_fuel(start: int, end: int):
    sum = 0
    fuel_cost = 1
    diff = abs(start - end)
    # print(f"{start}, {end}, {diff}")

    while diff > 0:
        sum += fuel_cost
        fuel_cost += 1
        diff -= 1
    # print(sum)
    return sum


if __name__ == "__main__":
    with open("2021/7/input.txt", "r") as f:
        crab_positions = [int(l) for l in f.read().strip().split(",")]

    mean = statistics.mean(crab_positions)
    print(mean)

    m = round(mean)
    lowest = None
    for mc in tqdm(range(m - 10, m + 10)):
        s = sum([calculate_crab_fuel(mc, n) for n in crab_positions])
        if lowest is None:
            lowest = s
        elif s < lowest:
            lowest = s
            print(f"new lowest at {mc}: {lowest}")

    print(lowest)
