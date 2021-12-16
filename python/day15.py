import itertools as it
from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable, List, Tuple, Mapping, Set
import heapq


@dataclass(frozen=True, order=True)
class Node:

    i: int
    j: int


@dataclass(frozen=True)
class Edge:

    src: Node
    dst: Node
    wgt: int


def _valid_neighbors(i: int, j: int, n: int, m: int) -> Iterable[Tuple[int, int]]:
    neighbors = [
        (i, j - 1),
        (i, j + 1),
        (i - 1, j),
        (i + 1, j),
    ]
    yield from filter(lambda x: 0 <= x[0] < n and 0 <= x[1] < m, neighbors)


@dataclass
class Problem:

    grid: List[List[int]]
    n: int
    m: int

    @property
    def vertex_set(self) -> Set[Node]:
        vertex_set = set()
        for i in range(self.n):
            for j in range(self.m):
                vertex_set.add(Node(i=i, j=j))
        return vertex_set

    @classmethod
    def from_input(cls, data: Iterable[str]) -> "Problem":
        grid = []
        for line in data:
            row = [int(x) for x in line]
            grid.append(row)

        n = len(grid)
        m = len(grid[0])

        return cls(grid=grid, n=n, m=m)

    def _djikstra(
        self,
        *,
        src: Node,
        dst: Node,
        vertex_set: Set[Node],
        edges: Mapping[Node, List[Edge]],
    ) -> int:
        dist = {src: 0}
        pq = []
        entry_finder = {}
        counter = it.count()
        REMOVED = "<removed-task>"

        def add_task(task: Node, *, priority: int = 0) -> None:
            if task in entry_finder:
                remove_task(task)
            count = next(counter)
            entry = [priority, count, task]
            entry_finder[task] = entry
            heapq.heappush(pq, entry)

        def remove_task(task: Node) -> None:
            entry = entry_finder.pop(task)
            entry[-1] = REMOVED

        def pop_task() -> Node:
            while pq:
                priority, count, task = heapq.heappop(pq)
                if task is not REMOVED:
                    del entry_finder[task]
                    return task
            raise KeyError("pop from an empty priority queue")

        for vertex in vertex_set:
            if vertex != src:
                dist[vertex] = float("inf")

            add_task(vertex, priority=dist[vertex])

        while len(pq) > 0:
            u = pop_task()

            if u == dst:
                return dist[dst]

            for edge in edges[u]:
                v = edge.dst
                if v in entry_finder:
                    tmp = dist[u] + edge.wgt
                    if tmp < dist[v]:
                        dist[v] = tmp
                        add_task(v, priority=tmp)

        raise ValueError("unsuccessful Djikstra execution")

    def _a_star(
        self,
        *,
        src: Node,
        dst: Node,
        vertex_set: Set[Node],
        edges: Mapping[Node, List[Edge]],
    ) -> int:
        def manhattan_distance(n: Node) -> float:
            return (self.n - n.i) + (self.m - n.j)

        open_set = {src}

        g_score = {v: float("inf") for v in vertex_set}
        g_score[src] = 0

        f_score = {v: float("inf") for v in vertex_set}
        f_score[src] = manhattan_distance(src)

        while len(open_set) > 0:
            current = min(open_set, key=lambda x: f_score[x])

            if current == dst:
                return g_score[current]

            open_set.remove(current)
            for edge in edges[current]:
                neighbor = edge.dst
                score = g_score[current] + edge.wgt
                if score < g_score[neighbor]:
                    g_score[neighbor] = score
                    f_score[neighbor] = score + manhattan_distance(neighbor)
                    if neighbor not in open_set:
                        open_set.add(neighbor)

        raise ValueError("unsuccessful A* execution")

    def solve_part_one(self) -> int:
        edges = defaultdict(list)
        for i in range(self.n):
            for j in range(self.m):
                for ni, nj in _valid_neighbors(i, j, self.n, self.m):
                    node_one = Node(i=i, j=j)
                    node_two = Node(i=ni, j=nj)

                    edge = Edge(src=node_one, dst=node_two, wgt=self.grid[ni][nj])
                    edges[node_one].append(edge)

        src = Node(i=0, j=0)
        dst = Node(i=self.n - 1, j=self.m - 1)
        return self._a_star(src=src, dst=dst, vertex_set=self.vertex_set, edges=edges)

    def solve_part_two(self) -> int:
        repeats = 5

        global_n = repeats * self.n
        global_m = repeats * self.m

        def _compute_wgt(i: int, j: int) -> int:
            i_transitions = i // self.n
            j_transitions = j // self.m

            orig_i = i % self.n
            orig_j = j % self.m
            orig_wgt = self.grid[orig_i][orig_j]
            new_wgt = orig_wgt + i_transitions + j_transitions

            if new_wgt <= 9:
                return new_wgt
            elif 9 < new_wgt <= 18:
                return new_wgt % 9
            else:
                raise ValueError(f"{orig_wgt=}, {i_transitions=}, {j_transitions=}")

        edges = defaultdict(list)
        vertex_set = set()
        for i in range(global_n):
            for j in range(global_m):
                for ni, nj in _valid_neighbors(i, j, global_n, global_m):
                    node_one = Node(i=i, j=j)
                    node_two = Node(i=ni, j=nj)

                    vertex_set.add(node_one)

                    wgt = _compute_wgt(ni, nj)
                    edge = Edge(src=node_one, dst=node_two, wgt=wgt)
                    edges[node_one].append(edge)

        src = Node(i=0, j=0)
        dst = Node(i=global_n - 1, j=global_m - 1)
        return self._djikstra(src=src, dst=dst, vertex_set=vertex_set, edges=edges)


with open("../inputs/day15.txt", "r") as fp:
    data = map(str.strip, fp.readlines())

problem = Problem.from_input(data)
print(f"part one: {problem.solve_part_one()}")
print(f"part one: {problem.solve_part_two()}")
