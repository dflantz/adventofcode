PAIRS = {"]": "[", "}": "{", ")": "(", ">": "<"}

POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def find_first_illegal_character(s):
    stack = []
    for c in s:
        if c in PAIRS.values():
            # print(f"adding {c} to stack")
            stack.append(c)
        else:
            closing = stack.pop()
            if closing != PAIRS.get(c):
                # print(f"illegal char: {c}")
                return c
    # if len(stack):
    #     print(f"expected char {stack.pop()}")
    # else:
    #     print("line is complete")


if __name__ == "__main__":
    score = 0
    for line in open("2021/10/input.txt", "r"):
        char = find_first_illegal_character(line.strip())
        if char is not None:
            score += POINTS[char]

    print(score)
