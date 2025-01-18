#Coverting Consonents to different letter

def translator(phrase):
    newPhrase = ""
    for letter in phrase:
        if letter.lower() not in "aeiou":
            if letter.isupper():
                newPhrase += 'J'
            else:    
                newPhrase += 'j'
        else:
            newPhrase += letter
    return newPhrase

userPhrase = input("Enter your Phrase: ")
print(translator(userPhrase))