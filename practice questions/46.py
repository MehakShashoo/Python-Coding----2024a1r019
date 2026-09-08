# take a password and check length, presence of @ and whether first and last characters are different
password = input("Enter password = ")

password_length = len(password)
print("Length:", password_length)

has_at_symbol = "@" in password
print("Contains '@':", has_at_symbol)

if password_length > 0:
  first_and_last_different = password[0] != password[-1]
else:
  first_and_last_different = False

print("First and last characters are different:", first_and_last_different)
