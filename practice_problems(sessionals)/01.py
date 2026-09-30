#Write a python program  to input a students marks in n consecutive tests and store them in a list. Find the longest consecutive sequence in which each marks is strictly greater than the previous mark.
#Display the sequeence its length, its starting and ending test numbers as tuple. If multiple sequence have the same maximum length, display the first one.
#Marks :[55,60,68,62,65,70,78,74]
#Longest improving sequence: [62,65,70,78]
#Number of test: 4
#test range:[4,7]
#Conditions:
#Accept at least one test
#Equal marks break the improving sequence
#Test number begin at 1
#Do not sort the list because the original test order matters.


n = int(input("enter the number of tests: "))
marks = []
for i in range(n):
  marks.append(int(input("Enter the marks : ")))

start  = 0
best_start = 0
best_length = 1

for i in range(1,n):
  if marks[i] <= marks[i-1]:
    start = i


  length = i-start+1

  if length > best_length:
    best_start = start
    best_length =length


sequence = marks[best_start:best_start+best_length]
test_range= (best_start+1,best_start+best_length)

print("Longest improvng sequence : ",sequence)

print("Number of tests : ",best_length)

print("Test Range : ",test_range)