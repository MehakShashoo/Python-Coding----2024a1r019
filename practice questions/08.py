# wap to calculate simple interest and total amount using principle,rate and time entered by the user
p = int(input("Enter Principal: "))
r  = int(input("Enter Rate: "))
t = int(input("Enter Time: "))
si = (p*r*t)/100
print("Simple Interest: ")
print("Total Amount", p+si)