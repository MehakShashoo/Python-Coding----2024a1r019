# write a python program to find remainder when a number is divided by z
y = int(input("Enter first number: "))
z = int(input("Enter second number: "))
rem = y%z
if y%z == 0:
    print(f"number is divisible z and remainder is {rem}")
else:
    print("Not divisibleby z")