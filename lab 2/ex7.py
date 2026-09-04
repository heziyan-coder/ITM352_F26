#This program will ask the user to enter a temperature in Fahrenheit and then convert it to Celsius and display the result.
# Name: Ziyan He
# Date: Sept. 4, 2026

fahrenhei_input = input("Please enter a temperature in Fahrenheit:")
fahrenhei_float = float(fahrenhei_input)

celsius_value = (fahrenhei_float - 32) * 5 / 9

celsius_value = round(celsius_value, 2)

print("you entered:", fahrenhei_float)
print("the temperature in Celsius is:", celsius_value)