hmap = {
    "Alice": 25,
    "Bob": 31,
    "Charlie": 22
}

def main():
    print("#1")
    if(check_if_present(hmap, "Alice")):
        print("Alice :", hmap["Alice"],"\n")

    print("#2")
    hmap["David"] = 28
    print(hmap)
    print("David : 28 now added to hmap\n")

    print("#3")
    update_value_hmap(hmap, "Bob", 32)
    print("Bob's age now updated to 32\n")
    print(hmap)

    print("#4")
    if(check_if_present(hmap, "Charlie")):
        print(f"Charlie is present, 'Charlie' : {hmap["Charlie"]}\n")

    print("#5")
    if(check_if_present(hmap, "Michael")):
        print(f"Michael is present, 'Michael' : {hmap["Michael"]}\n")

    print("#6")
    if(check_if_present(hmap, "Alice")):
        del hmap["Alice"]
    print("Alice now deleted from hmap\n")
    print(hmap)

    print("#7")
    print(f"len(hmap) : {len(hmap)}")


def check_if_present(hmap, key):
    return (key in hmap)

def update_value_hmap(hmap, key, value):
    if(hmap.get(key, 0) != 0):
        hmap[key] = value

main()