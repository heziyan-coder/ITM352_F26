# ask the user for a sentence (useing input())
# turn the sentence into a list of string (using split())
# remove the list
# join the list back into a string (using Join())
# name:Ziyan He
# date: 9/18/2026

sentence = input("enter a sentence:")
words = sentence.split()
words.reverse()
reversed_sentence = " ".join(words)
print("reversed sentence:", reversed_sentence)

joined_sentence = sentence + " " + reversed_sentence
print("joined_sentence:",joined_sentence)