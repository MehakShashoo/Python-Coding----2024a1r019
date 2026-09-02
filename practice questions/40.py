# wap to take string and separate characters present at even index positions and odd index positions.
input_string = input("Enter a string: ")


even_index_chars = input_string[::2]


odd_index_chars = input_string[1::2]


print(f"Characters at even index positions: {even_index_chars}")
print(f"Characters at odd index positions: {odd_index_chars}")
