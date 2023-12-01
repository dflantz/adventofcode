import re

print(
    sum(
        map(
            lambda x: int(x[0] + x[len(x) - 1]),
            map(lambda x: re.findall("\d", x), open("input.txt", "r").readlines()),
        )
    )
)
