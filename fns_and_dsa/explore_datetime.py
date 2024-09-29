import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(current_date)

#Part 2: Calculate a Future Date

# Function to calculate future date
def calculate_future_date(days):
    current_date = datetime.date.today()  # Get current date
    future_date = current_date + datetime.timedelta(days=days)  # Add days to the current date
    return future_date

# Prompt user for input
days = int(input("Enter the number of days: "))

# Calculate and print the future date
future_date = calculate_future_date(days)
print(f"The future date is: {future_date}")

