user_input = input("Enter a value: ")
try:
    my_tuple.append(user_input)
except Exception as error:
    print("An attempt was made to append a value to the tuple.")
    print(error)