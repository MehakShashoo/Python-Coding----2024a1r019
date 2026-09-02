# wap to take email address and print the domain name
email = input("Enter email= ")
index = email.find("@")
domain = email[index + 1 :]
print(domain)