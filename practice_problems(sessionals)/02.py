'''
Write a Python program to allocate seats to a group in a single row of a cinema hall. First, input the total number of seats n. Then enter the status of each seat:

0 means the seat is available.
1 means the seat is already booked.

Next, input the number of people in the group. The program must find the first consecutive block of available seats that can accommodate the entire group.

If such a block is found:

Book all those seats by changing their status from 0 to 1.
Display the allocated seat numbers in a tuple.
Display the updated list of seat statuses.

If no consecutive block of seats is available, display a message indicating that no suitable block is available and print the original list without changing it.

Conditions:

Seat numbering starts from 1.
The group size must be at least 1 and cannot exceed n.
All group members must be allocated together in consecutive seats.
If more than one suitable block exists, allocate the first block from the left.
If there is no suitable block, leave the original list unchanged.
'''