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

the_count = [1, 2, 3, 4, 5]
characters = ["graves", "Dory", "Boots", "Dora", "Shrek", "Odi-Man", "Ian"]
print(characters[0])
print(characters[4])

print(len(characters))

# Going through lists
for char in characters:
    print(char)

for num in the_count:
    print(num ** 2)

len(characters)
range(3)  # Makes a list of the number from 0 to 2
range(len(characters))  # Make a list of ALL INDICES

for num in range(len(characters)):
    char = characters[num]
    print("The character at index %d is %s" % (num, char))

str1 = "Hello World!"  # Start counting from 0
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
newStr = "".join(listOne)
print(newStr)

#