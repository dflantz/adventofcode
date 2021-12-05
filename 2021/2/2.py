x = y = aim = 0

for line in open("2021/2/input.txt"):
    direction, steps_str = line.split(" ")
    steps = int(steps_str)
    match direction:
        case "forward":
            x += steps
            y += aim * steps
        case "up":
            aim -= steps
        case "down":
            aim += steps
    
print(x * y)