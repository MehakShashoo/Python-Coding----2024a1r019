# wap to take a 2 digit numbers as input and print the sum of its digits
a = input("Enter a two digit number= ")
first = a // 10
sec = a % 10
sum = first + sec 
print(f"sum of digits are = {sum}")
