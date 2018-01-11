import random
money = 15
trial = 0
print("Welcome to Lucky 7's!")

while money > 0:
    most_money = 0
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    number = dice1 + dice2
    if number == 7:
        money += 4
        trial += 1
        print("cOoL")
        print("You have %s dollar(s)left" % money)
    elif number != 7:
        money -= 1
        trial += 1
        print("dummy")
        print("You have %s dollar(s)left" % money)
    if money > most_money:
        most_money + money


def no_money():
    if money is 0:
        print("You have no money left :(")
        print("You rolled %s times" % trial)
        print("The most money you had was %s" % most_money)


no_money()
