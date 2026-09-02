# wap to take a word and count the number of vowels

# Take a word input from the user
word = input("Enter word: ")

count = 0

vowels = "aeiouAEIOU"
for char in word:
    if char in vowels:
        count += 1

print(f"Number of vowels is {count}")

