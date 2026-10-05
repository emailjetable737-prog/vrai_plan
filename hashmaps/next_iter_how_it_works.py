# introduction to next and iter

# iter: transforms an iterable (array, hashmap, etc. for ex) into an iterator

# ex: iter([1,2])

# next: The next function takes an iterator, 
# gives you the element at its current position (first position), 
# and then moves the position forward by one step:

# it = iter([1,2])
# ex: next(it, "end") 

# ("end" is returned, when the end of the iterator has been reached, 
# "end" can be replaced with anything,  including an integer)

numbers = [1,2,3,4]

it = iter(numbers)

a = next(it, "end")
while(a != "end"):
    print(a)
    a = next(it, "end")

print(f"\n{a}")