# Write a program to demonstrate type checking of various data types and demonstrate the use of following built in functions in python: abs(), len(), min(), round(), isalnum(), type().

a = 10
b = 5.7
c = "Hello"
d = True

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of d:", type(d))

print("Absolute value:", abs(-25))

print("Length of string:", len("Python"))

print("Minimum value:", min(10, 5, 20, 2))

print("Rounded value:", round(5.6789, 2))

text = "Python123"
print("Is alphanumeric:", text.isalnum())