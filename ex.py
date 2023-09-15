"""Pangrams are sentences (i.e. strings) that contain all the letters of the alphabet. 
Implement a method is_pangram that takes one argument as input and checks 
if the given string is a pangram and then returns the result as a boolean value.
"""


def is_pangram(text):
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    return all(letter in text for letter in alphabet)
    
    
text = input('Enter any text to determine if the input text is pangram: ')

print(is_pangram(text.lower()))



