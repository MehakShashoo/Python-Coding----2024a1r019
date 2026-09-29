# wap in python to store repeated values in a tuple and count how many times a given value occurs
n = tuple(map(int, input("Enter numbers with repeated values: ").split()))
target = int(input("Enter the value to be counted: "))
count = 0
for i in n:
    if i == target:
        count = count + 1
print(f"Number of times {target} occured is {count}")