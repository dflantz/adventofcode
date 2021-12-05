from typing import Dict


def convert_str_to_binary(input: str):
    return sum(
        [2 ** (len(input) - (i + 1)) for i in range(len(input)) if input[i] == "1"]
    )


places: Dict[int, str] = {}

for line in open("2021/3/input.txt"):
    # digits = line.split("")
    for i, digit in enumerate(line.strip()):
        if places.get(i) is None:
            places[i] = 0
        if digit == "1":
            places[i] += 1
        else:
            places[i] -= 1

gamma_str = ["1" if places[d] > 0 else "0" for d in places]
epsilon_str = ["1" if c == "0" else "0" for c in gamma_str]

print(convert_str_to_binary(gamma_str) * convert_str_to_binary(epsilon_str))
