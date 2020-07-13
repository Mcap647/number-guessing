import random
print("Number guessing game")
number = random.randint(1, 9)
chances = 0
print("Guess a number (between 1 and 9:")

while chances < 5:
    guess = int(input())
    # Compare the user entered number
    # with the number to the gussed
    if guess == number:
        print("Congratulations you Won")
        break
    elif guess < number:
        print("Your guess was too low: Guess a higer number")

    else:
        print("Your guess was too high: Guess low")
    chances += 1
if not chances < 5:
    print("You lose!!! The number is", number)
