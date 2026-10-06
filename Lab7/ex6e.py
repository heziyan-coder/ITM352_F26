user_input = input("Enter a value: ")

try:
    my_tuple.append(user_input)
except Exception:
    my_tuple = (*my_tuple, user_input)
print(my_tuple)