# Open a file and read its contents

with open("names.txt", "r") as file_object:
    contents = file_object.read()
    print(contents)
    contents_list = contents.split("\n")
    print(f"Number of names: {len(contents_list)}")
    for name in contents_list:
        print(name)


#I used split("\n") to separate the names into a list. Then I used len() to count the number of names.