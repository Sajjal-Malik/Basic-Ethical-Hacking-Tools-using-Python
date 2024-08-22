# Code in this file is Just for Practice of Python Basics 

import random

print("******* Welcome to Hangman Task! ********")


words = ["hacker","bounty","random"]


display_word = []


secret_word = random.choice(words)
# print(secret_word)

print("You get total of 5 gusses!")
for letter in secret_word:
    display_word += "-"
print(display_word)

num = 0
game_over = False
while not game_over:
    guess = input("Guess the letter:").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
        num += 1
        guesses_left = 5 - num
        print(f"You have {guesses_left} guesses left until this challenge finishes!")
        if num >= 5:
            print("Game Over, You have reaached Guess limit!")
            game_over = True

    if "-" not in display_word:
        print("You won, Game is over")
        game_over = True