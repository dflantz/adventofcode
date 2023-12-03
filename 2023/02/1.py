def game_is_possible_with_pickings(game, max_per_color):
    return all(
        map(
            lambda picking: all(
                n <= max_per_color[color] for color, n in picking.items()
            ),
            game["pickings"],
        )
    )


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
                        lambda line: line.strip().split(":"),
                        open("input.txt", "r").readlines(),
                    ),
                ),
            ),
        )
    )
)
