from HandyMath import max, min

input1 = float(input("Enter the first number: "))
input2 = float(input("Enter the second number: "))

max_value = max(input1, input2)
min_value = min(input1, input2)

print(f"The maximum of {input1} and {input2} is: {max_value}")
print(f"The minimum of {input1} and {input2} is: {min_value}")