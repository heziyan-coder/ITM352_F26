#This program will ask the user to enter weight in pounds and then convert it to kilograms and display the result.
# Name: Ziyan He
# Date: Sept. 4, 2026

#print("The weight in kilogram is:", float(input("enter weight in pounds:"))*0.453592)

KG_TO_POUNDS = 0.453592
weight_in_pounds = input("enter weight in pounds:")
weight_in_pounds_float = float(weight_in_pounds)
weight_in_kilograms = weight_in_pounds_float * KG_TO_POUNDS

print("You entered:", weight_in_pounds)
print("The weight in kilogram is:", weight_in_kilograms)
