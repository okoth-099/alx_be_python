# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    try:
        # Convert to Celsius using the global conversion factor
        celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        return celsius
    except TypeError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    try:
        # Convert to Fahrenheit using the global conversion factor
        fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        return fahrenheit
    except TypeError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# Prompt the user to enter the temperature
try:
    temp_input = input("Enter the temperature to convert: ")
    temperature = float(temp_input)  # Ensure the input is numeric
    
    # Prompt the user to enter the temperature unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Perform the appropriate conversion based on the user's input
    if unit == "C":
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
    elif unit == "F":
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")

