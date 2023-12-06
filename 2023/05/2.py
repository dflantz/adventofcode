from pipe import map, Pipe, where, chain, dedup
from functools import cache


@Pipe
def min_with_default(iterable, default):
    def inner(iterable):
        try:
            return min(iterable)
        except ValueError:
            return default

    return inner(iterable)


def get_dest_value_if_exists(seed, dest_range_start, source_range_start, range_len):
    if source_range_start <= seed < source_range_start + range_len:
        return dest_range_start + seed - source_range_start
    else:
        return None


@cache
def find_seed_mapping(seed, mapping_range_set):
    for (dest_range_start, source_range_start, range_len) in mapping_range_set:
        if source_range_start <= seed < source_range_start + range_len:
            return dest_range_start + seed - source_range_start
    return seed


@cache
def traverse_mappings(seed, mapping_range_sets):
    for set in mapping_range_sets:
        seed = find_seed_mapping(seed, set)
    return seed


@Pipe
def parse(seeds_and_mappings):
    return (
        seeds_and_mappings[0].split(":")[1].split() | map(int) | Pipe(list),
        seeds_and_mappings[1]
        | map(
            lambda section: section.split(":")[1].strip().split("\n")
            | map(lambda map_entry: tuple(int(s) for s in map_entry.split()))
            | Pipe(tuple)
        )
        | Pipe(tuple),
    )


@Pipe
def generate_full_series(seeds_and_mappings):
    return (
        [
            seeds_and_mappings[0][i : i + 2]
            for i in range(0, len(seeds_and_mappings[0]), 2)
        ]
        | map(
            lambda start_and_range: range(
                start_and_range[0], start_and_range[0] + start_and_range[1]
            )
        )
        | chain
        | dedup,
        seeds_and_mappings[1],
    )


print(
    open("input.txt", "r").read().split("\n\n")
    | Pipe(lambda sections: (sections[0], sections[1:]))
    | parse
    | generate_full_series
    | Pipe(
        lambda seeds_and_mappings: seeds_and_mappings[0]
        | map(lambda seed: traverse_mappings(seed, seeds_and_mappings[1]))
    )
    | Pipe(min)
)
