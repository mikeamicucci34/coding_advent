import statistics
from typing import Optional

with open("../inputs/day10.txt", "r") as f:
    lines = f.readlines()


# map opening symbols to their closing counterparts
openers = {"(": ")", "[": "]", "{": "}", "<": ">"}


def get_corrupted_score(symbols: str) -> int:
    """Use a stack to process the list of symbols."""
    # map closing symbols to their score
    closers = {")": 3, "]": 57, "}": 1197, ">": 25137}

    stack = []
    for curr in symbols.strip():
        if curr in openers:
            stack.append(curr)  # push

        else:
            # s better be a closer
            assert curr in closers, f"illegal character {curr}"

            opener = stack.pop()
            if curr != openers[opener]:
                return closers[curr]

    return 0


score = 0
for line in lines:
    score += get_corrupted_score(line)

print(f"part one: {score}")


def get_incomplete_score(symbols: str) -> Optional[int]:
    """Use a stack to process the list of symbols."""
    # map closing symbols to their score
    closers = {")": 1, "]": 2, "}": 3, ">": 4}

    stack = []
    for curr in symbols.strip():
        if curr in openers:
            stack.append(curr)  # push

        else:
            # s better be a closer
            assert curr in closers, f"illegal character {curr}"

            opener = stack.pop()
            if curr != openers[opener]:
                # this was a corrupted line, so we ignore it
                return None

    line_score = 0
    for unclosed in reversed(stack):
        closer = openers[unclosed]
        closing_score = closers[closer]

        line_score *= 5
        line_score += closing_score

    return line_score


scores = []
for line in lines:
    score = get_incomplete_score(line)
    if score is not None:
        scores.append(score)

print(f"part two: {statistics.median(scores)}")
