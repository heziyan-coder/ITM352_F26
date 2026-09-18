# properly format an inputted name in title case

raw_name = input("enter your name: ")

stripped_name = raw_name.strip(" z")
print("stripped name: ", stripped_name)

title_case_name = stripped_name.title()
print("Formatted name in title case: ", title_case_name)
