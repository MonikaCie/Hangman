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
    
    lives = 10
    
    while len(correctLetters) > 0 and lives > 0:
        
        #Used letters
        print('\nUsed letters: ' , ' '.join(selectedLetters))
        
        #Currently guessed letters in the word
        wordLetters = []
        for letter in word:
            if letter in selectedLetters:
                wordLetters.append(letter)
            else:
                wordLetters.append('*')
        print(' '.join(wordLetters))
                
    
        playerLetter = input(f'Lives left: {lives}\nChoose a letter => ').upper()
        
        if playerLetter in letters and playerLetter not in selectedLetters:
            selectedLetters.add(playerLetter)
            if playerLetter in correctLetters:
                correctLetters.remove(playerLetter)
            else:
                lives = lives - 1
                print(f'{playerLetter} not in the word.')
                
        elif playerLetter in selectedLetters:
            print(f'Letter {playerLetter} already used. Try a different letter.')
        else:
            print(f'Letter {playerLetter} is invalid. Try a different letter.')
    
    if lives == 0:
        print(f'GAME OVER!\nThe word was: {word}')
    else:
        print(f'Congratulations! You guessed {word} correctly')
    
hangman()