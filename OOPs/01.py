'''
Create a class and object: Student details
Create a student class to store a student's name and roll number. Create an object and display the details using an instance method
'''
class student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
    def display_details(self):
        print("Name:",self.name)
        print("Roll number:",self.roll_number)
student1 = student("Mehak" , 19)
student1.display_details()