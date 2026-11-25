import random

items = ["rock", "paper", "scissors"]
user_choice = input("Enter your choice (rock, paper, scissors): ")
comp_choice = random.choice(items)

print(f"user choice: {user_choice} , computer choice: {comp_choice}")

if user_choice == comp_choice:
    print("This match is a tie!")
elif user_choice == "rock":
    if comp_choice == "scissors":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "paper":
    if comp_choice == "rock":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "scissors":
    if comp_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")