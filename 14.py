import itertools
with open("14.txt") as f:
    lines = f.read().splitlines()

def mask_value(mask, value):
    binary_value = list(reversed(bin(value)))
    new_value = ""
    for counter, i in enumerate(reversed(mask)):
        if i == "0" or i == "1":
            new_value = i + new_value
            continue
        idx = counter
        if idx < len(binary_value) - 2:
            new_value = binary_value[idx] + new_value
        else:
            new_value = "0" + new_value
    return int(new_value, 2)

def floating(addr):
    xs = addr.count("X")
    addrs = []
    for i in itertools.product([0,1], repeat=xs):
        new_addr = addr[:]
        for char in i:
            new_addr = new_addr.replace("X", str(char), 1)
        addrs.append(new_addr)
    return addrs

def mask_addresses(mask, addr):
    binary_value = list(reversed(bin(addr)))
    new_addr = ""
    for counter, i in enumerate(reversed(mask)):
        if i == "1":
            new_addr = i + new_addr
        elif i == "0":
            idx = counter
            if idx < len(binary_value) - 2:
                new_addr = binary_value[idx] + new_addr
            else:
                new_addr = "0" + new_addr
        elif i == "X":
            new_addr = i + new_addr
    return floating(new_addr)
    return int(new_addr, 2)

mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
memory = {}
memory_2 = {}
for i in lines:
    inp = i.split(" = ")
    if inp[0] == "mask":
        mask = inp[1]
    else:
        addr = int(inp[0][4:-1])
        value = int(inp[1])
        memory[addr] = mask_value(mask, value)
        #PART 2
        addrs = mask_addresses(mask, addr)
        for i in addrs:
            memory_2[i] = value
print(sum(memory.values()))
print(sum(memory_2.values()))