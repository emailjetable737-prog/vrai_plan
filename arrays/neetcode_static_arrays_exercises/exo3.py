# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.

arr = [2,3,4,5,0]

def insert_middle(arr, i, n, capacity):
    for j in range (capacity - 1, i, -1):
        arr[j] = arr[j - 1]
    arr[i] = n

print("INSERT AT THE iTH POSITION THE VALUE OF N:\n")
print(f"{arr}\n")

n = int(input("value of n : "))
i = int(input("value of i : "))

insert_middle(arr, i, n, 5)
print(f"\n{arr}")