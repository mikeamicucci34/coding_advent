with open("../inputs/day1.txt", "r") as f:
    data = f.readlines()

data = [int(x) for x in data]

# part one
count = 0
for x, y in zip(data[:-1], data[1:]):
    if y > x:
        count += 1

print(f"part 1: {count}")

# part two
count = 0
for i in range(3, len(data)):
    x = sum(data[i - 3 : i])
    y = sum(data[i - 2 : i + 1])
    if y > x:
        count += 1

print(f"part 2: {count}")
