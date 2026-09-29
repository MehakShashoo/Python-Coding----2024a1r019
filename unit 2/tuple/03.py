# wap in python to show that tuple value cannot be changed directly. Convert into list, update it and convert it back into tuple

numbers = (10, 20, 30, 40)
print("Original tuple:", numbers)

# Trying to change tuple directly
# numbers[1] = 25
# gives TypeError because tuples cannot be changed.

numbers_list = list(numbers)
numbers_list[1] = 25
numbers = tuple(numbers_list)
print("Updated tuple:", numbers)