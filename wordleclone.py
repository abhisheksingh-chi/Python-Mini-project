import random
words =random.choice(["words","ready"])
atem = 0
correct = ['_', '_', '_', '_', '_']

print("- - - - -\n"*6,end="")
while atem < 6:
    atem += 1
    guess = input("Enter 5 letter word: ")
    if len(guess)<5:
        print("Please enter a 5 letter word")
#Exception handling for IndexError when len(guess)<len(words)      
    for index, char in enumerate(words):
        if guess[index] == words[index]:
            correct[index] = guess[index]
        else:
            correct[index]= "-"
    print(correct)
    if guess == words:
        break
                
   