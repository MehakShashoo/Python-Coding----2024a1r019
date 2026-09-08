# take an email address and print address,domain and reversed domain

email = input("Enter email address = ")
position = email.find("@")

username = email[:position]
domain = email[position + 1:]
revdomain = domain[::-1]

print("Username = ",username)
print("Domain = ",domain)
print("Reversed Domain = ",revdomain)

