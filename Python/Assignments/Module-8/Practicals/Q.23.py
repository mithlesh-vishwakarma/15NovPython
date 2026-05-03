# Q.23 Write a Python program to search for a word in a string using re.search(). 

import re

text = "Python is an amazing programming language."
word_to_search = "amazing"

match = re.search(word_to_search, text)

if match:
    print(f"Word '{word_to_search}' found at index {match.start()} to {match.end()}.")
else:
    print(f"Word '{word_to_search}' not found.")
