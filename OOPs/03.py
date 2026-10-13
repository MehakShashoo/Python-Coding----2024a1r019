'''
Create a product class with the product name,price and quantity. Add an instance method to calculate the total cost. Take these values from the user and display the product name and total cost.
'''


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity
name = input("Enter name of product: ")
price = float(input("Enter price of one product: "))
quantity = int(input("Enter quantity of product: "))
p = Product(name, price, quantity)
print(f"Total cost is {p.total_cost()}")
