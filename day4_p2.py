import time, re


def load(file):
    with open(file) as f:
        return [row.strip()[row.index(":")+1:].split("|") for row in f]


def solve(p):
    part1 = 0
    card_ammounts = [1] *len(p)
    for card_no, (winning, have) in enumerate(p):
        winning = set(map(int,winning.split()))
        have = set(map(int, have.split()))
        winner = len(winning & have)
        if winner:
            #!part1 += 2**(winner-1)
            for n in range(1, winner+1):
                card_ammounts[card_no+n] += card_ammounts[card_no]
    #!for i in card_ammounts:
     #!   part1 += i
            
    return sum(card_ammounts)  

time_start = time.perf_counter()
print(f'Part 1: {solve(load("aufgaben/day4_p2.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')