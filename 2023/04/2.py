from pipe import map


def get_num_matches(winners_and_picks):
    return len(set(winners_and_picks[0]) & set(winners_and_picks[1]))


# print(
#     list(
#         open("input.txt", "r").readlines()
#         | map(lambda line: line.strip().split(":"))
#         | map(lambda s: (int(s[0].split()[1]), s[1].strip()))
#         | map(
#             lambda game_and_numbers: (
#                 game_and_numbers[0],
#                 game_and_numbers[1].split("|"),
#             )
#         )
#         | map(
#             lambda game_and_winners_and_picks: (
#                 game_and_winners_and_picks[0],
#                 (
#                     [int(s) for s in game_and_winners_and_picks[1][0].strip().split()],
#                     [int(s) for s in game_and_winners_and_picks[1][1].strip().split()],
#                 ),
#             )
#         )
#         | map(lambda game: get_num_matches(game[1]))
#     )
# )


print(
    list(
        open("input.txt", "r").readlines()
        | map(lambda line: line.strip().split(":"))
        | map(lambda s: s[1].strip())
        | map(lambda numbers: numbers.split("|"))
        | map(
            lambda winners_and_picks: (
                [int(s) for s in winners_and_picks[0].strip().split()],
                [int(s) for s in winners_and_picks[1].strip().split()],
            )
        )
        | map(get_num_matches)
        # | map(lambda num_matches: 2 ** (num_matches - 1) if num_matches > 0 else 0)
    )
)
"""
thoughts
current number is not 0

[4, 2, 2, 1, 0, 0]

index 3 = 1
true * 2^0 +  true * 2^1 + true * 2^2 + true * 2^3 +  true * 2^4
"""