# wap to take 2 inputs and swap their values using a temporary variable and print updated values
a = int(input("Enter first number= "))
b = int(input("Enter second number= "))
c = 0
c = b
b = a
a = c
print(f"a = {a}")
print(f"b = {b}")