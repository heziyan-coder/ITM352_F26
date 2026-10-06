user_input = input("Enter a value: ")
my_list = list(my_tuple)
my_list.append(user_input)
my_tuple = tuple(my_list)

print(my_tuple)