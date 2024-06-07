import random

def main():
    while True:
        user_choice = input("Enter rock, paper, or scissors: ")
        user_choice = user_choice.lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        print(f"Your choice: {user_choice}")
        
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer's choice: {computer_choice}")
        
        determine_winner(user_choice, computer_choice)
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing!")
            break

def determine_winner(user, computer):
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    main()
