# wap to take a word and print it in reverse order using slicing also check whether it is the same forward and backward

word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

if word == reversed_word:
    print("The word is the same forward and backward (Palindrome).")
else:
    print("The word is not the same forward and backward.")
