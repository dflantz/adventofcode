from functools import reduce
from pipe import map, Pipe
from sympy.ntheory.modular import solve_congruence
from math import lcm

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


def get_cycle_info(graph, starting_node):
    history = {}
    steps = 0
    cycle_start, cycle_end, steps_to_z = 0, 0, 0
    curr_node = starting_node
    while True:
        instruction = instructions[steps % len(instructions)]

        if curr_node.endswith("Z"):
            if (curr_node, instruction) in history:
                cycle_start = history[(curr_node, instruction)]
                cycle_end = steps
                return cycle_end - cycle_start
            else:
                history[(curr_node, instruction)] = steps
        match instruction:
            case "L":
                curr_node = graph[curr_node][0]
            case "R":
                curr_node = graph[curr_node][1]
        steps += 1


curr_nodes = [k for k in graph.keys() if k.endswith("A")]
cycle_lengths = [get_cycle_info(graph, n) for n in curr_nodes]
print(lcm(*cycle_lengths))
