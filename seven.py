import re

with open("seven") as f:
    lines = f.readlines()

graph = {}

for i in lines:
    regex = re.match('(.+?) bags', i)
    color_primary = regex.group(1)
    color_inside = re.findall('(\d+) (.+?) bag', i)
    if len(color_inside) > 0:
        color_inside = color_inside
        graph[color_primary] = color_inside
        print(color_inside)
    else:
        graph[color_primary] = [('0', '')]


def shiny_gold(color):
    if color == "shiny gold":
        return True
    elif color == "":
        return False
    else:
        return any(shiny_gold(child) for amount, child in graph[color])

print("part 1: ", sum(shiny_gold(color) for color in graph.keys())-1)

def count(color):
    if color == "":
        return 1
    return 1 + sum(int(amount)*count(child) for amount, child in graph[color])
print(count("shiny gold")-1)