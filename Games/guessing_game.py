# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

# importing the random library
import random

attempts = 0
games = 0

# Creating the random list generator
random_list = random.randint(1,9)

# Ask user to guess between 1 and 9
game_start = input("Would you like to play a game? Enter yes/no: ")

# Higher or lower
while game_start == 'yes' :
    guess = input("Pick a number between 1 and 9 (to exit: type exit): ")
    if guess == "exit":
        print('Goodbye!')
        break
    if int(guess) == random_list:
        attempts += 1
        print ("Thats the number I guessed, you win!")
        print("Here's how many guesses it took: ", {attempts})
        print("Thanks for playing!")
        break
        # if input("Play again? yes/no ") == "no":
        #     break
        # else:
        #     games += 1
        #     print('This is game:', {games})
    elif int(guess) < random_list:
        attempts += 1
        print("You guessed too low :(")
    elif int(guess) > random_list:
        attempts += 1
        print('You guessed too high :(')
else:
    print("Okay, see you next time!")
