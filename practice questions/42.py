# take a sentence containing double spaces and unwanted spaces at beginning or end and clean the sentence

sentence = input("Enter a sentence : ")

new_sentence = " ".join(sentence.split())

print("Cleaned sentence:", new_sentence)

