# try to append to a tuple. It won't work.
# name: Ziyan He
# Date: 2026-9-16

survey_respondents = (1012, 1035, 1021, 1053)
#survey_respondents.append(1011) #This will raise an AttributeError because tuples are immutable

survey_respondents = survey_respondents + (1011,) #This will create a new tuple with the additional element
print("Updated survey_respondents: ", survey_respondents)
