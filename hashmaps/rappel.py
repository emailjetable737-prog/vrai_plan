# Rappel sur hmap.items(), ou hmap est une hashmap
# hmap.items() retourne les entries/items de hmap
# une entry/item c'est un couple (key, value)
# une entry/item a cette forme (1, 2) ou 1 = key, 2 = value
# on peut recuperer la cle en faisant z[0], ou z est une entry
# on peut recuperer la valeur en faisant z[1], ou z est une entry 

nums = [4, 1, 2, 4, 3, 4, 2, 1, 4]

hmap = {}

for i in nums:
    if(i not in hmap):
        hmap[i] = 1
    else:
        hmap[i] += 1

print(hmap.items())

for entry in hmap.items():
    print(entry)