actualWord = "lion"
isGuess = True
guessMax = 5

print("You only have 5 Guess, Guess correctly")

while isGuess and guessMax > 0:
    guessWord = input("Enter your Guess: ").lower()
    if(actualWord == guessWord):
        print("You guessed it correctly")
        print("You WIN")
        isGuess = False
    else: 
        guessMax -= 1
        if(guessMax == 0):
            print("Your guess didn't match")
            print("You LOST")   
        else:
            print("Your guess didn't match, Please Try Again...")
            print("You only have",guessMax,"Guesses now")    

print("...GAME OVER...")