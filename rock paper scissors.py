import random

beats = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}
options = ["rock", "scissors", "paper"]

while True:
    your_choice = input("Choose rock, scissors, or paper: ").lower().strip()
    
    if your_choice not in beats:
        print("Invalid choice! Please try again.")
        continue

    random_choice = random.choice(options)
    print(f"Computer chose: {random_choice}")

    if beats[your_choice] == random_choice:
        print("You won!")
        break
    elif your_choice == random_choice:
        print("It's a tie, try again.\n")
    else:
        print("You lost..")
        break