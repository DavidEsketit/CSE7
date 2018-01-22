import random
"""

Outline of Hangman
1. Make a word bank - 10 items on list
2. Select a random item from the list
3. Hide the word(use*)
4. Reveal letters if they have been guessed
5. Create the win condition

"""
print("You are playing a game of hangman.")
print("You must guess a word relating to Marvel or DC comics.")
print("If you guess the letter incorectly 10 times you will lose.")
word_bank = ["Batman", "Wonderwoman", "Joker", "Deadshot", "The Flash", "Reverse Flash", "Firestorm", "Thor", "Ironman",
             "Captain America"]
word = random.choice(word_bank)
guesses_left = 1
letters_guessed = ""
print(word)
while guesses_left > 0:
    num_of_word = len(word)
    print("The length of the word is %s" % num_of_word)
    response = (input("Guess now. "))
    print(response + letters_guessed)
    if response == word:
        guesses_left -= 1
        print("So far you got %s" % response)
    elif response != word:
        guesses_left -= 1
        print("That's not a letter.")
