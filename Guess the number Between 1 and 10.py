import random

x = random.randrange(1,10)

guess = int(input("Guess a number between 1 and 10: "))

while guess != x:
    print("Sorry, you guessed incorrectly. Try again. \n")
    guess = int(input("Guess a number between 1 and 10: "))

print("Congratulations! You guessed the number correctly!")
    
