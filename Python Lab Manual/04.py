# Write a program to perform searching activity using Linear and Binary Search.

# Linear Search
arr = list(map(int, input("Enter elements: ").split()))

target = int(input("Enter element to search: "))

found = 0

for i in range(len(arr)):
    if arr[i] == target:
        print("Linear Search: Element found at index", i)
        found = 1
        break

if found == 0:
    print("Linear Search: Element not found")

# Binary Search
arr.sort()
low = 0
high = len(arr) - 1
found = 0
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print("Binary Search works on sorted array hence: Element found at index", mid)
        found = 1
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

if found == 0:
    print("Binary Search: Element not found")

