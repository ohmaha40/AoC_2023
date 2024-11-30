import time, re


def load(file):
    with open(file) as f:
        return f.read()
##zahlen finden
def num_span(matches):
    return [(int(match.group()), set(range(match.span()[0], match.span()[1]))) for match in matches]
    ##hier wird aus dem string eine Liste mit einer set aus den Zahlen und den koordinaten gebaut.

#symbole finden
def symbol(matches, rl):
    return {match.span()[0]+ delta for match in matches for delta in {-rl-1,-rl+1,-rl,-1,1,+rl,+rl+1,+rl-1}}

def solve(p):
    row_length=p.index("\n")+1
    numbers = num_span(re.finditer("\d+",p))
    symbole = symbol(re.finditer("[^0-9.\n]", p), row_length)
    part1 = sum(n for n,p in numbers if p & symbole)
    return part1
    
    


time_start = time.perf_counter()
print(f'Part 1: {solve(load("aufgaben/day3_p1.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')