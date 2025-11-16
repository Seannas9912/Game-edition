# 🃏 Blackjack Starter Template
# =============================
# Rules:
# - The deck is unlimited in size.
# - There are no Jokers.
# - Jack, Queen, and King count as 10.
# - Ace can count as 11 or 1.
# - Cards are not removed from the deck when drawn.

import random
import os  #You will use os to clear the screen when necessary
from arts import logo 

# print(logo)
def clear_screen():
    """To clear screen of os terminal"""
    # For windows
    if os.name == "nt":
        _ = os.system("cls")
    # for mac and linux
    else:
        _ = os.system("clear")

def deal_card():
    """Return a random card from the deck."""
    # TODO: Create a list of card values and return one at random.
    list_of_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "Q", "K", "J", "A"]
    return random.choice(list_of_cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    # TODO: Handle blackjack (21 with 2 cards) and Ace adjustment (11 or 1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compare user and computer scores and return a message indicating the result."""
    # TODO: Implement the game result logic.
    if calculate_score(user_score) == calculate_score(computer_score):
        return f"It's a Tie with {sum(user_score)}"
    elif calculate_score(user_score) == 21:
        return f"You are the winner with {sum(user_score)} a BLACKJACK"
    elif calculate_score(computer_score) == 21:
        return f"Computer is the winner with {sum(computer_score)} a BLACKJACK"
    elif calculate_score(user_score) > 21:
        return f"Computer is the winner with {sum(computer_score)} closer and less then 21"
    elif calculate_score(computer_score) > 21:
        return f"You are the winner with {sum(user_score)} closer and less then 21"
    elif calculate_score(user_score) < calculate_score(computer_score):
        return f"Computer is the winner with {sum(computer_score)} closer to 21"
    else:
        return f"You are the winner with {sum(user_score)} closer to 21"

def play_game():
    print(logo + "\n" + "-----------------------------------------------------------------------")

    # TODO: Initialize empty lists for user_cards and computer_cards.
    user_cards = []
    computer_cards = []
    # TODO: Deal two cards to each player using deal_card().
    for _ in range(4):
        card = deal_card()
        if len(user_cards) != 2:
            if isinstance(card, str):
                match card:
                    case "K" | "J" | "Q":
                        user_cards.append(10)
                    case "A" if calculate_score(user_cards) <= 10:
                        user_cards.append(11)
                    case "A" if calculate_score(user_cards) > 10:
                        user_cards.append(1)
            else:
                user_cards.append(card)
        else:
            if isinstance(card, str):
                match card:
                    case "K" | "J" | "Q":
                        computer_cards.append(10)
                    case "A" if calculate_score(computer_cards) <= 10:
                        computer_cards.append(11)
                    case "A" if calculate_score(computer_cards) > 10:
                        computer_cards.append(1)
            else:
                computer_cards.append(card)
    
    # TODO: Display user's cards and the computer's first card.
    
    # TODO: Use a while loop to allow the user to draw more cards or stop.
    # TODO: Computer should draw cards until it reaches 17 or higher.
    turn_count = 0
    while True:
        print(f"Your cards: {user_cards}, current score {calculate_score(user_cards)}")
        print("-----------------------------------------------------------------------")
        print(f"Computer's first card: {computer_cards[0]}")
        print("-----------------------------------------------------------------------")
        card = deal_card()
        if calculate_score(user_cards) == 21:
            break
        elif calculate_score(computer_cards) == 21:
            break
        else:
            if turn_count == 0:
                while True:
                    commands = ["y", "n"]
                    try:
                        user_input = input("Type 'y' to get another card, 'n' to pass: ").lower()
                        if user_input in commands:
                            break
                        else:
                            print("You can only type (y/n), please try again. \n")
                    except ValueError:
                        print("You can only type (y/n), please try again. \n")
                if user_input == "y":
                    turn_count += 1
                    match card:
                        case "K" | "J" | "Q":
                            user_cards.append(10)
                            card = 10
                        case "A" if calculate_score(user_cards) <= 10:
                            user_cards.append(11)
                            card = 11
                        case "A" if calculate_score(user_cards) > 10:
                            user_cards.append(1)
                            card = 1
                        case _ as value:
                            user_cards.append(value)
                            card = value
                    print(f"You drew a {card}")
                    print("-----------------------------------------------------------------------")
                    if calculate_score(user_cards) > 21:
                        break
                else:
                    turn_count += 1
            else:
                if calculate_score(computer_cards) < 17:
                    turn_count -= 1
                    match card:
                        case "K" | "J" | "Q":
                            computer_cards.append(10)
                        case "A" if calculate_score(computer_cards) <= 10:
                            computer_cards.append(11)
                        case "A" if calculate_score(computer_cards) > 10:
                            computer_cards.append(1)
                        case _ as value:
                            computer_cards.append(value)
                    if calculate_score(computer_cards) > 21:
                        break
                else:
                    break
    # TODO: Call compare() to determine the outcome and print it.
    print(compare(user_cards, computer_cards))
# TODO: Create a loop to let the user replay the game if they choose.

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
