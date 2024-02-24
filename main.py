import random

error_inv = "Invalid"


# Roll the "dice" function
def roll():
    min_value = 1
    max_value = 100
    roll = random.randint(min_value, max_value)

    return roll


# Get the number of players
while True:
    players = input("Enter the number of players (2-6) >>> ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 6:
            break
        else:
            print("There have to be between 2-6 players.")
    else:
        print("[Error -- " + error_inv + "]: Please try again.")

max_score = 500

# Initializing the score of all players with 0
player_scores = [0 for i in range(players)]

# Game functionality
while max(player_scores) < max_score:

    # Showing the player his score before his turn
    for player_i in range(players):
        print("\nPlayer " + str(player_i + 1) + " turn has just started!\n")
        print("Your current total score is: " + str(player_scores[player_i]) + "\n")
        current_score = 0

        # Evaluate the value if chosen to take the chance
        while True:
            want_to_roll = input("Would you like to roll (y/n) >>> ")
            if want_to_roll.lower() != "y":
                break
            else:
                rolled_value = roll()

            if rolled_value <= (100 / 3):
                print(
                    f"Uhhh... I'm Sorry. {rolled_value} is in the lower third. Your turn is therefore over.\nAnd you gain 0 points.")
                current_score = 0
                break
            else:
                current_score += rolled_value
                print("Your rolled a " + str(rolled_value) + " . Your score has been updated.")

            print("Your score is: " + str(current_score))

        player_scores[player_i] += current_score
        print("The total score of Player " + str(player_i + 1) + " is: " + str(player_scores[player_i]))

# Identifying the winner
max_score = max(player_scores)
winner = player_scores.index(max_score)
print("Player " + str(winner + 1) + " is the winner of this game with a score of " + str(max_score))