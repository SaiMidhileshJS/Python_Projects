
systemNumber = 47
loopCondition = True

while loopCondition:
    userInput = float(input("Guess the number between 0 to 100: "))
    if(systemNumber == userInput):
        print("You guessed the right Number")
        print("You win")
        break
    elif systemNumber < userInput:
        print("You guessed a bigger number. Guess a Smaller Number")
    elif systemNumber > userInput:
        print("You guessed a smaller number. Guess a Bigger Number")   
    else:
        print("You entered something wrong. Try Again...")     


print("---GAME OVER---")


