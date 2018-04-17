"""
Characters:
    1. Shrek - Can yell and damage your hearing, run fast, jump scares, spit acid on you
    2. Ian - Can give you directions
    3. Alek - Christian Minecraft server owner
    4. Christian - Contains Ring of Gyges, a god but and atheist, dies with hood on head
    5. Denim - Can shoot arrows from afar, can become friend or foe, if foe then he becomes a boos in the game
    6. Auckland - Can pay to win cost is ring of Gyges
    7. Ronald McDonald - Can lead you to the groceries isle
    8. Man In Corner - Can kill you if you look at him, located in parking pharmacy
"""
"""
Name:
Description:
Dialogue?
Inventory:
Interact
Move?
Climb
Look
Item
Fight
Health
takeDamage
"""


class Characters(object):
    def __init__(self, name, health, damage, heal, takedamage, description):
        self.name = name
        self.health = health
        self.description = description
        self.damage = damage
        self.heal = heal
        self.takeDamage = takedamage


you = Characters("Your Name", 200, 30, 20, 30, "You are yourself")
shrek = Characters("Shrek", 200, 30, 20, 30, "A tall green man with a bald head and a huge mouth and nose.")

print("You are fighting Shrek. He has 200 health and you also have a health of 200.")


def description_of_enemy():
    print("Your enemy is %s" % shrek.description.lower())


description_of_enemy()


if shrek.health > 0 or you.health > 0:
    def attack():
        shrek.health -= you.damage
        print("You have attacked Shrek.")
        print("Shrek's health is now at %s" % shrek.health)


    attack()


def heal_yourself():
    print("Healing...")
    you.health += you.heal
    print("Your health is now at %s" % you.health)


heal_yourself()


def take_damage():
    you.health -= shrek.damage
    print("Shrek has attacked you.")
    print("Your health is now at %s" % you.health)


take_damage()


heal_yourself()
