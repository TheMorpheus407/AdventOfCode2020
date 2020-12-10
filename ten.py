with open("ten") as f:
    lines = f.read().splitlines()
    input = [0] + sorted([int(i) for i in lines])
    input = input + [max(input) + 3]

import collections
diffs = [b-a for a, b in zip(input, input[1:])]
differences_dict = collections.Counter(diffs)
print(differences_dict[1] * differences_dict[3])

poss = [1]+[0]*input[-1]
for i in input[1:]:
    poss[i] = poss[i-1] + poss[i-2] + poss[i-3]
print(input)
print(poss[-1])
