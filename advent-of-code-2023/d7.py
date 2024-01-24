from enum import Enum
from collections import Counter

lines = [line.split() for line in open("d7.in").read().splitlines()]

part1_chars = "AKQJT987654321"
part1_char_to_score = {char: idx for idx, char in enumerate(part1_chars[::-1])}

part2_chars = "AKQT987654321J"
part2_chars_to_score = {char: idx for idx, char in enumerate(part2_chars[::-1])}


class Score(Enum):
    FIVE_OF_A_KIND = 5
    FOUR_OF_A_KIND = 4
    FULL_HOUSE = 3.5
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    PAIR = 1
    HIGH = 0

    def __lt__(self, other):
        return self.value < other.value


def part1_score(hand: str):
    c = Counter(hand)
    scores = [part1_char_to_score[char] for char in hand]
    _type = 0
    common = c.most_common()
    _, num1 = common[0]
    _, num2 = common[1] if len(common) > 1 else (0, 0)

    if len(common) == 1:
        _type = Score.FIVE_OF_A_KIND
    elif num1 == 4:
        _type = Score.FOUR_OF_A_KIND
    elif num1 == 3 and num2 == 2:
        _type = Score.FULL_HOUSE
    elif num1 == 3 and num2 != 2:
        _type = Score.THREE_OF_A_KIND
    elif num1 == 2 and num2 == 2:
        _type = Score.TWO_PAIR
    elif num1 == 2 and num2 != 2:
        _type = Score.PAIR
    elif num1 == 1:
        _type = Score.HIGH

    return tuple([_type, *scores])


def part2_score(hand: str):
    c = Counter(hand)
    jokers = c.get("J", 0)
    del c["J"]

    scores = [part2_chars_to_score[char] for char in hand]
    _type = 0
    common = c.most_common()
    _, num1 = common[0] if len(common) >= 1 else (0, 0)
    _, num2 = common[1] if len(common) > 1 else (0, 0)
    if num1 + jokers == 5:
        _type = Score.FIVE_OF_A_KIND
    elif num1 + jokers == 4:
        _type = Score.FOUR_OF_A_KIND
    elif num1 + jokers == 3 and num2 == 2:
        _type = Score.FULL_HOUSE
    elif num1 + jokers == 3 and num2 != 2:
        _type = Score.THREE_OF_A_KIND
    elif num1 + jokers == 2 and num2 == 2:
        _type = Score.TWO_PAIR
    elif num1 + jokers == 2 and num2 != 2:
        _type = Score.PAIR
    elif num1 == 1:
        _type = Score.HIGH

    return tuple([_type, *scores])


def compute_total(hands, score_func):
    s_lines = sorted(hands, key=lambda line: score_func(line[0]))
    total = 0
    for idx, line in enumerate(s_lines):
        total += (idx + 1) * int(line[1])
    return total


print(compute_total(lines, part1_score))
print(compute_total(lines, part2_score))
