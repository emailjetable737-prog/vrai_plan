# Exercise 4 — Find the most frequent number

# nums = [4, 1, 2, 4, 3, 4, 2, 1, 4, 4]
# Return:

# 5

nums = [4, 1, 2, 4, 3, 4, 2, 1, 4, 4]

hmap = {}

for i in nums:
    if(i not in hmap):
        hmap[i] = 1
    else:
        hmap[i] += 1


it = iter(hmap.items())
best_pair = next(it)
curr_pair = next(it, "end")

while(curr_pair != "end"):
    if(curr_pair[1] > best_pair[1]):
        best_pair = curr_pair
    curr_pair = next(it, "end")

print(hmap)
print(f"{best_pair} -> {best_pair[1]}")