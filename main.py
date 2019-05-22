# -*- coding: utf-8 -*-
"""
Created on Sun May 19 19:19:19 2019

@author: pratu
"""
import json
from difflib import SequenceMatcher as sm
from difflib import get_close_matches as cm

def getData():       
        global words
        words = json.load(open("C:\\Users\\pratu\\Documents\\MSCS\\Self-Learning\\PracticeProblems\\Projects\\Interactive Dictionary\\data.json"))

def MatchWord(word):
    ratio = 0
    for exitsWord in words.keys():
        if ratio < sm(None, word, exitsWord).ratio():
            ratio = sm(None, word, exitsWord).ratio()
            nearestWord = exitsWord
    if ratio >= 0.8:
        return nearestWord
    else:
        return "0" 
    
def getMeaning(word):
    word = word.lower()
    if(word in words.keys()):
        return words[word]
    elif word.capitalize() in words.keys():
        return words[word.capitalize()]
    elif word.upper() in words.keys():
        return words[word.upper()]
    else:
        nearestWord = MatchWord(word)
        if nearestWord == "0":
            print("Word not found! Please try again!")
        else:
            newWord = input("Word not found! Did you mean %s? Press y/Y for Yes, n/N for No: " %nearestWord)
            if newWord.lower() == 'y':
                return words[nearestWord]
            elif newWord.lower() == 'n':
                return
            else:
                print("Sorry! we didn't understand the input.")
                return
    
getData()
word = input("Please enter a word or type 1 to quit:")
while(word != "1"):
    meaning = getMeaning(word)
    if(type(meaning) == list):
        i = 1
        for mean in meaning:
            print(str(i)+": " + mean)
            i += 1
    else:
        print("1: %s" %meaning)
    word = input("Please enter a word or type 1 to quit:")
print("Thank you for using the application!")



