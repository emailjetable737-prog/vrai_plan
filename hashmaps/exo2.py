# Exercise 2 — Count numbers

# Given:

# nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# Produce:

# {
#     1: 1,
#     2: 2,
#     3: 3,
#     4: 4
# }
# Constraint: use a dictionary.

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

hmap = dict()

def main():
    for i in nums:
        if(i in hmap):
            hmap[i] += 1
        else:
            hmap[i] = 1

    print(f"{nums}\n")

    print("{")
    for (k, v) in hmap.items():
        if(k == 4):
            print(f"\t{k} : {v}")
        else:
            print(f"\t{k} : {v},")
    print("}")

main()