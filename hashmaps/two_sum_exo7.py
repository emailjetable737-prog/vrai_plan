nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    hmap = {}

    for i in range (0, len(nums)):
        hmap[nums[i]] = i

    for (k, v) in hmap.items():
        if(target - k) in hmap:
            return (v, hmap[target-k])

    return -1

print(f"nums : {nums}")
print(f"target : {target}")
print(two_sum(nums, target))