numbers = []
with open("numbers") as f:
    numbers = list(map(int, f.readlines()))

for x in numbers:
    for y in numbers:
        if x+y == 2020:
            print(x*y)

for x in numbers:
    for y in numbers:
        for z in numbers:
            if x+y+z == 2020:
                print(x*y*z)