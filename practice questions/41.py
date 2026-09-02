# take an email address and check whether it contains @ and .com

email = input("Enter your email address: ")

if "@" in email and email.endswith(".com"):
    print("Valid email address.")
else:
    print("Invalid email address. ")
