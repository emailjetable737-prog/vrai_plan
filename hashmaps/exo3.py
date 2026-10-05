# Exercise 3 — Count characters

# Given:

# s = "banana"
# Produce:

# {
#     "b": 1,
#     "a": 3,
#     "n": 2
# }
# Do not use collections.Counter yet.

s = "banana"

hmap = dict()

for char in s:
    if(char not in hmap):
        hmap[char] = 1
    else:
        hmap[char] += 1

print("{")
for (k,v) in hmap.items():
    if(k == "n"):
        print(f"\t{k}: {v}")
    else:
        print(f"\t{k}: {v},")
print("}")