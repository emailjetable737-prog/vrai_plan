# Insert n into arr at the next open position (the next open position
# is always the last position).
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).


arr = [1,2,3,4,0]

def insert_end(n, arr, capacity, length):
    if length < capacity:
        arr[length] = n    

print("INSERT AT THE LAST POSITION THE VALUE OF N:\n")

print(f"{arr}\n")
n = int(input("value of n : "))
insert_end(n, arr, 5, 4)
print(f"\n{arr}")