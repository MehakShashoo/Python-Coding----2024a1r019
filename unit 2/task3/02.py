'''
wap in python to a square pattern of star patterns of n rows and n columns
* * * *
* * * *
* * * *
* * * *
'''

n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()