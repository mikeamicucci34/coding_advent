from collections import Counter
from dataclasses import dataclass
from typing import Iterable, Tuple


@dataclass(frozen=True)
class Line:

    x1: int
    y1: int
    x2: int
    y2: int

    @classmethod
    def from_input_line(cls, line: str) -> "Line":
        """Parse a row of the input file."""
        left, right = line.split(" -> ", maxsplit=1)
        x1, y1 = map(int, left.split(",", maxsplit=1))
        x2, y2 = map(int, right.split(",", maxsplit=1))
        return Line(x1=x1, y1=y1, x2=x2, y2=y2)

    def points(self) -> Iterable[Tuple[int, int]]:
        """Yield all points on the line."""
        def delta(a: int, b: int) -> int:
            if a > b:
                return -1
            elif a < b:
                return 1
            else:
                return 0

        dx = delta(self.x1, self.x2)
        dy = delta(self.y1, self.y2)

        x, y = self.x1, self.y1
        while x != self.x2 or y != self.y2:
            yield x, y
            x += dx
            y += dy

        # can't exclude the final point
        yield self.x2, self.y2

    @property
    def is_straight(self) -> bool:
        """Determine whether a bool is perfectly straight."""
        return self.x1 == self.x2 or self.y1 == self.y2


with open("../inputs/day5.txt", "r") as f:
    lines = [Line.from_input_line(x) for x in f.readlines()]


def solve(vents: Iterable[Line]) -> int:
    counter = Counter()
    for line in vents:
        for position in line.points():
            counter[position] += 1

    return sum(1 for k in counter if counter[k] > 1)


part_one = solve(filter(lambda x: x.is_straight, lines))
print(f"{part_one=}")


part_two = solve(lines)
print(f"{part_two=}")
