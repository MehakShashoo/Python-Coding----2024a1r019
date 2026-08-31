# wap to take 2 inputs and swap their values without using a temporary variable but using arithmetic operators

a = int(input("Enter first number= "))
b = int(input("Enter second number= "))
t = a - b
a = a - t
b = b + t
print(f"a = {a}")
print(f"b = {b}")