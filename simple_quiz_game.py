
# This is simpe quiz game 

print("WELCOME TO MY QUIZ GAME:")

want_to_play = input("Do you want to play game:")
if want_to_play.upper() != "YES":
    quit()

print("Let's Play :) ")
score = 0

answer = input("What is the capital city of Nepal? ")
if answer.upper()=="KATHMANDU":
    print("CORRECT")
    score += 2
else:
    print("INCORRECT")

answer = input("What is the largest river in the world? ")
if answer.upper()=="NILE":
    print("CORRECT")
    score += 2
else:
    print("INCORRECT")

answer = input("Who is the prime minister of Nepal? ")
if answer.upper()=="SHER BAHADUR DEUBA":
    print("CORRECT")
    score += 2
else:
    print("INCORRECT")

answer = input("What is the full form of CPU? ")
if answer.upper()=="CENTRAL PROCESSING UNIT":
    print("CORRECT")
    score += 2
else:
    print("INCORRECT")

answer = input("Who wrote this code? ")
if answer.upper()=="RAMESHWOR NEPAL":
    print("CORRECT")
    score += 2
else:
    print("INCORRECT")

print("You have scored " + str(score) + " out of 10.")