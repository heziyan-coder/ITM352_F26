student_id = input("Enter student ID: ")
num_reqs = int(input("Enter number of requirements: "))

if num_reqs >= 2:
    total = 0
    product = 1

    for digit in student_id:
        number = int(digit)
        total += number

        if number != 0:
            product *= number

    r1 = total % num_reqs + 1
    r2 = product % num_reqs + 1

    if r1 == r2:
        r2 = r2 % num_reqs + 1

    print("Requirement 1:", r1)
    print("Requirement 2:", r2)

else:
    print("Need at least 2 requirements.")