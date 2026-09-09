""" Write a python program to detrmine whether a student is eligible for a scholarship
The scholarship should be granted if the student staifies either of the following cond.:
a) The studnet has a CGPA of 8.5 or above and attendence of 85 percent or above.
b) The student has a won a national- level competition

The prgram should take Cgpa , attendce perecentage, and national level competition status as input, then display whether the studnet is eligible for the scholarship.
"""

Cgpa = float(input("Enter your CGPA(1-10) : "))
att_per = float(input("Enter your attendence percentage(1-100) : "))
nat_level = bool(input("Enter Yes/ No for your national level competition status : "))

if Cgpa >=8.5 and att_per >=85 and nat_level == "yes" or "Yes":
    print("Student is eligible for scholarship")
else:
    print("Student is not eligible for scholarship")