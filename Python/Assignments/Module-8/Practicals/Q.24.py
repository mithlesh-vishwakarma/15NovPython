# Q.24 Write a Python program to match a word in a string using re.match().

import re

text = "Python is an amazing programming language."
word_to_match = "Python"

match = re.match(word_to_match, text)

if match:
    print(f"Matched '{word_to_match}' at the beginning of the string.")
else:
    print(f"Did not match '{word_to_match}' at the beginning.")
