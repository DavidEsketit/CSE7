import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1,6)
money = 15
trial = 0
number = dice1 + dice2
print("Welcome to Lucky 7's!" )

while money > 0:
    if number == 7:
        money += 4
        trial += 1
        print("cOoL")
    elif number
        