# Exercise 5 — First unique character

# Given:

# s = "leetcode"
# Return:

# "l"
# Because l appears once and is the first character that appears only once.

# Then try:

# z = "loveleetcode"
# Answer:

# "v"

s = "leetcode"
z = "loveleetcode"

def main(strg):
    hmap = {}

    for char in strg:
        if(char not in hmap):
            hmap[char] = 1
        else:
            hmap[char] += 1

    correct_entry = return_first_entry_with_value_equal_1(hmap)
    if(correct_entry != -1):
        print(hmap)
        print(correct_entry)
        print(correct_entry[0])


def return_first_entry_with_value_equal_1(hmap):
    it = iter(hmap.items())
    curr_pair = next(it)

    while(curr_pair[1] != 1 and curr_pair != "end"):
        curr_pair = next(it, "end")

    if(curr_pair == "end"):
        return -1
    
    return curr_pair

main(z)