# Rock, Paper, Scissors game in simple Python Code 

import random


user_wins = 0
computer_wins = 0
draw = 0

options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Rock / Paper / Scissors or Q to quit : ").lower()
    if user_pick == "q":
        break
    if user_pick not in options:
        continue

    random_number = random.randint(0 , 2)
    
    computer_pick = options[random_number]
    print("Computer picked " + computer_pick + " .")

    if user_pick == 'rock' and computer_pick == 'scissors':
        print("You Win!!")
        user_wins += 1

    elif user_pick == 'paper' and computer_pick == 'rock':
        print("You Win!!")
        user_wins += 1

    elif user_pick == 'scissors' and computer_pick == 'paper':
        print("You Win!!")
        user_wins += 1

    elif user_pick == computer_pick:
        print("Draw!!")
        draw += 1

    else:
        print("Computer Win!!")
        computer_wins += 1


print("You win " + str(user_wins) + " times.")
print("Computer Win " + str(computer_wins) + " times.")
print("You both have " + str(draw) + " times.")

print("GOODBYE!!!")
