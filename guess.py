print("Welcome to number guessing game")
print("I am going to think of a number between 1 and 100")
import random
cguess = random.randint(1,100)
print(f"Compter guessed number:{cguess}")
level = input("Choose difficulty  level.Type 'easy' or 'hard").lower()
if level == "easy":
    attempts = 10
else:
    attempts = 5
 
while attempts > 0:
    uguess = int(input(f"You have {attempts} attempts remaining to guess  the number\n.Make a guess:"))
    
    if uguess > cguess:
        print("Too high")
        attempts -= 1 
        
            
    elif uguess < cguess:
        print("Too low")
        attempts -= 1        
            
    else:
            print("You have  guessed the right number")
            attempts = 0
            
if uguess != cguess and attempts == 0:
    print("\n===YOU have no more attempts remianing====\n====YOU LOST=====")
    