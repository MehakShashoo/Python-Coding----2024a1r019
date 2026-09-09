'''
Write a python program to create a simple password validation sytem.
The program should repeadly ask the user to enter a password until a avalid passwprd is enterd. A password will be considered valid only if it has at least 8 character and contain @ symbol.
Once the user enter a valid password, the program should display "Password accepted." and stop. Otherwise, it should display "Weak passowrd. Try again."
and ask for the password again
'''

while True:
  password = input("Enter a password: ")

  if len(password) >= 8 and "@" in password:
    print("Password accepted.")
    break
  else:
    print("Weak password. Try again.")
