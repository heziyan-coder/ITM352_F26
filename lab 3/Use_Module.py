import HandyMath

#get two numbers from the user for HandyMath Calculations
input1 = float(input("Enter the first number: "))
input2 = float(input("Enter the second number: "))

#Display the results of calculated by functions from the HandyMath module
midpoint = HandyMath.midpoint(input1, input2)
squareroot = HandyMath.squareroot(input1)
exponent = HandyMath.exponent(input1, input2)
max_value = HandyMath.max(input1, input2)
min_value = HandyMath.min(input1, input2)

#Display the results of calculated by functions from the HandyMath module
print(f"The midpoint of {input1} and {input2} is: {midpoint}")
print(f"The square root of {input1} is: {squareroot}")
print(f"The exponent of {input1} and {input2} is: {exponent}")
print(f"The maximum of {input1} and {input2} is: {max_value}")
print(f"The minimum of {input1} and {input2} is: {min_value}")