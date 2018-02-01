# print("Hello World!")
#
# # David Solis
#
# print(3 + 5)
# print(5 - 3)
# print(5 * 3)
# print(6 / 2)
# print(3 ** 2)
#
# print()
# print("See if you can figure this out")
# print(100 % 3)
#
# # Variables
# car_name = "Wiebe Mobile"
# car_type = "Lamborghini Sesto Elemento"
# car_cylinders = 8
# car_mpg = 9000.1
#
# # Inline Printing
# print("My car is the %s." % car_name)
# print("My car is the %s. It is a %s" % (car_name, car_type))
#
# # Taking input
# name = input("What is your name? ")
# print("Hello %s." % name)
# print(name)
#
# age = input("What is your age? ")
# print("%s is a nice age to be in." % age)
#
# # Initializing Variable
# answer = random.randint(1, 50)
# turns_left = 5
# correct_guess = False
#
# # Describes exactly ONE turn. The while loop is the Game Controller.
# while turns_left > 0 and correct_guess is False:
#     guess = int(input("Guess a number between 1 and 50: "))
#     if guess == answer:
#         print()

# Lists

# the_count = [1, 2, 3, 4, 5]
# # characters = ["graves", "Dory", "Boots", "Dora", "Shrek", "Odi-Man", "Ian", "Carl"]
# print(characters[0])
# print(characters[4])
#
# print(len(characters))
#
# # Going through lists
# for char in characters:
#     print(char)
#
# for num in the_count:
#     print(num ** 2)
#
# len(characters)
# range(3)  # Makes a list of the number from 0 to 2
# range(len(characters))  # Make a list of ALL INDICES
#
# for num in range(len(characters)):
#     char = characters[num]
#     print("The character at index %d is %s" % (num, char))
#
# str1 = "Hello World!"  # Start counting from 0
# listOne = list(str1)
# print(listOne)
# listOne[11] = '.'
# print(listOne)
# newStr = "".join(listOne)
# print(newStr)
#
# # Adding stuff to list
#
# characters.append("Ironman/Batman/whomever you want")
# print(characters)
#
# characters.append("Black Panther")
#
# # Removing stuff from list
#
# characters.remove("Carl")
#
# characters.pop(6)
# print(characters)

# The string class
# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.punctuation)
#
# strTwo = 'tHiS sEntEnCe iS uNuSuAl'
# lowercase = strTwo.lower()
# print(lowercase)
# uppercase = strTwo.upper()
# print(uppercase)
# # Hangman Board
# """
# Make a list for the word, letter by letter.
# Add the letters guessed by the user to another list
# """

# Dictionaries - Make up a key: value pair
dictionary = {'name': 'Lance', 'age': 18, "height": 6 * 12 + 2}

# Accessing from a dictionary
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

large_dictionary = {
    "California": "CA",
    "Washington": "WA",
    "Florida": "FL"
}

print(large_dictionary['Florida'])

larger_dictionary = {
    "California": [
        "Fresno",
        "Sacramento",
        "Los Angeles"
    ],
    "Washington": [
        "Seattle",
        "Tacoma",
        "Olympia",
        "Spokane"
    ],
    "Illinois": [
        "Chicago",
        "Naperville",
        "Peoria"
    ],
}

print(larger_dictionary["Illinois"])
print(larger_dictionary["Illinois"][0])

# Spokane
print(larger_dictionary["Washington"][3])

largest_dictionary = {
    "CA": {
        'NAME': "California",
        'Population': 39250000,
        'BORDER ST': [
            'Oregon',
            "Nevada",
            "Arizona"
        ],
    },
    "MI": {
        "NAME": "Michigan",
        "POPULATION": 9928000,
        "BORDER ST": [
            'Wisconsin',
            'Ohio',
            "Indiana"
        ]
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 2610000,
        "BORDER ST": [
            'Georgia',
            'Alabama'
        ]
    }
}
print(largest_dictionary["MI"]["BORDER ST"][1])
print(largest_dictionary["FL"]["NAME"])
