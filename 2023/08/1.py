from functools import reduce
from pipe import map, Pipe


instructions, graph_entries = open("input.txt", "r").read().split("\n\n")
instructions = instructions.strip()

graph = {
    x[0]: x[1]
    for x in (
        graph_entries.split("\n")
        | map(lambda x: x.split("="))
        | map(
            lambda left_and_right: (
                left_and_right[0].strip(),
                left_and_right[1].split(",")
                | map(lambda x: x.strip().replace("(", "").replace(")", ""))
                | Pipe(tuple),
            )
        )
    )
}

curr_node = 'AAA'
steps = 0
while curr_node != 'ZZZ':
    instruction = instructions[steps % len(instructions)]
    match instruction:
        case 'L':
            curr_node = graph[curr_node][0]
        case 'R':
            curr_node = graph[curr_node][1]
    steps += 1

print(steps)
        