# Read a file of names one line at a time and print each name

with open("names.txt", "r") as file_object:
    while (line := file_object.readline()):
        print(line.strip())

#I used readline() to read one name at a time. 
# The while loop stops when there are no more lines. I used strip() to remove extra spaces and newlines.