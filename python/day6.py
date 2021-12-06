from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Population:

    population: defaultdict[int, int]

    @classmethod
    def from_input(cls, data: str) -> "Population":
        dd = defaultdict(int)
        for timer in map(int, data.strip().split(",")):
            dd[timer] += 1
        return cls(population=dd)

    def advance(self) -> None:
        dd = defaultdict(int)

        for timer, count in self.population.items():
            if timer == 0:
                dd[6] += count
                dd[8] += count
            else:
                dd[timer - 1] += count

        self.population = dd

    def size(self) -> int:
        return sum(v for k, v in self.population.items())


# part one
with open("../inputs/day6.txt", "r") as f:
    population = Population.from_input(f.read())

for i in range(80):
    population.advance()

print(f"part one: {population.size()}")


# part two
with open("../inputs/day6.txt", "r") as f:
    population = Population.from_input(f.read())

for i in range(256):
    population.advance()

print(f"part two: {population.size()}")
