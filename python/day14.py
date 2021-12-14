from collections import Counter
from dataclasses import dataclass
from typing import Dict, Iterable


@dataclass
class Problem:

    template: str
    rules: Dict[str, str]

    @classmethod
    def from_input(cls, data: Iterable[str]) -> "Problem":
        listed = list(data)
        template = listed[0]

        rules = {}
        for rule in listed[2:]:
            key, value = rule.split(" -> ", maxsplit=1)
            rules[key] = value

        return Problem(template=template, rules=rules)

    def solve_part_one(self) -> int:
        """Solve AoC day fourteen part one."""

        def _apply_polymer_rules(template: str) -> str:
            pieces = [template[0]]
            for x, y in zip(template[:-1], template[1:]):
                key = f"{x}{y}"
                insertion = self.rules.get(key, "")
                pieces.append(f"{insertion}{y}")

            return "".join(pieces)

        polymer = self.template
        for _ in range(10):
            polymer = _apply_polymer_rules(polymer)

        counter = Counter(polymer)
        return counter.most_common()[0][1] - counter.most_common()[-1][1]

    def solve_part_two(self) -> int:
        """We need a more computationally efficient approach."""
        polymer = Counter()

        for x, y in zip(self.template[:-1], self.template[1:]):
            polymer[f"{x}{y}"] += 1

        for _ in range(40):
            update = polymer.copy()
            for pattern, insertion in self.rules.items():
                if pattern in polymer:
                    amt = polymer[pattern]

                    update[pattern] -= amt
                    if not update[pattern]:
                        update.pop(pattern)

                    update[f"{pattern[0]}{insertion}"] += amt
                    update[f"{insertion}{pattern[1]}"] += amt

            polymer = update

        counter = Counter()
        for key, val in polymer.items():
            counter[key[0]] += val
            counter[key[1]] += val

        counter[self.template[0]] += 1
        counter[self.template[-1]] += 1

        return (counter.most_common()[0][1] - counter.most_common()[-1][1]) // 2


with open("../inputs/day14.txt", "r") as f:
    data = map(str.strip, f.readlines())


problem = Problem.from_input(data)
print(f"part one: {problem.solve_part_one()}")
print(f"part two: {problem.solve_part_two()}")
