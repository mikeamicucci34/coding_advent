from dataclasses import dataclass
from typing import List, Literal, Tuple, Set


@dataclass
class Fold:

    axis: Literal["x", "y"]
    n: int


@dataclass
class Origami:

    dots: Set[Tuple[int, int]]
    folds: List[Fold]

    @classmethod
    def from_input(cls, data: List[str]) -> "Origami":
        dots = set()
        folds = list()

        for row in data:
            if row.startswith("fold"):
                axis, n = row.lstrip("fold along ").split("=", maxsplit=1)
                fold = Fold(axis=axis, n=int(n))
                folds.append(fold)
            elif row != "\n":
                x, y = map(int, row.strip().split(",", maxsplit=1))
                coords = (x, y)
                dots.add(coords)

        return Origami(dots=dots, folds=folds)

    def _fold(self, *, times: int) -> Set[Tuple[int, int]]:
        dots = self.dots.copy()
        for i in range(times):
            tmp = set()
            fold = self.folds[i]

            for x, y in dots:
                if fold.axis == "x":
                    if x < fold.n:
                        coords = x, y
                        tmp.add(coords)
                    else:
                        coords = fold.n - abs(fold.n - x), y
                        tmp.add(coords)

                if fold.axis == "y":
                    if y < fold.n:
                        coords = x, y
                        tmp.add(coords)
                    else:
                        coords = x, fold.n - abs(fold.n - y)
                        tmp.add(coords)

            dots = tmp
        return dots

    def solve_part_one(self) -> int:
        folded = self._fold(times=1)
        return len(folded)

    def solve_part_two(self) -> str:
        folded = self._fold(times=len(self.folds))
        max_x = max(folded, key=lambda x: x[0])[0] + 1
        max_y = max(folded, key=lambda x: x[1])[1] + 1

        solution = ["." * max_x] * max_y
        for x, y in folded:
            row = solution[y]
            solution[y] = row[:x] + "#" + row[x + 1:]

        return "\n".join(solution)


with open("../inputs/day13.txt", "r") as f:
    lines = f.readlines()

origami = Origami.from_input(lines)

print(f"part one: {origami.solve_part_one()}")
print(f"part two: \n{origami.solve_part_two()}")
