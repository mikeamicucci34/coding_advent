import statistics

with open("../inputs/day7.txt", "r") as f:
    data = [int(x) for x in f.read().strip().split(",")]

median = statistics.median(data)
energy_usage = sum(abs(median - x) for x in data)
print(f"part one: {energy_usage}")


def f(x_i: int, x_0: int) -> int:
    """Compute total cost of realignment.

    Uses the arithmetic series sum formula:
    1 + 2 + ... + n = (n^2 + n) / 2

    :param
        x_i: starting point
        x_0: ending point
    """
    z = x_i - x_0
    return (z ** 2 + abs(z)) / 2


cost = float("inf")
for j in range(min(data), max(data)):
    test = sum(f(x_i=x, x_0=j) for x in data)
    if test < cost:
        cost = test

print(f"part two: {cost}")
