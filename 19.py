rules_dict = {}
depth_list = [0]

def match_rule(r, m, depth=0):
    depth_list.append(depth)
    if depth == 1000:
        return False, m
    rules = r.split(" | ")
    if len(rules) > 1:
        for rule in rules:
            res, m2 = match_rule(rule, m, depth+1)
            if res:
                return True, m2
        return False, m
    rules = r.split(" ")
    m_prev = m
    res = None
    for rule in rules:
        if rule.isnumeric():
            res, m = match_rule(rules_dict[int(rule)], m, depth+1)
            if not res:
                return False, m_prev
    if res:
        return True, m
    if len(m) >= 1 and m[0] == r:
        return True, m[1:]
    else:
        return False, m


def matches(m):
    res, m2 = match_rule(rules_dict[0], m)
    if res:
        return len(m2) == 0

msg = []
with open("19.txt") as f:
    while (line := f.readline().strip()) != "":
        rule_id, rule = line.split(": ")
        rules_dict[int(rule_id)] = rule.replace("\"", "")
    while line := f.readline().strip():
        msg.append(line)

counter = 0
for m in msg:
    if matches(m):
        counter += 1
print(counter)