count = 0
prev = None
for line in open("2021/1/input.txt", "r"):
    n = int(line)
    if prev is not None and n > prev:
        count += 1
    prev = n

print(count)
