# wap to take a student name and roll number then generate a username using first 3 letters of the name and last 2 digits of roll number
name = input("Enter name= ")
roll = input("Enter roll number= ")

name_u = name[:3]
roll_u = name[-2:]

username = name_u + roll_u
print(f"Username is {username}")