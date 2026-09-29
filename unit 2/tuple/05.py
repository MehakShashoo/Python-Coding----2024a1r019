# wap in python to check whether a given value is present in a tuple.If present, display its position.
n = tuple(map(int,input("Enter values of tuple: ").split()))
target = int(input("Enter the value to be searched: "))
found = False

for i in range (len(n)):
    if i == target:
        print(f"{target} is at {i+1} position")
        found = True
if found == False:
    print("Data not found!")