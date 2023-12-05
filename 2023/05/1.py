from pipe import map, Pipe, where


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


def find_seed_mapping(seed, mapping_range_set):
    return (
        mapping_range_set
        | map(lambda s: get_dest_value_if_exists(seed, s[0], s[1], s[2]))
        | where(lambda s: s is not None)
        | min_with_default(seed)
    )


def traverse_mappings(seed, mapping_range_sets):
    if not mapping_range_sets:
        return seed
    return traverse_mappings(find_seed_mapping(seed, mapping_range_sets[0]), mapping_range_sets[1:])


@Pipe
def parse(seeds_and_mappings):
    return (
        seeds_and_mappings[0].split(":")[1].split() | map(int) | Pipe(list),
        seeds_and_mappings[1]
        | map(
            lambda section: section.split(":")[1].strip().split("\n")
            | map(lambda map_entry: [int(s) for s in map_entry.split()])
            | Pipe(list)
        )
        | Pipe(list),
    )


print(
    open("input.txt", "r").read().split("\n\n")
    | Pipe(lambda sections: (sections[0], sections[1:]))
    | parse
    | Pipe(
        lambda seeds_and_mappings: seeds_and_mappings[0]
        | map(lambda seed: traverse_mappings(seed, seeds_and_mappings[1]))
    )
    | Pipe(min)
)
