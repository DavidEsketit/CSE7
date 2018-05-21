import random


class Characters(object):
    def __init__(self, name, inventory, health, description, attack):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.description = description
        self.attack = attack
        self.death = False

    def take_damage(self, amount):
        self.health -= amount

    def swing(self, enemigo):
        enemigo.take_damage(self.attack)
        print("You attacked %s." % enemigo.name)
        if enemigo.health <= 0:
            enemigo.death = True
            print("%s died." % enemigo.name)

    def fight(self, enemigo):
        print("You start a fight with %s" % enemigo.name)

        while self.health != 0:
            choice = random.choice([enemigo, self])
            if choice == self:
                enemigo.swing(self)
            elif choice == enemigo:
                self.swing(enemigo)


you = Characters("Your Name", [], 100, "You are yourself", random.randint(1, 10))
shrek = Characters("Shrek", [], 100, "A tall green man with a bald head and a huge mouth and nose.",
                   random.random.randint(1, 20))

you.fight(shrek)
