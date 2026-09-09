'''
wap in python to detect whether a comment is spam or not. A comment shoulb be treated as spam if it contains any of these keybwords-'buy now' , 'subscribe this' , 'click this'
'''


comment = input("Enter a comment: ")

if "buy now" in comment or "subscribe this" in comment or "click this" in comment:
    print("This comment is spam.")
else:
    print("This comment is not spam.")