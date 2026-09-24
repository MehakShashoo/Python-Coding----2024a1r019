'''
wap in python to input numbers in a list and create two separate lists for even and odd numbers
'''
numbers = list(map(int, input("Enter your list: ").split()))


even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)  
    else:
        odd_numbers.append(num)   

print("Original List:", numbers)
print("Even Numbers List:", even_numbers)
print("Odd Numbers List:", odd_numbers)
