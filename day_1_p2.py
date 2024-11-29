import time, re


def load(file):
    with open(file) as f:
        return [row.strip() for row in f]


def solve(p):
    replacements = [("one", "one1one"),("two","two2two"),("three","three3three"),("four","four4four"),
                    ("five","five5five"),("six","six6six"),("seven","seven7seven"),("eight","eight8eight"),
                    ("nine","nine9nine")]
    part2 = 0
    for row in p:
        for a,b in replacements:
            row = row.replace(a,b)
        numbers = re.findall("\d", row)
        part2 += int(numbers[0] + numbers[-1])
    print(part2)


time_start = time.perf_counter()
print(f'Part 1: {solve(load("aufgaben/day_1_p2.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')