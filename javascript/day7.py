# happy learned how to putt

import statistics

with open("../day7_mike.txt", "r") as f:
    for line in f:
        amount = line.split(",")

    amount = [int(i) for i in amount]

def gas(array):
    mid = statistics.median(array)
    gas_total = 0

    for i in range(0, len(array)):
        gas_total += abs((array[i]) - mid)

    return gas_total
