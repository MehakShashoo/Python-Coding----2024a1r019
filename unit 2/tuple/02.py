# wap in python to store all month name in a tuple, input a month number and display the corresponding month name.

months_tuple = ("January","February","March","April","May","June","July","August","September","October","November","December")
m = int(input("Enter month number: "))
print(f"{m}th month of the year is {months_tuple[m-1]}")
