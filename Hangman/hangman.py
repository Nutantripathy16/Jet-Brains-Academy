# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 00:31:41 2021

@author: NutanTripathy
"""

#first stage of hangman
print("""
H A N G M A N
The game will be available soon.
""")

#second stage of hangman
print("""
H A N G M A N
The game will be available soon.
""")
word = input("Guess the word:")
if word == "python":
    print("You survived!")
else:
    print("You lost!")    

#third stage of hangman

import random
print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
word1 = input("Guess the word:")
#print("Guess the word: ")
word2 = random.choice(words)
#print(word)
if word1 == word2 :
    print("You survived!")
else:
    print("You lost!")    

#forth stage of hangman

import random
print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
#word1 = input("Guess the word:")
#print("Guess the word: ")
print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript'] 
word1 = random.choice(words)
a = word1[:3]
b = word1[3:]
word = a + "-" * len(b)
print("Guess the word:",word)
#print(word)
word2 = input() 
if word1 == word2 :
    print("You survived!")
else:
    print("You lost!")    

#fifth stage of hangman
import random
print("H A N G M A N\n")
words = ['python', 'java', 'kotlin', 'javascript']
word1 = random.choice(words)
unique_letters = set(word1)
print("-" * len(word1))
initial_word = list("-" * len(word1))
for i in range(8):
    letter = input("Input a letter:")
    print()
    if letter in word1:
        for m in range(0, len(word1)):
            if word1[m] == letter:
                initial_word[m] = letter
        final_word = "".join(initial_word)
        print(final_word)
    else:
        print("That letter doesn't appear in the word")
print("""Thanks for playing!
We'll see how well you did in the next stage""")

#sixth stage of hangman
import random
print("H A N G M A N\n")
words = ['python', 'java', 'kotlin', 'javascript'] 
word1 = random.choice(words)
#print("word1",word1)
unique_letters = set(word1)
#print("unique_letters",unique_letters)
initial_word = list("-" * len(word1))
final_word = "".join(initial_word)
print(final_word)
tries = 8
true_guesses = set()
false_guesses = set()
win = 0

while tries > 0:
    print()
    dash = 0
    for i in word1:
        if i in true_guesses:
            print(i,end = '')
        else:
            dash = dash + 1
            print("-",end='') 
    if dash == 0:
        print("\nYou guessed the word!")
        print("You survived!") 
        win = 1
        break          
    letter = input("\nInput a letter: ")
    if letter in unique_letters:
        if letter in true_guesses:
            print("No improvements")
            tries = tries - 1
        true_guesses.add(letter)
    else:
        false_guesses.add(letter)
        print("That letter doesn't appear in the word")
        tries = tries - 1
        
if win != 1:
    print("You lost!")

#seventh stage of hangman
import random
import string
alphabet_string = string.ascii_lowercase
alphabet_list_lower = list(alphabet_string) 

print("H A N G M A N\n")
words = ['python', 'java', 'kotlin', 'javascript'] 
word1 = random.choice(words)
#print("word1",word1)
unique_letters = set(word1)
#print("unique_letters",unique_letters)
initial_word = list("-" * len(word1))
final_word = "".join(initial_word)
print(final_word)
tries = 0
true_guess = set()
false_guess = set()
win = 0

while tries < 9:
    if tries == 8 and final_word != word1:
        print("You lost!")
        break
    
    if tries <= 8 and final_word == word1:
        print(f"You guessed the word {final_word}!")
        print("You survived!") 
        break 
    
    letter = input("Input a letter: ")
    
    if letter not in alphabet_list_lower and len(letter) == 1:
        print("Please enter a lowercase English letter\n")
        print()
        print(final_word)
    elif len(letter) != 1:
        print("You should input a single letter\n")
        print()
        print(final_word)
        
    elif letter in unique_letters and letter not in true_guess:
        true_guess.add(letter)
        for i in range(0,len(word1)):
            if word1[i] == letter:
                initial_word[i] = letter
        final_word = "".join(initial_word)
        print()
        print(final_word)
        
    elif letter not in unique_letters and letter not in false_guess:
        tries = tries + 1
        #print("tries",tries)
        false_guess.add(letter)
        if tries < 8:
            print("That letter doesn't appear in the word\n")
            print(final_word)
        elif tries == 8:
            print("That letter doesn't appear in the word")    
        
        
    elif letter in false_guess or letter in true_guess:
        if tries < 8:
            print("You've already guessed this letter\n")
            print(final_word)
        elif tries == 8:
            print("You've already guessed this letter")    

#eighth stage of hangman
import random
import string
alphabet_string = string.ascii_lowercase
alphabet_list_lower = list(alphabet_string) 

print("H A N G M A N\n")
while True:
    chance = input('Type "play" to play the game, "exit" to quit:')
    if chance == "play":
        words = ['python', 'java', 'kotlin', 'javascript'] 
        word1 = random.choice(words)
        #print("word1",word1)
        unique_letters = set(word1)
        #print("unique_letters",unique_letters)
        initial_word = list("-" * len(word1))
        final_word = "".join(initial_word)
        print(final_word)
        tries = 0
        true_guess = set()
        false_guess = set()
        win = 0

        while tries < 9:
            if tries == 8 and final_word != word1:
                print("You lost!")
                break
            
            if tries <= 8 and final_word == word1:
                print(f"You guessed the word {final_word}!")
                print("You survived!") 
                break 
            
            letter = input("Input a letter: ")
            
            if letter not in alphabet_list_lower and len(letter) == 1:
                print("Please enter a lowercase English letter\n")
                print()
                print(final_word)
            elif len(letter) != 1:
                print("You should input a single letter\n")
                print()
                print(final_word)
                
            elif letter in unique_letters and letter not in true_guess:
                true_guess.add(letter)
                for i in range(0,len(word1)):
                    if word1[i] == letter:
                        initial_word[i] = letter
                final_word = "".join(initial_word)
                print()
                print(final_word)
                
            elif letter not in unique_letters and letter not in false_guess:
                tries = tries + 1
                #print("tries",tries)
                false_guess.add(letter)
                if tries < 8:
                    print("That letter doesn't appear in the word\n")
                    print(final_word)
                elif tries == 8:
                    print("That letter doesn't appear in the word")    
                
                
            elif letter in false_guess or letter in true_guess:
                if tries < 8:
                    print("You've already guessed this letter\n")
                    print(final_word)
                elif tries == 8:
                    print("You've already guessed this letter")    
    elif chance == "exit":
        break
                   