##################### SCOPE ################################

# examples of local and global variables
# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function : {enemies}")
#
# increase_enemies()
# print(f"enemies outside function : {enemies}")

#Local Scope
#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)

# #Global Scope
# player_health = 10
#
# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
# drink_potion()

#Variable dentro da funcao nao usa fora
# game_level = 3
# def create_enemy()
#     enemies = ["Skeleton","Zombie","Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
# print(new_enemey)

import random

#SETUP
difficulty = { "easy": 10, "hard": 5}
number_to_guess = 0
guesses = 0

def startGame():
    global number_to_guess
    number_to_guess = random.randint(1, 100)
    return number_to_guess

print("Guess a number from 0 to 100!")
choose_difficulty = input(f"Choose your difficult type 'hard' or 'easy': ").lower()

is_game_over = False
startGame()

guesses = difficulty[choose_difficulty]

print(f"You have chose {choose_difficulty} mode, you have {guesses} to guess")

while not is_game_over:

    if guesses > 0:
        number_guessed = int(input("Guess a number: "))

    if number_guessed > number_to_guess and guesses > 0:
        print("Too HIGH!")
        guesses -= 1

    elif number_guessed < number_to_guess and guesses > 0:
        print("Too LOW! Try Again")
        guesses -= 1

    elif number_guessed == number_to_guess:
        print("YOU GOT IT! YOU WON!")
        is_game_over = True
    elif guesses == 0:
        print("You have no more Guesses! YOU LOSE!")
        is_game_over = True