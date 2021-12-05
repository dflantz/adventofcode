from __future__ import annotations
from typing import List, NamedTuple

BOARD_DIMENSION = 5


class Number(NamedTuple):
    value: str
    marked: bool


Row = List[Number]
Board = List[Row]


def mark_drawn_number(n: str, board: Board):
    for x, row in enumerate(board):
        for y, number in enumerate(row):
            if number.value == n:
                board[x][y] = Number(n, True)


def check_for_bingo(board: Board):
    return any(
        [
            # lateral
            any([all([n.marked for n in row]) for row in board]),
            # vertical
            any(
                [all([row[i].marked for row in board]) for i in range(BOARD_DIMENSION)]
            ),
            # diag
            # all([board[i][i].marked for i in range(BOARD_DIMENSION)]),
            # reverse diag
            # all(
            #     [
            #         board[i][BOARD_DIMENSION - (i + 1)].marked
            #         for i in range(BOARD_DIMENSION)
            #     ]
            # ),
        ]
    )


def get_board_score(board: Board, last_draw_str: str) -> int:
    last_draw = int(last_draw_str)

    sum_unmarked = 0
    for row in board:
        for n in row:
            if not n.marked:
                sum_unmarked += int(n.value)

    return sum_unmarked * last_draw


with open("2021/4/input.txt") as f:
    sections = f.read().split("\n\n")

    draw_numbers = sections[0].split(",")

    boards: List[Board] = []

    for board_str in sections[1:]:
        boards.append(
            [[Number(n, False) for n in row.split()] for row in board_str.split("\n")]
        )

    solved = [False] * len(boards)

    for n in draw_numbers:
        print(n)
        for i, board in enumerate(boards):
            if not solved[i]:
                mark_drawn_number(n, board)
                if check_for_bingo(board):
                    solved[i] = True
                    score = get_board_score(board, n)

    print(f"last set score: {score}")
