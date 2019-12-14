#Guess the number game.

#import module.
import random

#Ask for player name and start the game.
print('Lets get acquainted. What is your name?')
name = input()

print('It is nice to meet you ' + name + ', I have choosen a number between 1 and 20.')

#Assigning a value for the secret number, using the random module.
secretNumber = random.randint(1, 20)

#Logic for the game using for loop. 6 is the maximum amount of guesses
for guessesTaken in range(1, 7):
    print('Which number do you think it is?')
    guess = int(input())
    if guess < secretNumber:
        print('Sorry, but the number I am thinking of is LARGER.')
    elif guess > secretNumber:
        print('Sorry, but the number I am thinking of is SMALLER.')
    else:
        break #Happens on correct guess

    #Win/Loss notification.
if guess == secretNumber:
    print('Magnificent, ' + name + '! You\'re Third-Eye is wide open, and you have revealed the true hidden number. It had only take you ' + str(guessesTaken) + ' attempts.')
else:
    print('You have taken too many guesses and have shamed your family in doing so. The number was, ' + str(secretNumber) + '.')
    
