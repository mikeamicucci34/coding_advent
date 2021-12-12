from collections import defaultdict, Counter
from dataclasses import dataclass
from typing import List, Set


def _is_big_cave(node: str) -> bool:
    return node.upper() == node


@dataclass
class Graph:

    adjacency_list: defaultdict[str, List[str]]

    @classmethod
    def from_input(cls, lines: List[str]) -> "Graph":
        adjacency_list = defaultdict(list)
        for line in lines:
            a, b = line.strip().split("-", maxsplit=1)
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
        return cls(adjacency_list)

    def _get_neighbors(self, *, of: str) -> List[str]:
        return self.adjacency_list[of]

    def _small_caves(self) -> Set[str]:
        return {
            x
            for x in self.adjacency_list
            if not _is_big_cave(x) and x not in ["start", "end"]
        }

    def solve_part_one(self) -> int:
        """Count number of distinct routes from start to end."""

        def _count_routes(node: str, visited_set: Set[str]) -> int:
            _visited_set = visited_set.copy()
            _visited_set.add(node)

            counter = 0
            for neighbor in self._get_neighbors(of=node):

                if neighbor == "end":
                    counter += 1

                elif neighbor not in _visited_set or _is_big_cave(neighbor):
                    counter += _count_routes(neighbor, _visited_set)

            return counter

        return _count_routes("start", visited_set=set())

    def solve_part_two(self) -> int:
        """Count number of distinct routes from start to end."""

        def _count_routes(node: str, visitations: Counter[str]) -> int:
            _visitations = visitations.copy()
            _visitations[node] += 1

            can_make_second_small_cave_visit = all(
                _visitations[x] < 2 for x in self._small_caves()
            )

            counter = 0
            for neighbor in self._get_neighbors(of=node):

                if neighbor == "end":
                    counter += 1

                elif neighbor == "start":
                    continue

                elif (
                    _is_big_cave(neighbor)
                    or _visitations[neighbor] == 0
                    or can_make_second_small_cave_visit
                ):
                    counter += _count_routes(neighbor, _visitations)

            return counter

        return _count_routes("start", visitations=Counter())


with open("../inputs/day12.txt", "r") as f:
    data = f.readlines()

graph = Graph.from_input(data)

print(f"part one: {graph.solve_part_one()}")
print(f"part two: {graph.solve_part_two()}")
