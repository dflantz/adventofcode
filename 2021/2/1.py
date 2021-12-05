x = y = 0

for line in open("2021/2/input.txt"):
    direction, steps_str = line.split(" ")
    steps = int(steps_str)
    match direction:
        case "forward":
            x += steps
        case "up":
            y -= steps
        case "down":
            y += steps
    
print(x * y)