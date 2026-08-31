# wap to take student details like name, roll no, CGPA, and hostel status from the user typecast them into appropriate types and print them with their detected types 
name = input ("Enter name: ")
roll = int(input ("Enter roll no: "))
cgpa = float(input ("Enter cgpa: "))
hosteller = bool(input ("Are you hosteller: "))

print(f"Name is of type {type(name)}")
print(f"Roll no is of type {type(roll)}")
print(f"CGPA is of type {type(cgpa)}")
print(f"Hosteller is of type {type(hosteller)}")