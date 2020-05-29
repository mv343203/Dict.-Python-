import json
from difflib import get_close_matches  

#storage
#dictionaryStorage = python dict type converted from json file with imported library 
dictionaryStorage = json.load(open("dictionary.json"))

# function with conditionals and string case methods(upper, lower, title) to attempt to return definition for user
#imported difflib linrary for matching of word with dictionary storage data
def definitionRetrieval(word): 
    word = word.lower()  
    if word in dictionaryStorage: 
        return dictionaryStorage[word]  
    elif word.title() in dictionaryStorage:
        return dictionaryStorage[word.title()]
    elif word.upper() in dictionaryStorage: 
        return dictionaryStorage[word.upper()]
    elif len (get_close_matches(word, dictionaryStorage.keys())) > 0: 
         yn = input("Did you mean %s instead? Enter Y if yes, or N if no:" % get_close_matches(word, dictionaryStorage.keys())[0]) #% allows for replacement variable
         if yn == "Y":
             return dictionaryStorage [get_close_matches(word, dictionaryStorage.keys())[0]]    
         elif yn == "N":
             return "The word does not exist. Please double check it"
         else:
             return "We did not understand your entry."
    else:
        return "The word does not exist. Please double check it."


# get user input
word = input("Enter word you would like defined:   ")

definition = definitionRetrieval(word)

# prints out multiple definitions on one line if object type is correct by iteration
if type(definition) == list:
        for item in definition:
            print(item)

else:
    print(definition)
