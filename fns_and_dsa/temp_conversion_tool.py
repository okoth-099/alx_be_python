FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

freezing_point = 32

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * fahrenheit - freezing_point

def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + freezing_point

#User interaction

user_temp = float(input("Enter the temperature to convert: "))

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if unit == 'C':
    temperature = convert_to_fahrenheit(user_temp)
    print(f"{user_temp}°{unit} is {temperature}°F")

elif unit == 'F':
    temperature = convert_to_celsius(user_temp)
    print(f"{user_temp}°{unit} is {temperature}°C")

else:
    print("Invalid temperature. Please enter a numeric value.”)
