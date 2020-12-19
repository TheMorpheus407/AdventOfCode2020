import re

def build_rules(r, depth=0):
    try:
        if int(r) == 8:
            return f"(?:{build_rules(42)})+"
        if int(r) == 11:
            if depth < 20:
                return f"(?:{build_rules(42)}{build_rules(11, depth+1)}?{build_rules(31)})"
            else:
                return f"(?:{build_rules(42)}{build_rules(31)})"
        rule = rules_dict[int(r)]
        regex = ""
        for part in rule.split("|"):
            regex += "|"
            for i in part.split(" "):
                regex += build_rules(i.strip())
        regex = regex[1:]
        regex = "(?:" + regex + ")"
        return regex
    except ValueError:
        if r == "a" or r == "b":
            return r
        else:
            return ""

rules_dict ={}
msg = []
with open("19.txt") as f:
    while (line := f.readline().strip()) != "":
        rule_id, rule = line.split(": ")
        rules_dict[int(rule_id)] = rule.replace("\"", "")
    while line := f.readline().strip():
        msg.append(line)

regex = re.compile(build_rules(0))
print(regex)
counter = 0
for m in msg:
    if regex.fullmatch(m):
        counter += 1
print(counter)