from typing import Dict, List


def convert_str_to_binary(input: str):
    return sum(
        [2 ** (len(input) - (i + 1)) for i in range(len(input)) if input[i] == "1"]
    )


def get_place_counts(inputs: List[str]) -> Dict[int, str]:
    places: Dict[int, str] = {}
    for line in inputs:
        for i, digit in enumerate(line):
            if places.get(i) is None:
                places[i] = 0
            if digit == "1":
                places[i] += 1
            else:
                places[i] -= 1
    return places


def best_match(lines: List[str], invert: bool) -> str:
    for i in range(len(lines[0])):
        places = get_place_counts(lines)
        if invert:
            lines = list(
                filter(
                    lambda line: line[i] == "0" if places[i] >= 0 else line[i] == "1",
                    lines,
                )
            )
        else:
            lines = list(
                filter(
                    lambda line: line[i] == "1" if places[i] >= 0 else line[i] == "0",
                    lines,
                )
            )

        if len(lines) == 1:
            return lines[0]
    raise Exception(f"more than one competing lines in input: {lines}")


if __name__ == "__main__":
    lines = [f.strip() for f in open("2021/3/input.txt")]

    o2_gen = best_match(lines, invert=False)
    co2_scrub = best_match(lines, invert=True)

    print(convert_str_to_binary(o2_gen) * convert_str_to_binary(co2_scrub))
