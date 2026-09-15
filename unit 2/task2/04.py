'''
wap to check whether a number is a perfect number. A number is perfect if the sum of its proper dividors is equal to the number itself
'''
num = int(input("Enter the number : "))
sums = 0
for i in range(1,num):
  if num % int(i)== 0:
    sums+=i

if num==sums:
  print("Number is perfect number")
else:
  print("Number is not perfect number")