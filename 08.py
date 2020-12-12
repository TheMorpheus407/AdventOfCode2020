import copy

with open("08.txt") as f:
    boot_sequence = f.read().splitlines()

def part_one():
    acc = 0
    idx_list = [False for _ in boot_sequence]
    idx = 0
    operation = boot_sequence[idx]

    while True:
        idx_list[idx] = True
        op, value = operation.split()
        if op == "nop":
            idx += 1
        elif op == "jmp":
            idx += int(value)
        elif op == "acc":
            acc += int(value)
            idx += 1

        if idx_list[idx] == True:
            break

        operation = boot_sequence[idx]

def part_two(boot_sequence):
    for i in range(len(boot_sequence)):
        boot_copy = copy.deepcopy(boot_sequence)
        if boot_copy[i].split()[0] == "jmp":
            boot_copy[i] = boot_copy[i].replace("jmp", "nop")
        elif boot_copy[i].split()[0] == "nop":
            boot_copy[i] = boot_copy[i].replace("nop", "jmp")

        acc = 0
        idx_list = [False for _ in boot_copy]
        idx = 0
        operation = boot_copy[idx]
        while True:
            idx_list[idx] = True
            op, value = operation.split()

            if op == "nop":
                idx += 1
            elif op == "jmp":
                idx += int(value)
            elif op == "acc":
                acc += int(value)
                idx += 1

            if idx_list[idx] == True:
                break
            if idx == (len(boot_copy) - 1):
                return acc
            operation = boot_copy[idx]
    return -1

print(part_two(boot_sequence))