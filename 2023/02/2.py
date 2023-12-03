from collections import defaultdict
import functools


def set_color_minimums(accumulator, pickings):
    for color, amount in pickings.items():
        accumulator.update({color: max(accumulator[color], amount)})
    return accumulator


def get_minimum_set_power(game_and_pickings):
    return functools.reduce(
        lambda x, y: x * y,
        functools.reduce(
            set_color_minimums, game_and_pickings["pickings"], defaultdict(int)
        ).values(),
    )


print(
    sum(
        map(
            get_minimum_set_power,
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
                    lambda line: line.strip().split(":"),
                    open("input.txt", "r").readlines(),
                ),
            ),
        ),
    )
)
