# Read the entire file using readlines()

with open("names.txt", "r") as file_object:
    names = file_object.readlines()
    print(f"Number of names: {len(names)}")
    for name in names:
        print(name.strip())

#I used readlines() to read all names into a list. I used len() to count the names and strip() to remove extra spaces and newlines.