from replit import clear
from art import logo
import random

############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

player_cards = []
player_score = 0
computer_cards = []
computer_score = 0
should_continue = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def add_card(list):
    """adds a card to a card deck"""
    list.append(random.choice(cards))

def check_ace(list):
    """turns an ace from an 11 to a 1"""
    list.remove(11)
    list.append(1)

def compare_score(computer, player):
    result = {
        "Lose": "You lose...",
        "Win": "You win!",
        "Tie": "You tied!"
    }
    
    if computer == 21:
        print(result["Lose"])
    elif player == 21:
        print(result["Win"])
    elif player > 21:
        print(result["Lose"])
    elif computer > 21:
        print(result["Win"]) 
    elif computer == 21:
        print(result["Lose"]) 
    elif player == computer:
        print(result["Tie"])
    elif player > computer:
        print(result["Win"])
    else:
        print(result["Lose"])

def blackjack():
    player_cards = []
    player_score = 0
    computer_cards = []
    computer_score = 0
    should_continue = True

    
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'. ")
    if play != "y":
        should_continue = False
        
    while should_continue:
        clear()
        print(logo)
    
        #generate the computer's first two cards
        add_card(computer_cards)
        add_card(computer_cards)
    
        computer_score = sum(computer_cards)
        add_card(player_cards)
        draw = True
        
        while player_score <= 21 and draw:
            add_card(player_cards)
            player_score = sum(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if player_score == 21 or computer_score == 21:
                break
    
            #if the score is over 21, checks if there is an available Ace card to convert to 1
            if player_score > 21:
                if 11 in player_cards:
                    check_ace(player_cards)   
                    player_score = sum(player_cards)
                else:
                        break
                    
            #asks user if they wish to draw another card
            answer = input("Type 'y' to get another card, 'n' to pass: ")
            if answer == "n":
                while computer_score < 17:
                    add_card(computer_cards)
                    computer_score = sum(computer_cards)
    
                    if computer_score > 21:
                        if 11 in computer_cards:
                            check_ace(computer_cards)
                            computer_score = sum(computer_cards)
                
                draw = False
    
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

        compare_score(computer = computer_score, player = player_score)
        
        blackjack()
        

blackjack()

