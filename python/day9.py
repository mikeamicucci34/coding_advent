from typing import List, Tuple, Set
import math


def _get_neighboring_points(i: int, j: int, n: int, m: int) -> List[Tuple[int, int]]:
    """Utility function for retrieving a list of neighboring points."""
    neighbors = []

    if i > 0:
        neighbors.append((i - 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if i < n - 1:
        neighbors.append((i + 1, j))
    if j < m - 1:
        neighbors.append((i, j + 1))

    return neighbors


def is_low_point(i: int, j: int, n: int, m: int, grid: List[List[int]]) -> bool:
    """Determine if grid[i][j] is a so-called low point."""
    neighbors = _get_neighboring_points(i, j, n, m)
    return all(grid[x][y] > grid[i][j] for x, y in neighbors)


def find_basin(
    i: int, j: int, n: int, m: int, grid: List[List[int]]
) -> Set[Tuple[int, int]]:
    already_visited = [[False] * m for _ in range(n)]

    def _find_basin(
        x: int, y: int, *, basin: Set[Tuple[int, int]]
    ) -> Set[Tuple[int, int]]:
        if grid[x][y] == 9 or already_visited[x][y]:
            return basin

        already_visited[x][y] = True

        new_basin = basin.copy()
        new_basin.add((x, y))

        neighbors = _get_neighboring_points(x, y, n, m)
        for args in neighbors:
            new_basin = new_basin.union(_find_basin(*args, basin=new_basin))

        return new_basin

    return _find_basin(i, j, basin=set())


with open("../inputs/day9.txt", "r") as f:
    grid = [[int(x) for x in y.strip()] for y in f]

n = len(grid)
m = len(grid[0])

risk_level = 0
for i in range(n):
    for j in range(m):
        if is_low_point(i, j, n, m, grid):
            risk_level += grid[i][j] + 1

print(f"part one: {risk_level}")


processed = set()
basin_sizes = []
for i in range(n):
    for j in range(m):
        if (i, j) not in processed and grid[i][j] != 9:
            basin = find_basin(i, j, n, m, grid)
            processed = processed.union(basin)
            basin_sizes.append(len(basin))

print(f"part two: {math.prod(sorted(basin_sizes)[-3:])}")
