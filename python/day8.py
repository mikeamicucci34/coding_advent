from collections import Counter
from dataclasses import dataclass
from typing import List, Dict, Set, Optional, Tuple

Output = Tuple[Optional[int], Optional[int], Optional[int], Optional[int]]


@dataclass
class Solver:

    line: str

    @staticmethod
    def _infer_representations(inputs: List[str]) -> Dict[int, Set[str]]:
        """Infer representation for each number 0-9."""

        def _try_to_parse(
            number: int, signal: str, known: Dict[int, Set[str]]
        ) -> Optional[Set[str]]:
            """Complex logic rules :("""
            ss = set(signal)
            L = len(signal)

            conditions = {
                0: (
                    L == 6
                    and 6 in known
                    and ss != known[6]
                    and 9 in known
                    and ss != known[9]
                ),
                1: L == 2,
                2: (
                    L == 5
                    and 3 in known
                    and ss != known[3]
                    and 5 in known
                    and ss != known[5]
                ),
                3: L == 5 and 1 in known and known[1].issubset(ss),
                4: L == 4,
                5: L == 5 and 6 in known and ss.issubset(known[6]),
                6: L == 6 and 1 in known and not known[1].issubset(ss),
                7: L == 3,
                8: L == 7,
                9: L == 6 and 4 in known and known[4].issubset(ss),
            }

            if conditions[number]:
                return ss
            else:
                return None

        mapper: Dict[int, Set[str]] = {}
        while len(mapper) != 10:
            tmp = {}
            for n in range(10):
                for i in inputs:
                    rep = _try_to_parse(n, i, mapper)
                    if rep is not None:
                        tmp[n] = rep

            mapper = tmp

        return mapper

    def solve(self) -> Output:
        left, right = self.line.split(" | ", maxsplit=1)
        inputs = left.split()
        outputs = right.split()

        int_to_string = self._infer_representations(inputs)

        def _translate(o: str) -> int:
            for k, v in int_to_string.items():
                if set(o) == v:
                    return k
            else:
                raise ValueError()

        a = _translate(outputs[0])
        b = _translate(outputs[1])
        c = _translate(outputs[2])
        d = _translate(outputs[3])

        return a, b, c, d


with open("../inputs/day8.txt", "r") as f:
    data = f.readlines()

results = []
for line in data:
    output = Solver(line).solve()
    results.append(output)


# part one
counter = 0
for x in results:
    for y in x:
        if y in {1, 4, 7, 8}:
            counter += 1

print(f"part one: {counter}")


# part two
_sum = 0
for x in results:
    n = int("".join(map(str, x)))
    _sum += n

print(f"part two: {_sum}")
