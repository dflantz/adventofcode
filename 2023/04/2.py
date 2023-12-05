from collections import defaultdict
from pipe import map, Pipe
from functools import reduce


@Pipe
def pipe_reduce(iterable, function, initializer=None):
    return reduce(function, iterable, initializer)


@Pipe
def items(d):
    yield from d.items()


def duplicate_card_to_future(acc, curr):
    acc[curr[0]]
    for i in range(curr[0] + 1, curr[0] + curr[1] + 1):
        acc[i] += acc[curr[0]]
    return acc


print(
    open("input.txt", "r").readlines()
    | map(lambda line: line.split(":")[1])
    | map(lambda numbers: numbers.split("|"))
    | map(
        lambda winners_and_picks: (
            [int(s) for s in winners_and_picks[0].strip().split()],
            [int(s) for s in winners_and_picks[1].strip().split()],
        )
    )
    | map(
        lambda winners_and_picks: len(
            set(winners_and_picks[0]) & set(winners_and_picks[1])
        )
    )
    | Pipe(enumerate)
    | pipe_reduce(duplicate_card_to_future, defaultdict(lambda: 1))
    | items
    | map(lambda item: item[1])
    | Pipe(sum)
)
