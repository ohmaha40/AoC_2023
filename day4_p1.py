import time, re


def load(file):
    with open(file) as f:
        return [row.strip()[row.index(":")+1:].split("|") for row in f]


def solve(p):
    part1 = 0
    for winning, have in p:
        winning = set(map(int,winning.split()))
        have = set(map(int, have.split()))
        winner = len(winning & have)
        if winner:
            part1 += 2**(winner-1)
    return part1    

time_start = time.perf_counter()
print(f'Part 1: {solve(load("aufgaben/day4_p1.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')