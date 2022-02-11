
from ctypes import sizeof
import os
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

images = [
 """
 
 
 
 
 
 
 
 
 """, """
    
           
           
           
            
          
     
  _______
 """, """
    
     |      
     |      
     |      
     |       
     |      
     |
  ___|___
 """, """
     _________
     |      
     |      
     |      
     |       
     |      
     |
  ___|___
""", """
     _________
     | /     
     |/      
     |      
     |       
     |      
     |
  ___|___
""", """
     _________
     | /     |
     |/      
     |      
     |       
     |      
     |
  ___|___
""", """
     _________
     | /     |
     |/     (_)
     |      
     |       
     |      
     |
  ___|___
""", """
     _________
     | /     |
     |/     (_)
     |       |
     |       |
     |      
     |
  ___|___
""", """
     _________
     | /     |
     |/     (_)
     |      \|/
     |       |
     |      
     |
  ___|___
""", """
     _________
     | /     |
     |/     (_)
     |      \|/
     |       |
     |      / \\
     |
  ___|___
"""]

class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed = ""
        for letter in word:
            self.guessed += "_"
        self.roundsFailed = 0
        self.usedLetters = ""

    def addLetter(self, letter):
        index = 0
        hit = 0
        for x in self.word:
            if x == letter:
                self.guessed = self.guessed[:index] + letter + self.guessed[index+1:]
                hit = 1
            index+=1
        return hit

    def printGame(self):
        print(images[h1.roundsFailed])
        print("Uhodnuto: " + h1.guessed)

    def won(self):
        print("Cg you won")

    def lost(self):
        print("You lost xd")

word = input("Zadejte slovo: ")
h1 = Hangman(word)
err = ""

while h1.roundsFailed < len(images)-1:
    clear()
    h1.printGame()
    print(err)
    letter = input("Zadejte pismeno: ")
    err = ""
    if len(letter)==1:
        if h1.usedLetters.find(letter)==-1:
            h1.usedLetters+=letter
            if h1.addLetter(letter)==0:
                h1.roundsFailed+=1
            if h1.word == h1.guessed:
                clear()
                h1.printGame()
                h1.won()
                exit()
        else:
            err = "Pismeno jiz bylo zadano"
    else:
        err = "Zadejte jen jedno pismeno"
h1.printGame()
h1.lost()
input("Stisknete enter pro ukonceni")