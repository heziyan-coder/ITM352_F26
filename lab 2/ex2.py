# Ask the user to enter their birth year. Calculate their age based on the current year and print it out.
# Name: Ziyan He
# Date: Sept. 2, 2026

birth_year = input("Please enter your birth year: ")
current_year =2026
age = current_year - int(birth_year)

print("You entered:", birth_year)
print("Your age is:" + str(age))
