import random

def rock_paper_scissors(player_hand: int, cpu_hand: int, win_count: int = 0):
    if player_hand == cpu_hand:
        return "Tie!"
    elif player_hand == 1:
            if cpu_hand == 2:
                return "You lose!"
            elif cpu_hand == 3:
                return "You win!"
    elif player_hand == 2:
            if cpu_hand == 1:
                return "You win!"
            elif cpu_hand == 3:
                return "You lose!"
    elif player_hand == 3:
            if cpu_hand == 1:
                return "You lose!"
            elif cpu_hand == 2:
                print("You win!")
                return "You win!"
    else:
        return "Invalid input!"



def main():
    game_count = 0
    win_count = 0
    game_history = [
        [["You"], ["CPU"], ["result"]]
    ]
    

    while True:

        cpu_hand = random.randint(1, 3)
        player_hand = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))
        result = rock_paper_scissors(player_hand, cpu_hand)
        game_history.append([[player_hand], [cpu_hand], [result]])

        if result == "You win!":
            win_count += 1

            if win_count == 3:
                print("\nYou won 3 times in a row!")
                break
            
        print("Game:", game_count, "You:", player_hand, "CPU:", cpu_hand, "Result:", result, "Win count:", win_count, "\n")
        
        game_count += 1

main()