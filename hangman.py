import random
import string
from words import words

def generateWord(words):
    word = random.choice(words)
    if '-' in word:
        word = random.choice(words)
    return word.upper()
    
def hangman():
    word = generateWord(words)
    correctLetters = set(word) 
    letters = set(string.ascii_uppercase)
    selectedLetters = set()
    playerLetter = input('Choose a letter => ').upper()
    
hangman()