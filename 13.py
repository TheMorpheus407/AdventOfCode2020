with open("13.txt") as f:
    inp = f.read().splitlines()
    earliest_departure = int(inp[0])
    buses = [int(i) for i in inp[1].split(',') if i != "x"]
    part_2 = []
    for counter, i in enumerate(inp[1].split(',')):
        if i != "x":
            part_2.append((-counter, int(i)))

def funk_part_1(buses, earliest_departure):
    best = 99999999999999
    found = False
    bus = -1
    for p in buses:
        n_before = earliest_departure // p
        x = 0
        if (earliest_departure % p) != 0:
            x = 1
        wait = (n_before + x) * p - earliest_departure
        if best > wait:
            best = wait
            bus = p
    print("Bus: ", bus)
    print("Waiting Time: ", best)
    print("Solution for part1: ", best * bus)

def gcd(a,b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = gcd(b % a, a)
    return (g, x - (b // a) * y ,y)

def modular_inverse(n, p):
    g, inv, y = gcd(n, p)
    assert g == 1
    return inv % p

def chinese_remainder_theorem(buses, modulo):
    x = 0
    for a, p in buses:
        n = modulo // p
        inverse = modular_inverse(n, p)
        x = (x+a*n*inverse) % modulo
    return x % modulo


def funk_part_2(buses):
    #0 = 19*x - t
    #-9 = 41*x - t
    modulo = 1
    for i in buses:
        modulo *= i[1]
    print(modulo)
    print(chinese_remainder_theorem(buses, modulo))

if __name__ == "__main__":
    funk_part_1(buses, earliest_departure)
    funk_part_2(part_2)
