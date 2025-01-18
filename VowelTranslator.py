#Find all the vowels in the word/Sentence and convert them into numbers

vowelList = ['a', 'e', 'i', 'o', 'u']
for vowel in vowelList:
    print(vowel)

userInput = list(input("Enter any word: "))
finalWord = ""

for word in userInput:
    for vowel in vowelList:
        if(word == vowel):
            finalWord += "2"
            break   
    if(word != vowel):
        finalWord += word

print(finalWord)
