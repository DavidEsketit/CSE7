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
    def __init__(self, name, health, damage, heal, takeDamage, description):
        self.name = name
        self.health = health
        self.description = description
        self.damage = damage
        self.heal = heal
        self.takeDamage = takeDamage


you = Characters("VENOM", 200, 30, 20, 30, "You are yourself.")
shrek = Characters("Shrek", 200, 30, 20, 30, "A tall green man with a bald head and a huge mouth and nose.")
ian = Characters("Ian", 200, 30, 20, 30, "A christian boi who wears glasses "
                                         "and is a faulty Mexican who is also Alek's twin brother.")
alek = Characters("Alek", 200, 30, 20, 30, "The owner of a Christian minecraft server who is also Ian's twin brother.")
print("There are three characters infront of you. Which would you like to fight?")

while True:
    characters = [shrek, ian, alek]
    command = input('>_').lower().strip()
    current_character = None
    print(current_character)
    if command in characters:
        current_character = command

    def attack():
        if command == 'attack':
            current_character.health -= you.damage
            print(current_character.health)


    attack()
