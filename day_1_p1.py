import time, re


def load(file):
    with open(file) as f:
        return [row.strip() for row in f]


def solve(p):
    part1 = 0
    for row in p:
        numbers = re.findall('\d', row)
        part1 += int(numbers[0] + numbers[-1])

    print(part1)

time_start = time.perf_counter()
print(f'Part 1: {solve(load("aufgaben/day_1.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')