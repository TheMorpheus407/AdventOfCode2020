f = open('three')
biome = [line.replace('\n', '') for line in f]
f.close()

list_right = [1, 3, 5, 7, 1]
list_down = [1, 1, 1, 1, 2]

alltogether = 1

for i in range(len(list_right)):
    counter = 0
    right = list_right[i]
    down = list_down[i]
    position_x = 0

    for position_y in range(0, len(biome), down):
        if biome[position_y][position_x] == "#":
            counter += 1
        position_x = (position_x + right) % len(biome[0])
    print(counter)
    alltogether *= counter
print(alltogether)
