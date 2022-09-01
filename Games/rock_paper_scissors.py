# Create a rock, paper, scissors game

import random
# Ask user if they want to play
loop_start_game = input("Would you to like to play rock, paper, scissors? Enter yes/no: ")

# creates a loop to keep playing the game
while loop_start_game == 'yes' :

# Allows user and computer to make a choice
    choice = input('Choose: rock, paper, or scissors (press q to quit): ')
    sample_set = {'rock', 'paper', 'scissors'}
    item = random.choice(tuple(sample_set))
    if choice == "q":
        print("Okay see you next time!")
        break

    # ** Bug that I don't know how to fix yet
    # if choice != 'rock' or 'paper' or 'scissors':
    #     print('That is not an item!')
    #     break
    print("I choose:", item)

# The conditions of winning, losing, or drawing
    if choice == item:
        print('Its a draw!')
    elif choice == 'rock' and item == 'scissors':
        print('You win!')
    elif choice == 'rock' and item == 'paper':
        print('You lose!')
    elif choice == 'scissors' and item == 'paper':
        print('You win!')
    elif choice == 'scissors' and item == 'rock':
        print('You lose!')
    elif choice == 'paper' and item == 'rock':
        print('You win!')
    elif choice == 'paper' and item == 'scissors':
        print('You lose!')

# Allows user to exit the game
    elif choice == "q":
        print("Okay see you next time!")
        break
else:
    print("Okay see you next time!")
