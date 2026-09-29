# wap in python to store one student data as tuple: name, rollno and marks and display grade on basis of marks
name = input("Enter student name: ")
rollno = int(input("Enter roll number: "))
marks = int(input("Enter marks: "))

student = (name, rollno, marks)

print("Student data:", student)

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Name:", student[0])
print("Roll No:", student[1])
print("Marks:", student[2])
print("Grade:", grade)