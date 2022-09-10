from cmath import log
import random
from hang_man_art import logo, stages
from hang_man_word import word_list

chosen_word = random.choice(word_list)
print(f"chosen word is {chosen_word}")
print(logo)
word_length = len(chosen_word)
lives = 6
display = []
for _ in range(word_length):
    display += "_"


end_of_the_game = False
while not end_of_the_game:
    user_guess = input("Enter a letter: ").lower()
    if user_guess in display:
        print(f"You already chose this {user_guess} chose other")
        print(display)
    for value in range(word_length):
        letter = chosen_word[value]
        if letter == user_guess:
            display[value] = letter
    if user_guess not in chosen_word:
        print(f"You letter is {user_guess} and it is not in the chosen word")
        lives -= 1
        if lives == 0:
            print("You lose")
            end_of_the_game = True
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_the_game = True
        print("You win")
    print(stages[lives])