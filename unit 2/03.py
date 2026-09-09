'''
Write a pp to calculate the final bill amount after applying a discount. The program should take the total bill amount as input from the user
and apply the discount according to the following rules. After calculating the discount, the program should display the discount amount and 
 final bill amount payableby the customer.
       BillAmount            Discount
        Above5000            20 percent
        below3000            No discount
        3000to5000           10 percent
'''

amount = int(input("Enter the bill amount: "))
if amount>5000:
  print("After 20 percent discount new amount is: ",amount-(amount*0.2))
elif amount>=3000 and amount<=5000:
  print("After 10 percent discount new amount is: ",amount-(amount*0.1))
else:
  print("No discount, The amount is :",amount)