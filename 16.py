import re
with open("16.txt") as f:
    lines = f.read().splitlines()

rules = {}
ranges = []
for line in lines[:20]:
    name = line.split(":")[0]
    rule = []
    for r in line.split(":")[1].split(" or "):
        rule.append(tuple(int(i) for i in r.split("-")))
    rules[name] = rule
    for i in rule:
        ranges.append(i)

error_rate = 0
tickets = []
for line in lines[25:]:
    values = [int(i) for i in line.split(",")]
    for v in values:
        invalid = True
        for mini, maxi in ranges:
            if mini <= v <= maxi:
                invalid = False
                break
        if invalid:
            error_rate += v
            break
    if not invalid:
        tickets.append(values)

print("Part 1: Error Rate: ", error_rate)
possibilities = {i: list(rules.keys()) for i in range(len(tickets[0]))}
for t in tickets:
    for counter, v in enumerate(t):
        for key in rules.keys():
            possible = False
            for mini, maxi in rules[key]:
                if mini <= v <= maxi:
                    possible = True
            if not possible and key in possibilities[counter]:
                possibilities[counter].remove(key)
changed = True
while changed:
    changed = False
    for key in possibilities:
        if len(possibilities[key]) == 1:
            to_delete = possibilities[key][0]
            for i in possibilities:
                if i == key or not to_delete in possibilities[i]:
                    continue
                possibilities[i].remove(to_delete)
                changed = True

my_ticket = [int(i) for i in lines[22].split(",")]
part2 = 1
for i in possibilities:
    if "departure " in possibilities[i][0]:
        part2 *= my_ticket[i]
print(part2)
exit()