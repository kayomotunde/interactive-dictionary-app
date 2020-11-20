import json
from difflib import get_close_matches

# Load json data into python dictionary data
data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        word_other = get_close_matches(word, data.keys())[0]
        yn = input(f"Did you mean {word_other} instead? Enter Y if yes, or N if No: ").capitalize()
        if yn == "Y":
            return data[word_other]
    else:
        return "The word doesn't exist. Please check it."

word = input("Enter word: ")

print(translate(word))