'''
wap in python to count how many times a particular item has appeared in the list
'''

a = list(map(int, input("Enter your list: ").split()))
item = int(input("Enter item to be counted: "))
count = a.count(item)
print("The item appeared", count, "times")
