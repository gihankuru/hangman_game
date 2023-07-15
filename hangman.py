# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 12:04:06 2023

@author: Gihan Kurukulasooriya
"""
def hangman():
    letter_chosen = []
    guess_condition = False
    word_chosen = input("Please choose a word for your friend to guess: ").lower() #choosing a word for the player to guess
    word_chosen_arr = list(word_chosen) #putting the word chosen into a list for easy access
    tries = 10 #number of tries we are giving them to allow them to keep trying
    while not guess_condition and tries>0:
        guess = input("Please choose a word, or letter for you to guess: ")
        if len(guess)==1 and guess.isalpha() #Checking if the person inputted a single letter instead of a whole word and if it is an alphabetical letter
            if guess in word_chosen_arr:
                print("We already guessed this letter:" guess)
            elif guess not in word_chosen_arr:
                print("The letter you have chosen isn't in this word")
                tries -= 1
            else:
                print("Correct choice, that is the right word")
        elif len(guess) == len(word_chosen) and guess.isalpha():
            
        
        else:
            print("Input is invalid please try again ")
        
    
    
