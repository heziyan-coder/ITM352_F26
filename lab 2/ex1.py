# This program prompts the user to enter a number between 1 and 100,  calculates the square of that number, and then prints both the original number and its square.

value_entered = input("enter a number between 1 and 100:")
value_as_integer = int(value_entered)

valuesquared = value_as_integer ** 2

print("you entered:", value_as_integer)
print("the square of your number is:", valuesquared)

print(f"you entered: {value_as_integer}, and the square of that number is: {valuesquared}")