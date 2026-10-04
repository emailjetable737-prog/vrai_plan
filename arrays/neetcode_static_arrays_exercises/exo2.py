# Remove from the last position in the array if the array
# is not empty (i.e. length is non-zero).

def remove_end(arr, capacity):
    if(capacity > 2 and arr[-1] != 0):
        arr[-1] = 0

arr =  [2,3,4]
print("REMOVE THE LAST ELEMENT:\n")
print(f"{arr}\n")
remove_end(arr, 3)
print(arr)