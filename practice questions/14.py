# wap to take an amount in rupee and calculate how many 500 rupee and 100 rupee notes are required

amount = int(input("Enter amount: "))
print(f"{amount // 500} notes of 500 and {amount % 500} notes of 100")