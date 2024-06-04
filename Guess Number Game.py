import random

target =  random.randint(1,100)
while True:
    userChoice = input("Guess the number? Or Quit(Q): ")
    if(userChoice == "Q"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Correct Guess, You Won!!!")
        break
    elif(userChoice < target):
        print("Guess a higher number!")
    else:
        print("Guess a smaller number!")


print("------Game Over------")