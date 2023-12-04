import operator
import re
from functools import partial, reduce


def above(y, x):
    return y - 1, x


def below(y, x):
    return y + 1, x


def left(y, x):
    return y, x - 1


def right(y, x):
    return y, x + 1


def above_left(y, x):
    return y - 1, x - 1


def above_right(y, x):
    return y - 1, x + 1


def below_left(y, x):
    return y + 1, x - 1


def below_right(y, x):
    return y + 1, x + 1


def get_number_grouping(line):
    return [
        (match.group(), match.start(), match.end())
        for match in re.finditer(r"\d+", "".join(line))
    ]


def grouping_match(direction_coords, grouping_line_index, grouping_start, grouping_end):
    return (
        direction_coords[0] == grouping_line_index
        and grouping_start <= direction_coords[1] < grouping_end
    )


def get_matching_groupings(line_idx, char_idx, groupings):
    return set(
        reduce(
            operator.concat,
            map(
                lambda grouping: [
                    grouping
                    for coord_fn in [
                        above,
                        below,
                        left,
                        right,
                        above_left,
                        above_right,
                        below_left,
                        below_right,
                    ]
                    if grouping_match(
                        coord_fn(line_idx, char_idx),
                        grouping[3],
                        grouping[1],
                        grouping[2],
                    )
                ],
                groupings,
            ),
        )
    )


def run(matrix):
    return sum(
        map(
            lambda match_sets: reduce(
                operator.mul, map(lambda x: int(x[0]), match_sets)
            ),
            filter(
                lambda match_sets: len(match_sets) == 2,
                reduce(
                    operator.concat,
                    map(
                        lambda idx_and_line: list(
                            map(
                                lambda idx_and_char: get_matching_groupings(
                                    idx_and_line[0],
                                    idx_and_char[0],
                                    # this is the least intuitive code here, but it's essentially getting a flattened
                                    # list of number groupings along with the line number and the start/end index
                                    reduce(
                                        operator.concat,
                                        map(
                                            lambda x: [(*y, x[0]) for y in x[1]],
                                            enumerate(
                                                map(get_number_grouping, matrix),
                                            ),
                                        ),
                                    ),
                                ),
                                filter(
                                    lambda idx_and_char: idx_and_char[1] == "*",
                                    enumerate(idx_and_line[1]),
                                ),
                            )
                        ),
                        enumerate(matrix),
                    ),
                ),
            ),
        )
    )


print(run(list(map(lambda line: line.strip(), open("input.txt", "r").readlines()))))
