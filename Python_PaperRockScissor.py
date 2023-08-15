import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    option = ["rock", "paper", "scissors"]
    computer_choice = random.choice(option)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"Your choice: {player}. Computer chose: {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! Player Wins"
        else:
            return "Paper covers rock! You lose!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! Player Wins"
        else:
            return "Scissors cuts paper! You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! Player Wins"
        else:
            return "Rock smashes scissors! You lose!"
    else:
        return "Invalid player choice."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)