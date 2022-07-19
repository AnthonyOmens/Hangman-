import random
from hangman_words import word_list
from hangman_art import stages, logo
# these imports prevent having a SUPER long file

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)


print(f'The word is {chosen_word}.')
#keeping this, tells you what the word is

display = []
# display becomes the list of underscores
# letters will populate on this list when letters are guesses
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
# .lower() incase user types in an upper case


    if guess in display:
      print("you already guessed that 0_0")
    # if user gusses the same letter again
  
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong
    if guess not in chosen_word:
        print(f"Fun Fact, the letter {guess} is NOT in the word")
        print("You lose a life")
        # we could use /n on these print statements but I prefer not to have a super long line of code (like this comment)
        if lives > 1:
          print(f"You now have {lives} lives left....")
        else:
          print(f"You now have {lives} life left....")
        #grammar is important
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose. (lol)")
          
    #join all the elements
    print(f"{' '.join(display)}")

    #check if the user has guessed all the letters
    if "_" not in display:
        end_of_game = True
        print("You win. yayyy")


    print(stages[lives])