from collections import defaultdict
import functools
import json


def sum_for_color(accumulator, pickings):
    for color, n in pickings.items():
        accumulator[color] += n
    return accumulator


def game_is_possible_with_pickings(game, max_per_color):
    print(
        functools.reduce(sum_for_color, game["pickings"], defaultdict(int)).items(),
    )
    return all(
        map(
            lambda item: item[1] <= max_per_color[item[0]],
            functools.reduce(sum_for_color, game["pickings"], defaultdict(int)).items(),
        )
    )


def strip_line(line):
    print(line)
    return line.strip().split(":")


print(
    sum(
        map(
            lambda game: game["game"],
            filter(
                lambda game: game_is_possible_with_pickings(
                    game,
                    {
                        "red": 12,
                        "green": 13,
                        "blue": 14,
                    },
                ),
                map(
                    lambda game_and_pickings: {
                        "game": int(game_and_pickings[0].split(" ")[1]),
                        "pickings": list(
                            map(
                                lambda pickings_str: {
                                    s[1]: int(s[0])
                                    for s in map(
                                        lambda s: s.strip().split(" "),
                                        pickings_str.split(","),
                                    )
                                },
                                game_and_pickings[1].split(";"),
                            )
                        ),
                    },
                    map(
                        strip_line,
                        open("input.txt", "r").readlines(),
                    ),
                ),
            ),
        )
    )
)
