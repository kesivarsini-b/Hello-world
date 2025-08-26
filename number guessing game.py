import random
number=random.randint(1,5)
print("Guess the number between 1 and 5")
guess=int(input("Your guess:"))
if guess==number:
    print(f"You guessed correct number")
else:
    print(f"You guessed wrong number.the correct number was {number}")