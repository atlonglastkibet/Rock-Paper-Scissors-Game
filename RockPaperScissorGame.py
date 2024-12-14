import random
from enum import IntEnum

# IntEnum
class Action(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3

# Get player action
def get_player_action():
    while True:
        try:
            player_action = input('\nPick a number (Rock[1], Paper[2] or Scissors[3]): ')
            selection = int(player_action)
            action = Action(selection)
            return action
        except (ValueError, KeyError):
            print('Invalid choice. Please choose 1, 2, or 3.')

# Get computer action
def get_computer_action():
    computer_choice = random.randint(1, len(Action))
    action = Action(computer_choice)
    return action

# Winner selection
def winner_selection(player_action, computer_action):
    if player_action == computer_action:
        print(f'Both of you have chosen {player_action.name}. It is a Draw!')
        return 'draw'
    
    if (player_action == Action.Rock and computer_action == Action.Scissors) or \
       (player_action == Action.Paper and computer_action == Action.Rock) or \
       (player_action == Action.Scissors and computer_action == Action.Paper):
        print(f'\n{player_action.name} beats {computer_action.name}. You won!')
        return 'user'
    
    print(f'\n{computer_action.name} beats {player_action.name}. Computer won!')
    return 'computer'

def play_game():
    user_points = 0
    computer_points = 0
    
    while user_points < 2 and computer_points < 2:
        user_action = get_player_action()
        computer_action = get_computer_action()
        
        print(f'You chose: {user_action.name}, Computer chose: {computer_action.name}')
        
        winner = winner_selection(user_action, computer_action)
        
        if winner == 'user':
            user_points += 1
            print('You won this round!')
        elif winner == 'computer':
            computer_points += 1
            print('Computer wins this round!')
        else:
            print("It's a draw!")
        
        print(f'\nScore: You {user_points} - {computer_points} Computer')
    
    if user_points > computer_points:
        print('\nKudos champ! You won the league!')
        
    else:
        print('\nThe computer won! Better luck next time!')

if __name__ == "__main__":
    print("\nWelcome to Rock-Paper-Scissors!")
    print('\n--------------------------------')
    play_game()