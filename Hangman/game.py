from calendar import c
from arts import *
from words import *
import random
import os

print("Welcome to hangman Game!")
print("Happy Coding!")
print(stages[0])


def word_choice():
    """To return a random word for the user to solve."""
    return random.choice(word_list)

def vaildation_check(user_input, word_chosen):
    """Compare if two strings are the same and return a boolen and the string of the letters which are the same."""
    vaild_letters = []
    is_it_the_same = False
    for i in range(len(word_chosen)):
        if user_input[i] == word_chosen[i]:
            vaild_letters.append(word_chosen[i])
        else:
            vaild_letters.append("_")
    vaild_letters_str = "".join(vaild_letters)
    if user_input == word_chosen:
        is_it_the_same = True
    return vaild_letters_str, is_it_the_same

def word_status(the_chosen_word):
    list_words = []
    for _ in range(len(the_chosen_word)):
        list_words.append("_")
    new_word = "".join(list_words)
    return new_word
    

def play_game():
    the_word = word_choice().lower()
    your_words = []
    your_words.append(word_status(the_word))
    word_index = -1
    index = len(stages)-1
    while True:
        print(the_word)
        print(stages[index])
        print(your_words[word_index])
        if index == 0:
            print("Sorry, you lose......")
            print(f"The word was '{the_word}'.")
            break
        while True:
            user_input = input(f"Please enter anyword of your choice that should be {len(the_word)} letters long.\n").lower()
            if len(user_input) == len(the_word):
                break
            print(f"Your word length must be '{len(the_word)}' letters long.")
        vaild_let, boolen = vaildation_check(user_input, the_word)
        your_words.append(vaild_let)
        if boolen:
            print("You won!!!")
            print(f"The word was '{the_word}'.")
            break
        index -= 1

def clear_screen():
    """To clear screen of os terminal"""
    # For windows
    if os.name == "nt":
        _ = os.system("cls")
    # for mac and linux
    else:
        _ = os.system("clear")

while True:
    play_game()
    while True:
        commands = ["y", "n"]
        try:
            print("-----------------------------------------------------------------------")
            user_play_again = input("Thanks for playing!!!\nType 'y' to play again, 'n' to exit: ").lower()
            if user_play_again in commands:
                break
            else:
                print("You can only type (y/n), please try again. \n")
        except ValueError:
            print("You can only type (y/n), please try again. \n")
    if user_play_again == "n":
        print("-----------------------------------------------------------------------")
        print("Thank You For Playing, Bye........")
        break
    else:
        clear_screen()
        continue
clear_screen()
