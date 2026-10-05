# Exercise 6 — Contains Duplicate

# Given:

# nums = [1, 2, 3, 1]
# Return:

# True
# Because 1 appears twice.

# Try:

# nums = [1, 2, 3, 4]
# Return:

# False
# Important: solve it with a dictionary first.

nums = [1, 2, 3, 1]

def main(nums):
    print(contains_duplicate(nums))


def contains_duplicate(nums):
    hmap = {}

    for i in nums:
        hmap[i] = hmap.get(i, 0) + 1


    for (curr_k, curr_v) in hmap.items():
        if(curr_v > 1):
            print(nums)
            print(hmap)
            print(f"({curr_k}, {curr_v})")
            return True

    return False

main(nums)