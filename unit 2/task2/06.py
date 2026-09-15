'''
wap in python to input a decimal number and convert it into binary without using the built-in bin function
'''

number = int(input("Enter the decimal number: "))

new_number = 0
place = 1

while number != 0:
    remainder = number % 2
    number = number // 2

    new_number = new_number + remainder * place
    place = place * 10

print("Binary conversion:", new_number)