import time, re


def load(file):
    with open(file) as f:
        return [row.strip() for row in f]


def solve(p):
    ids = 0
    for row in p:
        highest = dict(red=0, green=0, blue=0)
        colors = re.findall('red|green|blue', row)
        mengen = list(map(int,re.findall('\d+', row)))
        id = mengen.pop(0)
        for color, menge in zip(colors, mengen):
            highest[color] = max(highest[color], menge)
        if highest["red"] <= 12 and highest["green"] <= 13 and highest["blue"] <= 14:
            ids += id
        print(ids)
    print(ids)
time_start = time.perf_counter()
print(f'Part 1: {solve(load("aufgaben/day2_p1.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')