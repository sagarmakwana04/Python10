
import random

num=random.randint(1,20)

while True:
    guess=int(input("Guess a Number between 1 to 20: "))
    if guess==num:
        print("You Guessed a Correct Number")
        break
    elif guess>num:
        print("You Guessed a Greater Number")
    elif guess<num:
        print("You Guessed a Smaller Number")
        