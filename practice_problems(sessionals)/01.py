# Write a Python program to input a student's marks in n consecutive tests and store them in a list. Find the longest consecutive sequence in which each mark is strictly greater than the previous mark.

# Display the sequence, its length, and its starting and ending test numbers as a tuple. If multiple sequences have the same maximum length, display the first one.

# Conditions:

# Accept at least one test.
# Equal marks break the improving sequence.
# Test numbers begin at 1.
# Do not sort the list because the original test order matters.

marks = list(map(int, input("Enter marks: ").split()))
n = len(marks)
longest = [marks[0]]
current = [marks[0]]
start = 1
longest_start = 1

for i in range(1, n):
    if marks[i] > marks[i - 1]:
        current.append(marks[i])
    else:
        if len(current) > len(longest):
            longest = current.copy()
            longest_start = start

        current = [marks[i]]
        start = i + 1

if len(current) > len(longest):
    longest = current.copy()
    longest_start = start

longest_end = longest_start + len(longest) - 1

print("Longest improving sequence:", longest)
print("Number of tests:", len(longest))
print("Test range:", (longest_start, longest_end))