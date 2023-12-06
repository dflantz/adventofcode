from functools import reduce
from math import floor, ceil
import operator
from pipe import map, Pipe


@Pipe
def pipe_reduce(iterable, function, initializer=None):
    return reduce(function, iterable, initializer)


def quadratic_formula(a, b, c):
    return (
        (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a),
        (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a),
    )


def get_number_of_ways_to_win(time, target_distance):
    # find instance of first match
    # a = 1
    # b = -time
    # c = target_distance

    first_win, last_win = quadratic_formula(1, -time, target_distance)

    # there is probably a cleaner way 
    return ceil(last_win - 1) + 1 - floor(first_win + 1)


print(
    open("input.txt", "r").readlines()
    | map(lambda line: int("".join(line.split(":")[1].split())))
    | Pipe(list)
    | Pipe(
        lambda time_and_distance: get_number_of_ways_to_win(
            time_and_distance[0], time_and_distance[1]
        )
    )
)
