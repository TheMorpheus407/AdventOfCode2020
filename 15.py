def memory(nums, turns):
    num_dict = {num: counter + 1 for counter, num in enumerate(nums[:-1])}
    last = nums[-1]
    for i in range(len(nums), turns):
        if last in num_dict:
            new = i - num_dict[last]
        else:
            new = 0
        num_dict[last] = i
        last = new
    return last


with open("15.txt") as f:
    inp = f.read().strip().split(",")
nums = [int(i) for i in inp]
import timeit
print(timeit.timeit("memory(nums, 1000)", number=1000, globals=locals())*30000000/(1000*1000))
print(memory(nums, 2020))
print(memory(nums, 30000000))