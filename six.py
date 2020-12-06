with open("six") as f:
    groups = f.read().split('\n\n')

from functools import reduce
part_one = 0
part_two = 0
for group in groups:
    union_set = reduce(set.union, map(set, group.split()))
    intersection_set = reduce(set.intersection, map(set, group.split()))
    part_one += len(union_set)
    part_two += len(intersection_set)
print(part_one)
print(part_two)
