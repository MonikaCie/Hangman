import random
from words import words

def generateWord(words):
    word = random.choice(words)
    if '-' in word:
        word = random.choice(words)
    return word
    
generateWord(words)