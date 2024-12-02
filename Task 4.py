#Task 4: Rock-Paper-Scissors Game
print("Task 4: Rock-Paper-Scissors Game")
import random   
user_score = 0
computer_score = 0
while True:
    print("Choose one: rock, paper, or scissors.")
    user_choice = input("Your choice: ")
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please choose rock, paper, or scissors.")
        continue
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("You chose: ",user_choice)
    print("computer chose: ",computer_choice)
    if user_choice == computer_choice:
        print("tie")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("You win")
        user_score += 1
    else:
        print("You lose")
        computer_score += 1
    print("Your Score: ",user_score,"| Computer Score: ",computer_score)
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again != "yes":
        print("Thanks for playing")
        break