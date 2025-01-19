from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list
import random

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ''
for i in range(len(chosen_word)):
    placeholder += '_'

print(f"Word to guess: {placeholder}")

game_over = False
lives = 6
guessed_letters = []

while not game_over:
    display = ''
    guess = input('Guess a letter: ')
    for letter in chosen_word:
        if guess == letter:
            display += guess
            guessed_letters.append(guess)
        elif letter in guessed_letters:
            display += letter
        else:
            display += '_'

    if display == chosen_word:
        print(f"You have guessed {chosen_word}, You win!")
        game_over = True
    else:
        print(f"Word to guess: {display}")

    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life.")
        lives -= 1

    if lives == 0:
        print(f"You lose. the word was {chosen_word}.")
        game_over = True

    if '_' not in display:
        game_over = True

    print(stages[lives])
    print(f"***********************{lives}/6 LIVES LEFT*************************")


