

print('''
      
          /\ o 
   o     /_ /~~/
    \      /\/
     \    /   
      \  /   
,-----------------,
| ,-----------,   |
| |   Guess   | O |
| |    the    | O |
| |   number  |...|
| |___________|I#I|
|_____________dcau|
    
      
      ''')

import random

print("Welcome to the number guessing game!")

levels = ["easy", "medium", "hard"]

def game_level(level):
    
    if level == "easy":
        no_of_guesses = 10
        print(f"You get {no_of_guesses} number of guesses.")
    
    elif level == "medium":
        no_of_guesses = 6
        print(f"You get {no_of_guesses} number of guesses.")
    
    elif level == "hard":
        no_of_guesses = 4
        print(f"You get {no_of_guesses} number of guesses.")
    
    return no_of_guesses


while True:
    
    level = input("Pick a level (easy, medium, hard): ").lower()
   
    if level in levels:
        no_of_guesses = game_level(level)
        
        break
    
    else:
        print("Invalid input. Please recheck again.")


def random_number():
    return random.randint(1, 100)
    
number = random_number() 

guesses = 0

while guesses < no_of_guesses:
    
    player_guess = int(input("Guess the number from 1 to 100 ---> "))
    
    guesses += 1


    if player_guess < number:
        print("Too low, guess again!")
    
    elif player_guess > number:
        print("Too high, guess again!")
    
    else:
        print(f"Congrats! You win. The number was {number}. It took you {guesses} guesses.")
        break

if guesses == no_of_guesses and player_guess != number:
    print(f"Sorry, you've used all your {no_of_guesses} guesses. The number was {number}.")


 


