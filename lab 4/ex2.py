# define a list of survey responses values (5,7,3,8) and store them
# in a variable. define a tuple of survey responses IDs ((1012, 1035, 1021, and 1053)
# and add these to the list

responses_values = [5, 7, 3, 8]
responses_values.sort()
responses_ids = (1012, 1035, 1021, 1053)
responses_values.append(responses_ids)

print("combined responses values and IDs: ", responses_values)

responses_values_new = [(1012,5), (1035,7), (1021,3), (1053,8)]
print("combined responses values and IDs: ", responses_values_new)

