import random

number = random.randint(1, 1000)
print("Guess the number")

while True:
    guesnum = int(input("Enter a number: "))
    if number > guesnum:
        print("The number is HIGHER, try again")
    elif number < guesnum:
        print("The number is LOWER, try again")
    else:
        print("YOU GUESSED IT!")
        break