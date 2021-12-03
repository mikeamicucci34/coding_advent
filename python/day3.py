import operator

# part one
size = 12
ones = [0] * size
zeros = [0] * size

with open("../inputs/day3.txt", "r") as f:
    for line in f:
        for i, b in enumerate(line.strip()):
            if b == "1":
                ones[i] += 1
            elif b == "0":
                zeros[i] += 1
            else:
                raise ValueError(f"unexpected {b=}")

most_common_digit_at_index = lambda j: "1" if ones[j] > zeros[j] else "0"
least_common_digit_at_index = lambda j: "1" if ones[j] < zeros[j] else "0"

gamma_string = "".join(most_common_digit_at_index(j) for j in range(size))
epsilon_string = "".join(least_common_digit_at_index(j) for j in range(size))

print(f"part one: {int(gamma_string, base=2) * int(epsilon_string, base=2)}")


# part 2
with open("../inputs/day3.txt", "r") as f:
    binary = f.readlines()


def pick_binary_string(data, op) -> str:
    array = [x.strip() for x in data]

    k = 0
    while len(array) > 1:

        num_ones, num_zeros = 0, 0
        for bits in array:
            if bits[k] == "1":
                num_ones += 1
            if bits[k] == "0":
                num_zeros += 1

        target = "1" if op(num_ones, num_zeros) else "0"
        array = [x for x in array if x[k] == target]
        k += 1

    return array[0]


oxygen_generator_rating = pick_binary_string(binary, operator.ge)
co2_scrubber_rating = pick_binary_string(binary, operator.lt)

z = int(oxygen_generator_rating, base=2)
w = int(co2_scrubber_rating, base=2)
print(f"part two: {z * w}")