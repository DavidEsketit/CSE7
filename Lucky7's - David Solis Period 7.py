# David Solis 1/17/18
import random
money = 15
played = 0
most_money = 0
total_rounds = 0
broke = False

while money > 0 and broke is False:
    dice1 = (random.randint(0, 6))
    dice2 = (random.randint(0, 6))
    print("dice 1 : %s" % dice1)
    print("dice 2 : %s" % dice2)
    played += 1
    roll = (dice1 + dice2)
    print("This is round %s" % played)

    if roll == 7:
        money += 4
        if money > most_money:
            most_money = money
            total_rounds = played
    elif roll != 7:
        money -= 1
        print("You got $%s" % money)


if money == 0:
    print("You've played %s rounds!" % str(played))
    if most_money < 15:
        print("You should've never played this game in the first place, you didn't earn anything, SHAME.")
    elif most_money > 14:
        print("You should've stopped at round %s when you had $%s" % (total_rounds, most_money))
    broke = True
