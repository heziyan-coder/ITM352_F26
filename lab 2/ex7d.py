#This program will ask the user to enter a temperature in Fahrenheit and then convert it to Celsius and display the result.
#Create the conversion as function
# Name: Ziyan He
# Date: Sept. 4, 2026

def F_to_C(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    rounded_celsius = round(celsius, 2)
    return rounded_celsius


fahrenhei_input = input("Please enter a temperature in Fahrenheit:")
fahrenhei_float = float(fahrenhei_input)

celsius_value = F_to_C(fahrenhei_float)

print("you entered:", fahrenhei_float)
print("the temperature in Celsius is:", celsius_value)
