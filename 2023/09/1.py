from pipe import Pipe, map


def get_diffs(number_list):
    diffs = []
    for i in range(1, len(number_list)):
        diffs.append(number_list[i] - number_list[i - 1])
    return diffs


def get_rightmost_values(number_list):
    rightmost_values = [number_list[-1]]
    while not (len(set(number_list)) == 1 and number_list[0] == 0):
        number_list = get_diffs(number_list)
        rightmost_values.append(number_list[-1])
    return rightmost_values


print(
    open("input.txt", "r").readlines()
    | map(lambda line: line.split() | map(int) | Pipe(list))
    | map(get_rightmost_values)
    | map(sum)
    | Pipe(sum)
)
