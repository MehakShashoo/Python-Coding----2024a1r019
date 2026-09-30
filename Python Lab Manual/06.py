# Create records of n students. Store each student as a dictionary containing roll number, name, branch, marks. Store all records in a list and search for a student using roll number. Roll numbers must be unique.

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Enter roll number: "))

    exists = 0

    for student in students:
        if student["Roll no"] == roll:
            exists = 1
            break

    if exists == 1:
        print("Roll number already exists. Enter a different roll number.")
        continue

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    student = {
        "Roll no": roll,
        "Name": name,
        "Branch": branch,
        "Marks": marks
    }

    students.append(student)


# Display all students
print("\nStudent Records:")

for student in students:
    print(student)


# Search student
search_roll = int(input("\nEnter roll number to search: "))

found = 0

for student in students:
    if student["Roll no"] == search_roll:
        print("Student found:")
        print(student)
        found = 1
        break

if found == 0:
    print("Student not found")