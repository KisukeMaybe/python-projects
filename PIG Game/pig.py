import random

def roll_dice():
    roll = random.randint(1, 6)
    return roll

while True:
    player_count = input("Enter number of players (2-4): ")
    if player_count.isdigit() and 2 <= int(player_count) <= 4:
        player_count = int(player_count)
        break
    else:
        print("Invalid input. Please enter a number between 2 and 4.")

max_score = 50
player_scores = [0] * player_count

while max(player_scores) < max_score:

    for player in range(player_count):
        current_score = 0
        print(f"\nPlayer {player + 1}'s turn. Current score: {player_scores[player]}")

        while True:
            want_roll = input("Roll the dice? (y/n): ").lower()
            if want_roll != 'y':
                break

            value = roll_dice()
            if value == 1:
                print("Rolled a 1! Turn over, no points scored.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"Rolled a {value}. Current turn score: {current_score}")
        
        player_scores[player] += current_score
        print(f"Player {player + 1}'s total score: {player_scores[player]}")

winner = player_scores.index(max(player_scores)) + 1
print(f"\nPlayer {winner} wins with a score of {player_scores[winner - 1]}!")