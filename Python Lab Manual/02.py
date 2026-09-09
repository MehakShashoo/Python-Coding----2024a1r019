#write a program to illustrate iteration over the list and dictionary.   

numbers = [10, 20, 30, 40, 50]

print("Elements of the list are:")
for num in numbers:
    print(num)

student = {
    "Name": "Mehak",
    "Age": 20,
    "Course": "CSE"
}

print("\nDictionary elements are:")
for key, value in student.items():
    print(key, ":", value)