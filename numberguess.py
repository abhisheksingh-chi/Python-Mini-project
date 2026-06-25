import random
lower_bount = int(input("Enter the lower bound: "))
higher_bound = int(input("Enter the higher bound: "))
num = random.randint(lower_bount,higher_bound)
count = 7
guess = 0
print(" You have 7 Tries ")
while guess < count:
    input_value = int(input("Enter your Guess: "))
    guess+=1
    if num == input_value:
        print(f"Congrats you guessed it right in {guess}")
        break
    
    elif guess >=count and input_value != num:
         print(f'Sorry! The number was {num}. Better luck next time.')
    
    elif num > input_value:
        print("You guessed too small! ")
       
    elif num < input_value:
        print("You guessed too high! ")
       
    
        
    