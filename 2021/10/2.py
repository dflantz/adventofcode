POP_PAIRS = {"]": "[", "}": "{", ")": "(", ">": "<"}

COMPLETION_PAIRS = {"[": "]", "{": "}", "(": ")", "<": ">"}

POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def calculate_points(completion_str: str):
    score = 0
    for c in completion_str:
        score *= 5
        score += POINTS[c]
    return score


def get_completion_string(s):
    stack = []
    for c in s:
        if c in POP_PAIRS.values():
            # print(f"adding {c} to stack")
            stack.append(c)
        else:
            closing = stack.pop()
            if closing != POP_PAIRS.get(c):
                return None

    if len(stack):
        completion_str = ""
        while len(stack):
            completion_str += COMPLETION_PAIRS[stack.pop()]
        return completion_str


if __name__ == "__main__":
    scores = []
    for line in open("2021/10/input.txt", "r"):
        completion_str = get_completion_string(line.strip())
        if completion_str is not None:
            score = calculate_points(completion_str)
            scores.append(score)

    # could implement a BST to keep track of middle but who's got time for that
    middle_score = sorted(scores)[len(scores) // 2]
    print(middle_score)
