# wap to take marks of three subjects out of 100, print true if the student scored at least 40 in all three subjects and average marks are atleast 50
english = int(input("Enter marks of english = "))
maths = int(input("Enter marks of maths = "))
science = int(input("Enter marks of science = "))
avg = (english + maths + science) / 3

if english > 40 and maths > 40 and science > 40 and avg > 50 :
    print('True')
else:
    print('False') 