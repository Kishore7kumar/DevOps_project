from loguru import logger
import random

# Configure Loguru
logger.add("game_log.log", rotation="1 MB", level="INFO", format="{time} - {level} - {message}")

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    options = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    ties = 0

    while True:
        # Player's move
        player_move = input("Enter your move (rock, paper, scissors or 'quit' to exit): ").lower()
        if player_move == "quit":
            print("Thanks for playing! Goodbye!")
            logger.info("Game ended by the player.")
            break
        if player_move not in options:
            print("Invalid move. Please try again.")
            logger.warning(f"Invalid move entered: {player_move}")
            continue

        # Computer's move
        computer_move = random.choice(options)
        print(f"Computer chose: {computer_move}")

        # Determine the winner
        if player_move == computer_move:
            result = "It's a tie!"
            ties += 1
        elif (player_move == "rock" and computer_move == "scissors") or \
             (player_move == "scissors" and computer_move == "paper") or \
             (player_move == "paper" and computer_move == "rock"):
            result = "You win!"
            player_score += 1
        else:
            result = "You lose!"
            computer_score += 1

        # Log the round
        logger.info(f"Player: {player_move}, Computer: {computer_move}, Result: {result}")
        print(result)
        print(f"Score - You: {player_score}, Computer: {computer_score}, Ties: {ties}")

if __name__ == "__main__":
    play_game()