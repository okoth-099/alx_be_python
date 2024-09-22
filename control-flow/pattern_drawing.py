# pattern_drawing.py

# Step 1: Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Step 2: Use a while loop to iterate through each row
row = 0
while row < size:
    # Nested for loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")  # Print asterisks on the same line
    print()  # Move to the next line after each row
    row += 1

