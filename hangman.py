# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 12:04:06 2023

@author: Gihan Kurukulasooriya
"""
def hangman():
    letter_chosen = []
    guessed_words = []
    guess_condition = False
    print("WELCOME TO HANGMAN!")
    word_chosen = input("Please choose a word for your friend to guess: ").lower() #choosing a word for the player to guess
    word_chosen_arr = list(word_chosen) #putting the word chosen into a list for easy access
    tries = 10 #number of tries we are giving them to allow them to keep trying
    underscores = "_"*len(word_chosen)
    while not guess_condition and tries>0:
        guess = input("Please choose a word, or letter for you to guess: ")
        print("Here is the length of the word: ", underscores)
        
        if len(guess)==1 and guess.isalpha(): #Checking if the person inputted a single letter instead of a whole word and if it is an alphabetical letter
            if guess in word_chosen_arr:
                print("We already guessed this letter: ", guess)
                
                
            elif guess not in word_chosen_arr:
                print("The letter you have chosen isn't in this word")
                tries -= 1
                print("The total tries you have left: ", tries)
                
                
            else:
                print("Correct choice, that is the right word")
                word_list = list(underscores)
                index = [i for i, letter in enumerate(word_chosen) if letter == guess]
                for ind in index:
                    word_list[ind] = guess
                underscores = "".join(word_list)
                if("_" not in underscores):
                    guess_condition = True


        elif len(guess) == len(word_chosen) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed this word")
            elif guess != word_chosen:
                print(guess, "is not the word.")
                tries -= 1
                print("The total tries you have left: ", tries)
                guessed_words.append(guess)
            else:
                guess_condition = True
                underscores = word_chosen
        else:
            print("Input is invalid please try again")
        if guess_condition:
            print("Congrats you got the word and saved the man")
        else:
            print("Sorry for not completing the game, here is the word you were searching for: ", word_chosen)
def main():
    hangman()
    while input("Try again? (Y/N) ").upper() == "Y":
        hangman()
if __name__ == "__main__":
    main()
            
    
    
