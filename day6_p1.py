import time, re


def load(file):
    with open(file) as f:
        return [row.strip() for row in f]


def solve(p):
    times = []
    for row in p:
        times.append(list(map(int,re.findall("\d+", row))))
    spiel = 0
    part1 = 1
    for time in times[0]:
        gw = 0
        strecke = 0
        siege = 0
        weg_max = times[1][spiel]
        for i in range(time):
            if (time - gw) * gw > weg_max:
                siege += 1
            gw += 1
        part1 = part1* siege 
        spiel += 1   
    return part1

def solvep2(p):
    part2 =1
    liste = []
    for row in p:
        liste.append(re.findall("\d+",row))
    rennen =""
    for i in liste[0]:
        rennen += i
    distanz =""
    for i in liste[1]:
        distanz += i
    gw = 0
    strecke = 0
    siege = 0
    for i in range(int(rennen)): 
        if (int(rennen) - gw) * gw > int(distanz):
            siege += 1
        gw += 1
    part2 = part2 * siege   
    return part2
    
    
        


time_start = time.perf_counter()
print(f'Part 1: {solve(load("aufgaben/day6_p1.txt"))}')
print(f'Part 2: {solvep2(load("aufgaben/day6_p1.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')