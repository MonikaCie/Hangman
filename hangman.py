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
    correctLetters = set(word) #Letters present in the word
    letters = set(string.ascii_uppercase) #All letters
    selectedLetters = set() #Letters selected by a player
    playerLetter = input('Choose a letter => ').upper()
    
    if playerLetter in letters and playerLetter not in selectedLetters:
        selectedLetters.add(playerLetter)
        if playerLetter in correctLetters:
            correctLetters.remove(playerLetter)
    
hangman()