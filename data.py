import random
print("Number Guessing Game")
print("Guess a Number between 1-9")
n = random.randint(1,9)
chances = 0
while chances < 5:
    guess= int(input("Enter Your Guess :"))
    if guess == n:
        print("Congtrats You Won")
        break
    elif guess < n:
        print("Your number is to low, guess a higher number")
    else:
        print("Your number is to hight, guess a lower number")
    chances += 1
if not chances < 5:
    print("You Lose!!! The number is", n)