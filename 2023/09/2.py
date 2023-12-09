from pipe import Pipe, map


def get_diffs(number_list):
    diffs = []
    for i in range(1, len(number_list)):
        diffs.append(number_list[i] - number_list[i - 1])
    return diffs


def get_leftmost_values(number_list):
    leftmost_values = [number_list[0]]
    while not (len(set(number_list)) == 1 and number_list[0] == 0):
        number_list = get_diffs(number_list)
        leftmost_values.append(number_list[0])
    return leftmost_values

def calculate_previous_sequences(leftmost_values):
    cumulative = 0
    for value in leftmost_values[::-1][1:]:
        cumulative = value - cumulative
    return cumulative

print(
    open("input.txt", "r").readlines()
    | map(lambda line: line.split() | map(int) | Pipe(list))
    | map(get_leftmost_values)
    | map(calculate_previous_sequences)
    | Pipe(sum)
)
