from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_datetime)

#Part 2: Calculate a Future Date

number_of_days = int(input("Enter the number of days to add to the current date: "))



# Function to calculate futuire datie
def calculate_future_date(days):
    current_date = datetime.date.today()  # Get current date
    future_date = current_date + datetime.timedelta(days=days)  # Add days to the current date
    return future_date.strftime("%Y-%m-%d")


# Calculate and print the future date
future_date = calculate_future_date(number_of_days)
print(f"The future date is: {future_date}")

