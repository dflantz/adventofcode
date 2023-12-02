import re


def interpret_and_concat(s, number_mapping):
    print(s)
    return int(
        "".join(
            map(
                lambda x: str(number_mapping.get(x, x)),
                [s[0], s[1]],
            )
        )
    )


def find_first_and_last_numeric_string(s, number_mapping):
    print(s)
    return (
        next(re.finditer("|".join(["\d", *number_mapping.keys()]), s)).group(),
        next(
            re.finditer(
                "|".join(["\d", *[n[::-1] for n in number_mapping.keys()]]), s[::-1]
            )
        ).group()[::-1],
    )


def first_and_last(s):
    print(s)
    return (s[0], s[len(s) - 1])


def run(lines, number_mapping):
    return sum(
        map(
            lambda x: interpret_and_concat(x, number_mapping),
            map(
                lambda x: find_first_and_last_numeric_string(x, number_mapping),
                lines,
            ),
        )
    )


print(
    run(
        lines=open("input.txt", "r").readlines(),
        number_mapping={
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        },
    )
)
