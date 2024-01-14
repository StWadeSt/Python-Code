#Hangman Game

import random

file = open("words.txt", "r")
values = file.read()
list_of_words=values.split("\n")

lives = 6

#list_of_words=['generic', 'gigabit', 'morning', 'beekeeper','housing']
word = random.choice(list_of_words)
display = ["_"] * len(word)
used_letters=[]

end_of_game = False

while not end_of_game:
    print(display)
    letter=input("Guess a letter: ")
    
    if letter in used_letters:
        print("You have already guessed this letter.\nPLEASE TRY AGAIN\n")
    else:
        if letter not in word:
            lives -= 1
            print("BAD GUESS!\tYou got", lives, "attempts left")
        else:
            for position in range(0,len(word)):
                character = word[position]
                if character == letter:
                    display[position] = character
                    
        used_letters.append(letter)

        if "_" not in display:
            end_of_game = True
            print("You Win!\nThe word is ", display)
        elif lives == 0:
            end_of_game = True
            print("Game Over!")
 