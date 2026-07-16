import random
secret_word = random.choice(["ready", "words", "house", "train"])
attempt = 0
print("- - - - -\n" * 6, end="")
while attempt < 6:
    # Keeps asking until a valid word is entered
    while True:
        guess = input("Enter a 5 letter word: ").lower()
        if len(guess) == 5:
            break
        print("Please enter exactly a 5 letter word.")
    attempt += 1
    correct = ["_"] * 5
    # Green letter logic
    for index, char in enumerate(secret_word):
        if guess[index] == char:
            correct[index] = guess[index]
    formatted = "  ".join(correct)
    print(formatted.upper())
    # Extra information about each letter
    for index, letter in enumerate(guess):
        if letter == secret_word[index]:
            print(f"{letter.upper()} -> Correct position.")
        elif letter in secret_word:
            print(f"{letter.upper()} -> Exists elsewhere.")
        else:
            print(f"{letter.upper()} -> Doesn't exist.")
    # Win condition
    if guess == secret_word:
        print(f"\nCongratulations! The word was '{secret_word.upper()}'.")
        break
# Lose condition
else:
    print(f"\nYou lost! The word was '{secret_word.upper()}'.")
