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


def meets_symbol_conditions(symbol):
    return symbol != "." and not symbol.isnumeric()


def matrix_value_is_symbol(matrix, coords):
    if coords[0] >= 0 and coords[1] >= 0:
        try:
            return meets_symbol_conditions(matrix[coords[0]][coords[1]])
        except IndexError:
            pass
    return False


def check_surrounding_values(matrix, line_idx, char_enum):
    return any(
        matrix_value_is_symbol(matrix, f(line_idx, char_enum[0]))
        for f in [
            above,
            below,
            left,
            right,
            above_left,
            above_right,
            below_left,
            below_right,
        ]
    )


def find_adjacent_elements(matrix, line):
    return map(
        lambda s: check_surrounding_values(matrix, line[0], s),
        enumerate(line[1]),
    )


def get_number_grouping(line):
    return [
        (match.group(), match.start(), match.end())
        for match in re.finditer(r"\d+", "".join(line))
    ]


def has_overlap(mapped_matrix, line_idx, start_index, end_index):
    return any(mapped_matrix[line_idx][i] for i in range(start_index, end_index))


def filter_for_overlap(mapped_matrix, line_idx, groupings):
    return list(
        filter(lambda x: has_overlap(mapped_matrix, line_idx, x[1], x[2]), groupings)
    )


def get_line_sum(line_matches):
    return sum(int(x[0]) for x in line_matches)


def analyze(matrix, mapped_matrix):
    return sum(
        map(
            get_line_sum,
            map(
                lambda x: filter_for_overlap(mapped_matrix, x[0], x[1]),
                enumerate(
                    map(
                        lambda x: get_number_grouping(matrix[x[0]]),
                        enumerate(mapped_matrix),
                    )
                ),
            ),
        )
    )


def grouping_match(direction_coords, grouping_line_index, grouping_start, grouping_end):
    return (
        direction_coords[0] == grouping_line_index
        and grouping_start <= direction_coords[1] < grouping_end
    )


def length_2(x):
    return len(x) == 2


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


def subrun(matrix, groupings):
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
                                    groupings,
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


def run(matrix):
    return subrun(
        matrix,
        reduce(
            operator.concat,
            map(
                lambda x: [(*y, x[0]) for y in x[1]],
                enumerate(
                    map(get_number_grouping, matrix),
                ),
            ),
        ),
    )


print(run(list(map(lambda line: line.strip(), open("input.txt", "r").readlines()))))
