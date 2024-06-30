import random

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Choose Rock, Paper or Scissors: ").lower()

    if user_input == "q":
        quit()
    
    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please try again.")
        continue
    
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_input}, computer chose {computer_action}.\n")

    if user_input == computer_action:
        print(f"Both players selected {user_input}. It's a tie!")
    elif user_input == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            user_wins += 1
        else:
            print("Paper covers rock! You lose.")
            computer_wins += 1
    elif user_input == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_wins += 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_wins += 1
    elif user_input == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_wins += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_wins += 1

    print(f"\nYou have won {user_wins} times.")
    print(f"The computer has won {computer_wins} times.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")