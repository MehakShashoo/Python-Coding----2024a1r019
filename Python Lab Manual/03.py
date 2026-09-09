'''
Consider the string “Welcome to Python world”. Perform the following operations: 
Count the number of alphabets in the given string. 
To extract characters in the given, range from the given string. 
Check if the string is alphanumeric or not.
'''

string = "Welcome to Python world"

count = 0

for char in string:
    if char.isalpha():
        count += 1

print("Number of alphabets:", count)

print("Characters from index 0 to 6:", string[0:7])

print("Is the string alphanumeric?", string.isalnum())