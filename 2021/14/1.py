def apply_step(pt: str, rule_dict: dict) -> str:
    out = ""
    for i in range(len(pt) - 1):
        pair = pt[i : i + 2]
        if (to_insert := rule_dict.get(pair)) is not None:
            out += pair[0] + to_insert
    out += pair[1]
    return out


if __name__ == "__main__":
    with open("14/input.txt", "r") as f:
        polymer_template, rules = f.read().split("\n\n")

    rule_dict = {}
    for rule in rules.splitlines():
        pair, to_insert = rule.split(" -> ")
        rule_dict[pair] = to_insert

    for n in range(10):
        polymer_template = apply_step(polymer_template, rule_dict)

    counts = {c: polymer_template.count(c) for c in set(polymer_template)}

    print(max(counts.values()) - min(counts.values()))
