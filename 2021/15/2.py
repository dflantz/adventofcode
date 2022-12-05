from collections import defaultdict


LETTER_TOTALS = defaultdict(int)


def apply_step(rule_dict: dict, pair_counts: dict) -> dict:
    new_pair_counts = pair_counts.copy()
    for pair in list(pair_counts.keys()):
        if (to_insert := rule_dict.get(pair)) is not None:
            occurrences = pair_counts[pair]
            LETTER_TOTALS[to_insert] += occurrences

            new_pair_counts[pair[0] + to_insert] += occurrences
            new_pair_counts[to_insert + pair[1]] += occurrences

            new_pair_counts[pair] -= occurrences
            if new_pair_counts[pair] < 1:
                del new_pair_counts[pair]

    return new_pair_counts


if __name__ == "__main__":
    with open("14/input.txt", "r") as f:
        polymer_template, rules = f.read().split("\n\n")

    rule_dict = {}
    for rule in rules.splitlines():
        pair, to_insert = rule.split(" -> ")
        rule_dict[pair] = to_insert

    pair_counts = defaultdict(int)
    for i in range(len(polymer_template)):
        LETTER_TOTALS[polymer_template[i]] += 1
        pair = polymer_template[i : i + 2]
        pair_counts[pair] += 1

    for n in range(40):
        pair_counts = apply_step(rule_dict, pair_counts)

    print((totals_sorted := sorted(LETTER_TOTALS.values()))[-1] - totals_sorted[0])
