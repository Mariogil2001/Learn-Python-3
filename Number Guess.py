"""
Author: Mario Gil Domingo
The program should do the following:
    1. Roll a pair of dice.
    2. Add the values of the roll.
    3. Ask the user to guess a number.
    4. Compare the user's guess to the total value.
    5. Determine the winner (user or computer).
    
"""
from random import randint #Make sure rolls are random
from time import sleep #Simulate dice rolls

#Function to obtain the user guess
def get_user_guess():
    guess = int(input("Guess the number: "))
    return guess

#Function to simulate the rolling of a pair of dice
def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print ("The maximum possible value is: %d" % max_val)
    guess = get_user_guess()
    if (guess > max_val):
        print ("No guessing higher than the maximum possible value!")
    else:
        print ("Rolling...")
        sleep(2) #To simulate the dice rolling sleep 2 seconds
        print ("The 1st roll is : %d" % first_roll)
        sleep(1)
        print ("The 2n roll is : %d" % second_roll)
        sleep(1)
        total_roll = first_roll + second_roll
        print ("The total roll : %d " % total_roll)
        print ("Result... ")
        sleep(1)
        if (guess == total_roll):
            print("You won!!")
        else:
            print ("You lose Bozoo xD")
        sleep(3)
    return False
roll_dice(2)      
    