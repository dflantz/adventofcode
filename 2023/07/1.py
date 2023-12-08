from collections import defaultdict
from pipe import map, Pipe, sort
from functools import cmp_to_key

LABEL_RANK = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,

}


def get_card_type(card):
    """
    return the type of the card, with 0 being the weakest
    """
    counts = defaultdict(int)
    for s in card:
        counts[s] += 1

    current_rank = 0
    for n_occurrences in sorted(counts.values(), reverse=True):
        if n_occurrences == 5:
            return 10  # five of a kind
        elif n_occurrences == 4:
            return 9  # four of a kind
        elif n_occurrences == 3:
            current_rank = 8  # three of a kind
        elif n_occurrences == 2:
            match current_rank:
                case 8:
                    return 8  # full house
                case 7:
                    return 6  # two pairs
                case 0:
                    current_rank = 7
        elif n_occurrences == 1:
            match current_rank:
                case 8:
                    return 7  # three of a kind
                case 7:
                    return 5  # one pair

    return current_rank  # high card


def compare_cards(card1, card2):
    card_1_type, card_2_type = card1[2], card2[2]
    card_1_value, card_2_value = card1[0], card2[0]

    if card_1_type == card_2_type:
        for c1, c2 in zip(card_1_value, card_2_value):
            if LABEL_RANK[c1] > LABEL_RANK[c2]:
                return 1
            elif LABEL_RANK[c1] < LABEL_RANK[c2]:
                return -1
        return 0

    return 1 if card_1_type > card_2_type else -1


print(
    open("input.txt", "r").readlines()
    | map(lambda x: x.strip().split())
    | map(lambda x: (x[0], int(x[1])))
    | map(lambda x: (*x, get_card_type(x[0])))
    | sort(key=cmp_to_key(compare_cards))
    | Pipe(enumerate) 
    | map(lambda x: ((x[0] + 1) * x[1][1]))
    | Pipe(sum)
)
