'''
Create a database using lists and tuples. Each student record must contain roll number, name, branch and CGPA. Store each record as a tuple inside a list. Display all records and search using roll number.
'''
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    cgpa = float(input("Enter CGPA: "))

    student = (roll, name, branch, cgpa)

    students.append(student)


# Display all records
print("\nStudent Records:")

for student in students:
    print(student)


# Search student
search_roll = int(input("\nEnter roll number to search: "))

found = 0

for student in students:
    if student[0] == search_roll:
        print("Student found:")
        print(student)
        found = 1
        break

if found == 0:
    print("Student not found")