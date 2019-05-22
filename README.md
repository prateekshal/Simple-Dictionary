# Simple-Dictionary
Inserting a word and either getting the meaning or the closest match of the word.
This is an application that reads a json file which contains words and meanings.
It asks for a user input and if the word exists in the json file, it returns the meaning of the word.
Else if there is a word that is close match to the input, it verifies with the user whether they meant it and returns the meaning of the word.
Else, it returns word not found.
It is implemented in Python using json and difflib library.
json library is used to read the json file containing words and meanings.
Sequence Matcher in Difflib is used to get the closest match word.
