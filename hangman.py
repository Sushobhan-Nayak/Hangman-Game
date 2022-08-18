import random
from art import stages, logo
from wordlist import word_list

print(logo)

lives = 6

chosen_word = random.choice(word_list)

lenght = len(chosen_word)

display = []
for l in chosen_word:
    display.append("_")

end_of_game = False

print(stages[lives])

while not end_of_game:

    print(display)

    guess = input("Guess a letter !\n").lower()

    for position in range(0, lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print(f"You lose.\nThe word is {chosen_word}")

    if "_" not in display:
        end_of_game = True
        print("\n------Congratulations------\n     You have won !!!!")
