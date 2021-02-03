# game.py

import random

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#
#asking for an input
#

options = ["rock", "paper", "scissors"]

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

#
#validate the user selection 
#
#stop the program  (not try to determine the winner)
#... if the user choice is invalid

user_choice.lower()

if user_choice in options:
    pass
else:
    print("OOPS, please choose a valid option and try again")
    exit()


print(f"You chose: {user_choice}") 

#
#simulating a computer input
#

computer_choice = random.choice(options)

print(f"The computer chose: {computer_choice}")

#
#determining who won
#

print("-------------------")

if user_choice == computer_choice:
    print("It's tie!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win! Congrats")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win! Congrats")
else:
    print("Oh! The computer won, that's ok!")

print("-------------------")
print("Thanks for playing. Please play again!")