'''
wap in python to print a inverted right angled triangle using stars
* * * *
* * *
* *
*
'''
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i,n):        #range(n-i)
        print("*",end=" ")
    print()