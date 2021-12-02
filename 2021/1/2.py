with open("2021/1/input.txt", "r") as f:
    measurements = [int(l) for l in f.readlines()]

count = len(
    [
        i
        for i in range(len(measurements))
        if sum(measurements[i : i + 3]) < sum(measurements[i + 1 : i + 4])
    ]
)

print(count)
