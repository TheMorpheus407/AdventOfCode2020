import re
import string
with open("18.txt") as f:
    lines = f.read().splitlines()

def evaluate1(line):
    normal_pattern = re.compile(r"(\d+) ([+*]) (\d+)")
    replace_parentheses = re.compile(r"\((\d+)\)")
    while True:
        line = re.sub(replace_parentheses, r"\1", line)
        if match := re.search(normal_pattern, line):
            right, operator, left = match.groups()
            if operator == "+":
                val = int(right) + int(left)
            elif operator == "*":
                val = int(right) * int(left)
            line = line[:match.start()] + str(val) + line[match.end():]
        else:
            return int(line)

def evaluate2(line):
    multiply_pattern = re.compile(r"(\d+) \* (\d+)(?! \+)")
    add_pattern = re.compile(r"(\d+) \+ (\d+)")
    replace_parentheses = re.compile(r"\((\d+)\)")
    while True:
        print(line)
        line = re.sub(replace_parentheses, r"\1", line)
        if match := re.search(add_pattern, line):
            right, left = match.groups()
            val = int(right) + int(left)
            line = line[:match.start()] + str(val) + line[match.end():]
        else:
            for match in re.finditer(multiply_pattern, line):
                right, left = match.groups()
                val = int(right) * int(left)
                line = line[:match.start()] + str(val) + line[match.end():]
                break
            else:
                return int(line)

def evaluate2_2(line):
    tokens = line.split(" ")
    idcs = [i for i, t in enumerate(tokens) if t == "+"]
    for i in idcs:
        tokens[i-1] = '(' + tokens[i-1]
        tokens[i+1] = tokens[i+1] + ")"
    string = ' '.join(tokens)
    return eval(string)

result1 = 0
result2 = 0
result2_2 = 0
for line in lines:
    result1 += evaluate1(line[:])
    result2 += evaluate2(line[:])
    result2_2 += evaluate2_2(line[:])
print(result1)
print(result2)
print(result2_2)
