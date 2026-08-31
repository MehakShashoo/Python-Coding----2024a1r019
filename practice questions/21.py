# wap to take input from the user without typecasting and multiply it by 3 then typecast the same input to int and multiply it by 3 print both results to show the difference
a = input("Enter a number: ")
str_res = a * 3

int_res = int(a) * 3

print("Without typecasting (string multiplication):", str_res)
print("With typecasting (integer multiplication):", int_res)
