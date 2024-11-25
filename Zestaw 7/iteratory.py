import itertools
import random


def binary_alternator():
    return itertools.cycle([0, 1])

iterator_a = binary_alternator()
for _ in range(10):
    print(next(iterator_a), end=" ")

print("\n")
def random_walk():
    directions = ["N", "E", "S", "W"]
    while True:
        yield random.choice(directions)

iterator_b = random_walk()
for _ in range(10):
    print(next(iterator_b), end=" ")

print("\n")
def week_days():
    return itertools.cycle(range(7))

iterator_c = week_days()
for _ in range(15):
    print(next(iterator_c), end=" ")
