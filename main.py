import random
from art import logo

print(logo)

print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

NUMBER = random.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def attempts():
  if difficulty == "easy":
    attempts = 10
  elif difficulty == 'hard':
    attempts = 5
  else:
    print("Incorrect input! Exited")

  return attempts

print(f"You have {attempts()} attempts remaining to guess the number.")

guess = int(input("Make a guess: "))
attempts = attempts() 

while attempts > 0:
  
  if guess > NUMBER:
    print("Too High")
    attempts -= 1
    if attempts == 0:
      print("Sorry, you lost!")
      print(f"The Number was {NUMBER}")
    elif attempts > 1:  
      print(f"Remaining attempts: {attempts}")
      guess = int(input("Guess again! "))
      
  elif guess < NUMBER:
    print("Too low") 
    attempts -= 1
    if attempts == 0:
      print("Sorry, you lost!")
      print(f"The Number was {NUMBER}")
    elif attempts > 1:  
      print(f"Remaining attempts: {attempts}")
      guess = int(input("Guess again! "))
    
  elif guess == NUMBER:
    print("Congratulations, you won!")
    print("The answer was indeed f{NUMBER}")
    attempts = 0