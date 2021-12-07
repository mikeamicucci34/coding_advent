# happy learned how to putt

import statistics

with open("../day7_mike.txt", "r") as f:
    for line in f:
        amount = line.split(",")

    amount = [int(i) for i in amount]

#Solution 1

def gas(array):
    mid = statistics.median(array)
    gas_total = 0

    for i in range(0, len(array)):
        gas_total += abs((array[i]) - mid)

    return gas_total

#Solution 2

def gas(array):
    gas_total = 0

    for i in range(min(array), max(array)):
        curr_gas = 0
        for j in range(0, len(array)):
            triangle_num = abs(i - array[j])
            curr_gas += (triangle_num * (triangle_num + 1))/2
        if curr_gas < gas_total or gas_total == 0:
            gas_total = curr_gas

    return gas_total
