first = input("enter your first name: ")
middle_initial = input("enter your middle initial: ")
last = input("enter your last name: ")

full_name = first + " " + middle_initial + " " + last
print("Your full name is: " + full_name)

print(f"your full name using f-string is: {first} {middle_initial} {last}")
print("your full name using percentage formatting is: %s %s %s" % (first, middle_initial, last))
print("your full name using format is: {} {} {}".format(first, middle_initial, last))
print("your full name using list join is: " + " ".join([first, middle_initial, last]))
name_list = [first, middle_initial, last]

print("your full name using unpacking is: {} {} {}".format(*name_list))