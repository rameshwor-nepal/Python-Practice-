# This is simple number guessing game 

import random



print("Let's start number guessing game: ")

input_number = input("Enter the number: ")

if input_number.isdigit():
    input_number = int(input_number)

    if input_number <= 0:
        print("Enter the number greater than 0 next time. ")
        quit()

else:
    print("Enter number next time. ")
    quit()


random_number = random.randint(0, input_number)
guess_count = 0

while True:
    guess_count += 1
    guess_number = input("Enter your guess number: ")
    

    if guess_number.isdigit():
        guess_number = int(guess_number)

    else:
        print("Enter proper number next time. ")
        continue

    if guess_number == random_number:
        print("You have guess correct number. ")
        break

    elif random_number < guess_number:
        print("You have guess above the number. ")
    
    else:
        print("You have guess below the number. ")

    
print("You have got correct number in " + str(guess_count) + " guesses. ")