import itertools

numbers = []
with open("09.txt") as f:
    for i in f.read().splitlines():
        numbers.append(int(i))

target = -1
for i in range(25,len(numbers)):
    current = numbers[i]
    for a, b in itertools.combinations(numbers[i-25:i], 2):
        if a + b == current:
            break
    else:
        target = current

head = 0
tail = 0
while head <= len(numbers):
    current_list = numbers[tail:head]
    if len(current_list) < 2:
        head += 1
    sum_list = sum(current_list)
    if sum_list == target:
        print("found solution: ")
        print(max(current_list) + min(current_list))
        break
    elif sum_list < target:
        head += 1
    elif sum_list > target:
        tail += 1