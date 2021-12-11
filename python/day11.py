from copy import deepcopy
from dataclasses import dataclass
from typing import List, ClassVar, Iterable, Tuple


@dataclass
class Problem:

    n: ClassVar[int] = 10

    grid: List[List[int]]

    @staticmethod
    def _valid_neighbors(i: int, j: int, n: int) -> Iterable[Tuple[int, int]]:
        neighbors = [
            (i - 1, j - 1),
            (i - 1, j),
            (i - 1, j + 1),
            (i, j - 1),
            (i, j + 1),
            (i + 1, j - 1),
            (i + 1, j),
            (i + 1, j + 1),
        ]
        return filter(lambda coords: all(0 <= z < n for z in coords), neighbors)

    def _advance_energy_levels(self, _grid: List[List[int]]) -> int:
        # increment all timers
        for i in range(self.n):
            for j in range(self.n):
                _grid[i][j] += 1

        flashed = set()
        finished = False

        def _apply_flashes() -> bool:
            for x in range(self.n):
                for y in range(self.n):
                    coords = (x, y)
                    score = _grid[x][y]
                    if score > 9 and coords not in flashed:
                        flashed.add(coords)
                        for nx, ny in self._valid_neighbors(x, y, self.n):
                            _grid[nx][ny] += 1
                        return False
            return True

        while not finished:
            finished = _apply_flashes()

        for i in range(self.n):
            for j in range(self.n):
                if _grid[i][j] > 9:
                    _grid[i][j] = 0

        return len(flashed)

    def solve_part_one(self) -> int:
        # deepcopy so we can mutate the grid and still
        # have the original copy for part two
        _grid = deepcopy(self.grid)

        num_flashes = 0
        for i in range(100):
            num_flashes += self._advance_energy_levels(_grid)
        return num_flashes

    def solve_part_two(self) -> int:
        # deepcopy so we can mutate the grid and still
        # have the original copy for part two
        _grid = deepcopy(self.grid)

        i = 0
        while True:
            i += 1
            if self._advance_energy_levels(_grid) == self.n ** 2:
                return i


data = []
with open("../inputs/day11.txt", "r") as f:
    for line in f:
        data.append([int(x) for x in line.strip()])


problem = Problem(grid=data)
print(f"part one: {problem.solve_part_one()}")

print(f"part two: {problem.solve_part_two()}")
