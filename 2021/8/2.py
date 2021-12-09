# seven segment representation
#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc

# options:
# represent as tuple of 0s/1s with the following indices:
#  1111
# 0    2
# 0    2
#  6666
# 5    3
# 5    3
#  4444

from typing import Dict, Tuple, List


SEVEN_SEGMENT_MAPPING: Dict[Tuple[int], int] = {
    (0, 0, 1, 1, 0, 0, 0): 1,
    (0, 1, 1, 0, 1, 1, 1): 2,
    (0, 1, 1, 1, 0, 0, 0): 7,
    (0, 1, 1, 1, 1, 0, 1): 3,
    (1, 0, 1, 1, 0, 0, 1): 4,
    (1, 1, 0, 1, 1, 0, 1): 5,
    (1, 1, 0, 1, 1, 1, 1): 6,
    (1, 1, 1, 1, 1, 0, 1): 9,
    (1, 1, 1, 1, 1, 1, 0): 0,
    (1, 1, 1, 1, 1, 1, 1): 8,
}


def print_segment(seg: Tuple[int]):
    print(
        f"""
#  {seg[1]}{seg[1]}{seg[1]}{seg[1]}
# {seg[0]}    {seg[2]}
# {seg[0]}    {seg[2]}
#  {seg[6]}{seg[6]}{seg[6]}{seg[6]}
# {seg[5]}    {seg[3]}
# {seg[5]}    {seg[3]}
#  {seg[4]}{seg[4]}{seg[4]}{seg[4]}
    """
    )


def get_string_diff(s1: str, s2: str) -> str:
    diff_set = set(s1.split("")) - set(s2.split(""))
    return "".join(diff_set)


def get_letter_mappings(patterns: List[str]) -> Dict[str, int]:
    # determines which letters from a-g map to which index
    mapping: Dict[str, int] = {}

    p_set = set(patterns)

    # focus on unique values first
    p1 = next(filter(lambda x: len(x) == 2, p_set))
    p_set.remove(p1)
    p4 = next(filter(lambda x: len(x) == 4, p_set))
    p_set.remove(p4)
    p7 = next(filter(lambda x: len(x) == 3, p_set))
    p_set.remove(p7)
    p8 = next(filter(lambda x: len(x) == 7, p_set))
    p_set.remove(p8)

    seg_set = set([c for c in p8])

    # we know that the top bar (seg1) is the difference between p1 and p7
    seg1 = [c for c in p7 if c not in p1][0]
    mapping[seg1] = 1
    seg_set.remove(seg1)

    # figure out the rest of the patterns
    p6 = next(filter(lambda x: len(x) == 6 and not all([c in x for c in p1]), p_set))
    p_set.remove(p6)
    p9 = next(filter(lambda x: len(x) == 6 and all([c in x for c in p4]), p_set))
    p_set.remove(p9)
    p0 = next(filter(lambda x: len(x) == 6, p_set))
    p_set.remove(p0)

    seg5 = [c for c in p8 if c not in p9][0]
    mapping[seg5] = 5
    seg_set.remove(seg5)

    # p2
    p2 = next(filter(lambda x: len(x) == 5 and seg5 in x, p_set))
    p_set.remove(p2)

    # p5
    p5 = next(
        filter(lambda x: len(x) == 5 and len([c for c in x if c not in p2]) == 2, p_set)
    )
    p_set.remove(p5)

    # p3 (last one)
    p3 = p_set.pop()

    # figure out rest of letter -> segment mappings
    seg3 = [c for c in p3 if c not in p2][0]
    mapping[seg3] = 3
    seg_set.remove(seg3)

    # seg 4
    seg2 = [c for c in p8 if c not in p6][0]
    mapping[seg2] = 2
    seg_set.remove(seg2)
    seg6 = [c for c in p8 if c not in p0][0]
    mapping[seg6] = 6
    seg_set.remove(seg6)
    seg0 = [c for c in p4 if c not in p3][0]
    mapping[seg0] = 0
    seg_set.remove(seg0)
    seg4 = seg_set.pop()
    mapping[seg4] = 4

    return mapping


def convert_pattern_to_int(pattern: str, index_mapping: Dict[str, int]) -> int:
    l = [0] * 7
    for c in pattern:
        l[index_mapping[c]] = 1

    res = SEVEN_SEGMENT_MAPPING[tuple(l)]
    return res


if __name__ == "__main__":
    unique_lengths = [2, 4, 3, 7]  # 1, 4, 7, 8
    sum = 0
    for line in open("2021/8/input.txt", "r"):
        signal_patterns, output_values = line.split("|")
        signal_patterns = signal_patterns.split()
        mappings = get_letter_mappings(signal_patterns)

        output_values = output_values.split()
        output_ints = [convert_pattern_to_int(v, mappings) for v in output_values]
        full_sum = int("".join([str(i) for i in output_ints]))
        sum += full_sum

    print(sum)
