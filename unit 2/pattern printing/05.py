'''
wap in python to print a Floyd's triangle
1
2 3
4 5 6
7 8 9 10
'''

number = 1
rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
    print()
