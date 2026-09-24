'''
wap in python to rotate a list one position to the right
'''
a = list(map(int, input("Enter your list: ").split()))
last=a.pop()
a.insert(0,last)
print("Rotated list:",a)