import time
import re


def load(file):
  with open(file) as f:
    return f.read().split('\n\n')


def solve(p):
  numbers = [list(map(int, re.findall('\d+', part))) for part in p]
  seeds, converters = numbers[0], numbers[1:]
  part1 = part2 = float('inf')

  for seed in seeds:
    for converter in converters:
      for i in range(0, len(converter), 3):
        dest, source, rng = converter[i:i + 3]
        if seed < source or seed > (source + rng - 1): continue
        seed = seed - source + dest
        break
    part1 = min(part1, seed)

  pairs = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
  for low, high in pairs:
    while low < high:
      seed = low
      low = -1
      for converter in converters:
        for i in range(0, len(converter), 3):
          dest, source, rng = converter[i:i + 3]
          if seed < source or seed > (source + rng - 1): continue
          if low == -1: low = source + rng
          seed = seed - source + dest
          break
      part2 = min(part2, seed)

  return part1, part2



time_start = time.perf_counter()
print(f'Part 1: {solve(load("aufgaben/day5_p1.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')