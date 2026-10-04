# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.

arr = [9,1,2,3,4]

def remove_beginning(arr, i, capacity):
    if(i != capacity - 1):
        for j in range (i, capacity - 1):
            arr[j] = arr[j+1]
    arr[-1] = 0

print("SHIFT ELEMENTS TO THE LEFT:\n")
print(arr)
remove_beginning(arr, 0, 5)
print(arr)