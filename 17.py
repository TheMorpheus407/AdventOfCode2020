from collections import defaultdict
from itertools import product


def cycle(active, dim):
    diffs = set(product(*([-1, 0, 1] for _ in range(dim))))
    neighbors = defaultdict(lambda: 0)
    active_new = []
    for cell in active:
        for diff in diffs:
            neighbor = tuple(i + j for i, j in zip(cell,diff))
            if neighbor == cell:
                continue
            neighbors[neighbor] += 1
    for cell in neighbors.keys():
        if cell in active:
            if 2 <= neighbors[cell] <= 3:
                active_new.append(cell)
        else:
            if neighbors[cell] == 3:
                active_new.append(cell)
    return active_new

def calc(dim):
    with open("17.txt") as f:
        active = []
        for x, line in enumerate(f.read().splitlines()):
            for y, cell in enumerate(line):
                if cell == "#":
                    active.append((x,y)+ (0,)*(dim-2))
    for i in range(6):
        active = cycle(active, dim)
    print(len(active))
for i in [3,4]:
    calc(i)
exit()