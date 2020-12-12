with open("12.txt") as f:
    lines = f.read().splitlines()
    route = [(i[0], int(i[1:])) for i in lines]

def part2(route):
    waypoint = [1, 10, 0, 0]
    pos = [0,0]
    for op, amount in route:
        if op == "F":
            pos[0] += amount*(waypoint[1]-waypoint[3])
            pos[1] += amount*(waypoint[0]-waypoint[2])
        elif op == "N":
            waypoint[0] += amount
        elif op == "S":
            waypoint[2] += amount
        elif op == "E":
            waypoint[1] += amount
        elif op == "W":
            waypoint[3] += amount
        elif op == "R":
            amount = amount//90
            for i in range(amount):
                waypoint = [waypoint[3]] + waypoint[:3]
        elif op == "L":
            amount = amount//90
            for i in range(amount):
                waypoint = waypoint[1:] + [waypoint[0]]
    print(abs(pos[0]) + abs(pos[1]))

def part1(route):
    pos = [0,0]
    current_rotation = 0
    rotation = {
        0: "E",
        90: "S",
        180: "W",
        270: "N"
    }
    for op, amount in route:
        orientation = rotation[current_rotation]
        if op == "F":
            op = orientation

        if op == "N":
            pos[1] += amount
        elif op == "S":
            pos[1] -= amount
        elif op == "E":
            pos[0] += amount
        elif op == "W":
            pos[0] -= amount
        elif op == "R":
            current_rotation = (current_rotation + amount) % 360
        elif op == "L":
            current_rotation = (current_rotation - amount) % 360
    print(abs(pos[0]) + abs(pos[1]))


if __name__ == "__main__":
    part2(route)