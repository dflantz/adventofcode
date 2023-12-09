from pipe import Pipe, map


def get_end_values(number_list):
    yield number_list[-1]
    while set(number_list) != {0}:
        number_list = [
            number_list[i] - number_list[i - 1] for i in range(1, len(number_list))
        ]
        yield number_list[-1]


print(
    open("input.txt", "r").readlines()
    | map(lambda line: line.split() | map(int) | Pipe(list))
    | map(lambda line: line[::-1])
    | map(get_end_values)
    | map(sum)
    | Pipe(sum)
)
