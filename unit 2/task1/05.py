'''
Write a pp to input marks of 5 students
FOR each studnet , the program should check whether the enterd marks are valid or nvalid. Marks
are considered valid only if they are between 0a and 100. If the marks are invalid, the program should
display "invlaid marks skipped" and move to the next studnet without printing those marks.
if the marks are valid , the program should display the marks as valid
'''
for i in range(1, 6):
    marks = float(input(f"Enter marks for student {i}: "))
    
    if marks < 0 or marks > 100:
        print("invalid marks skipped")
        continue
        
    print(f"Marks {marks} is valid")
