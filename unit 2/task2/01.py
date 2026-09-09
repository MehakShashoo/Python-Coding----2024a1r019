'''
Write a pyhton program that asks the user to enter the user name and password. The user should get only 3 attempts. If the correct credentials are entered, display "login Successful" and stop the loop . If all attempt are used , display "Account Locked"
'''
correct_username = "admin"
correct_password = "python1234"
attempt = 3

while attempt >0:
  username = input("Enter username : ")
  password = input("Enter password : ")
  if username == correct_username and password == correct_password:
    print("Login successful")
    break
  else:
    attempt = attempt-1
    print("Wrong details. Attempt left: ", attempt)
if attempt == 0:
  print("Account Locked")