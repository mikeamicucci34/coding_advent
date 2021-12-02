# part one
vertical, horizontal = 0, 0

with open("../inputs/day2.txt", "r") as f:
    for line in f:
        direction, amount = line.split(" ", maxsplit=1)
        amount = int(amount)

        if direction == "forward":
            horizontal += amount
        elif direction == "down":
            vertical += amount
        elif direction == "up":
            vertical -= amount
        else:
            raise ValueError(f"unexpected {direction=}")

print(f"part one: {vertical * horizontal}")

# part two
vertical, horizontal, aim = 0, 0, 0

with open("../inputs/day2.txt", "r") as f:
    for line in f:
        direction, amount = line.split(" ", maxsplit=1)
        amount = int(amount)

        if direction == "forward":
            horizontal += amount
            vertical += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount

        else:
            raise ValueError(f"unexpected {direction=}")

print(f"part two: {vertical * horizontal}")