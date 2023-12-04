from pipe import map


def get_num_matches(winners_and_picks):
    return len(set(winners_and_picks[0]) & set(winners_and_picks[1]))


print(
    sum(
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
        | map(lambda num_matches: 2 ** (num_matches - 1) if num_matches > 0 else 0)
    )
)
