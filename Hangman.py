import random
"""

Outline of Hangman
1. Make a word bank - 10 items on list
2. Select a random item from the list
3. Add user input to a list of letters_guessed
4. Build a list of letters to show, and display the string form
5. Create the win condition

"""
print("You are playing a game of hangman.")
print("You must guess a word relating to Marvel or DC comics.")
print("If you guess the letter incorrectly 10 times you will lose.")
word_bank = ["Batman", "Wonderwoman", "Joker", "Deadshot", "The Flash", "Reverse Flash", "Firestorm", "Thor", "Ironman",
             "Captain America"]
word = random.choice(word_bank)
guesses_left = 10
letters_guessed = []
print(word)

while guesses_left != 0:
    num_of_let = len(word)
    response = input("Guess now. ")
    print("The length of the word is %s" % num_of_let)
    letters_guessed.append(response)  # Make this lowercase
    output = []
    print("You've got %s guesses/guess left" % guesses_left)
    if response == word:  # If you guess the whole word
        print("So far you got %s" % response.join)
    else:
        print("That's not a letter.")
        guesses_left -= 1
    for letter in word:
        if letter in letters_guessed:  # only compare lowercase
            # Show the letter
            output.append(letter)
        else:
            # Hide the letter
            output.append("*")
    if guesses_left == 0:
        print("The word was %s" % word)
    str1 = "".join(output)
    print(str1)
    print("So far you've guessed %s" % letters_guessed)
