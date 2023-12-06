from pipe import map, Pipe, where, chain, dedup, sort, traverse
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


def find_seed_mapping(seed, mapping_range_set):
    for dest_range_start, source_range_start, range_len in mapping_range_set:
        if source_range_start <= seed < source_range_start + range_len:
            return dest_range_start + seed - source_range_start
    return seed


def map_ranges_to_range_set(ranges, mapping_range_set):
    output = []
    for source_start, source_end in ranges:
        for dest_start, dest_end, shift in mapping_range_set:
            if source_start == source_end:
                continue
            # fully contained
            if source_start >= dest_start and source_end < dest_end:
                output.append(
                    (
                        source_start + shift,
                        source_end + shift,
                    )
                )
                source_start = source_end
            # partial overlap left
            elif source_start < dest_start and source_end >= dest_start:
                output.append(
                    (
                        source_start + shift,
                        dest_start + shift,
                    )
                )
                source_start = dest_start
            # partial overlap right
            elif source_start < dest_end and source_end >= dest_end:
                output.append(
                    (
                        source_start + shift,
                        dest_end + shift,
                    )
                )
                source_end = dest_end

            # # no overlap
            # else:
            #     output.append(
            #         (
            #             source_start,
            #             source_end,
            #         )
            #     )
            #     source_start = source_end
        if source_start != source_end:
            output.append(
                (
                    source_start,
                    source_end,
                )
            )

    return output


def get_mapped_ranges(source_start, source_end, mapping_range_set):
    output = []
    covered = False
    for dest_start, dest_end, shift in mapping_range_set:
        if source_start >= dest_start and source_end < dest_end:
            output.append(
                (
                    source_start + shift,
                    source_end + shift,
                )
            )
            source_start = source_end
            covered = True
            break
        elif source_start < dest_start and source_end > dest_end:
            output.append(
                (
                    dest_start + shift,
                    dest_end + shift,
                )
            )
            covered = True
            break
            print("Problem: source range fully contains dest range")
        # partial overlap left
        elif source_start < dest_start and dest_start < source_end < dest_end:
            output.append(
                (
                    source_end + shift,
                    dest_end + shift,
                )
            )
            source_start = dest_start
        # partial overlap right
        elif dest_start <= source_start < dest_end and source_end >= dest_end:
            output.append(
                (
                    source_start + shift,
                    dest_end + shift,
                )
            )
            source_start = dest_end

    if not covered and source_start != source_end:
        output.append(
            (
                source_start,
                source_end,
            )
        )

    return output


def run_seed_range_through_mappings(seed_ranges, mapping_range_sets):
    # print("running range calculation for", seed_ranges)
    for set in mapping_range_sets:
        tmp = []
        for range in seed_ranges:
            ranges = get_mapped_ranges(range[0], range[1], set)
            tmp += ranges
        seed_ranges = tmp
        # seed_ranges = list(map_ranges_to_range_set(seed_ranges, set) | dedup)
        # print("after set", set, ":", seed_ranges)
    return seed_ranges


@Pipe
def parse(seeds_and_mappings):
    return (
        seeds_and_mappings[0].split(":")[1].split() | map(int) | Pipe(list),
        seeds_and_mappings[1]
        | map(
            lambda section: section.split(":")[1].strip().split("\n")
            | map(lambda map_entry: tuple(int(s) for s in map_entry.split()))
            | sort(lambda x: x[1])
            | map(
                lambda map_entry: (
                    map_entry[1],  # start
                    map_entry[1] + map_entry[2],  # end
                    map_entry[0] - map_entry[1],  # shift
                )
            )
            | Pipe(list)
        )
        | Pipe(tuple),
    )


# @Pipe
# def generate_full_series(seeds_and_mappings):
#     return (
#         [
#             seeds_and_mappings[0][i : i + 2]
#             for i in range(0, len(seeds_and_mappings[0]), 2)
#         ]
#         | map(
#             lambda start_and_range: range(
#                 start_and_range[0], start_and_range[0] + start_and_range[1]
#             )
#         )
#         | chain
#         | dedup,
#         seeds_and_mappings[1],
#     )


@Pipe
def run(seeds_and_mappings):
    return (
        seeds_and_mappings[0]
        | map(
            lambda interval: run_seed_range_through_mappings(
                [[interval[0], interval[0] + interval[1] - 1]], seeds_and_mappings[1]
            )
        )
        | traverse
        | Pipe(min)
    )


print(
    open("input.txt", "r").read().split("\n\n")
    | Pipe(lambda sections: (sections[0], sections[1:]))
    | parse
    | Pipe(
        lambda seeds_and_mappings: (
            [
                seeds_and_mappings[0][i : i + 2]
                for i in range(0, len(seeds_and_mappings[0]), 2)
            ],
            seeds_and_mappings[1],
        )
    )
    | Pipe(list)
    | run
    # | generate_full_series
    # | Pipe(
    #     lambda seeds_and_mappings: seeds_and_mappings[0]
    #     | map(lambda seed: traverse_mappings(seed, seeds_and_mappings[1]))
    # )
    # | Pipe(min)
)
