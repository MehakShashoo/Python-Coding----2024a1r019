"""
Write a python program to stimulate a digital lock system.
The lock should ask the user to enter a 4-digit PIN. If the entered PIN does not conatin exactly 4 digits,the program should display an error message and ask again. if the enterd PIN is correct, the lock should open. Otherwise, the program should ask the user to try again."""

correct_pin = "1234"

while True:
    pin = input("Enter 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("Error: PIN must contain exactly 4 digits.")
        continue
    if pin == correct_pin:
        print("Lock is open")
        break
    else:
        print("Incorrect PIN. Try again.")

