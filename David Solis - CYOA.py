#  1. import statements
#  2. Class Definitions
#       Items
#       Characters
#       Rooms
#  Instantiation of classes
#  Controller
import random
import webbrowser


class Item(object):
    def __init__(self, name, description, value, shop_number):
        self.name = name
        self.description = description
        self.value = value
        self.shop_number = shop_number


class Armor(Item):
    def __init__(self, name, description, value, shop_number, armor_amount):
        super(Armor, self).__init__(name, description, value, shop_number)
        self.armor_amount = armor_amount


class ExoticA(Armor):  # A stands for Armor
    def __init__(self, name, description, value, shop_number, armor_amount, exotica_factor):
        super(ExoticA, self).__init__(name, description, value, shop_number, armor_amount)
        self.exoticA_factor = exotica_factor


diamond_clothing = ExoticA('Diamond Clothing',
                           'A very heavy clothing but gives you the power to summon diamond walls.', 500, 4, 100,
                           'Gives you the power to summon walls that block damage.')


emerald_clothing = ExoticA('Emerald Clothing',
                           'A more light weight clothing made out of emerald.', 500, 3, 100,
                           'Allows you to deflect 40% of the damage.')


platinum_clothing = ExoticA('Platinum Clothing',
                            'A heavy piece of armor that is made of platinum.', 500, None, 100,
                            'Gives you the power to now be affected by common weapons.')


class RareA(Armor):
    def __init__(self, name, description, value, shop_number, armor_amount, rarea_factor):
        super(RareA, self).__init__(name, description, value, shop_number, armor_amount)
        self.rareA_factor = rarea_factor


iron_clothing = RareA('Iron Clothing',
                      'A reasonable weight armor that is made of Iron', 280, 5, 50,
                      'Can block 20% of the damage from any weapon except exotic weapons.')


metal_clothing = RareA('Metal Clothing',
                       'An armor made out of metal on the more heavy side.', 300, 6, 60,
                       'Can block 25% of the damage from any weapon except exotic weapons.')


wood_clothing = RareA('Wood Clothing',
                      'An armor made out of wood that is very light weight.', 250, 7, 40,
                      'Can block 15% of the damage from any weapon except exotic weapons.')


class CommonA(Armor):
    def __init__(self, name, description, value, shop_number, armor_amount, commona_factor):
        super(CommonA, self).__init__(name, description, value, shop_number, armor_amount)
        self.commonA_factor = commona_factor


cotton_clothing = CommonA('Cotton Clothing', 'A regular t-shirt.', 0, None, 0,
                          'Has a 0.0000000001% chance that you will become invincible to everything.')


bronze_clothing = CommonA('Bronze Clothing',
                          'A light weight armor that is made out of bronze.', 100, 1, 20,
                          'Can block 10% of damage conflicted by anything except exotic weapons.')


chain_clothing = CommonA('Chain Clothing', 'An armor made out of chain.', 50, 2, 10,
                         'Can block 5% of damage conflicted by anything expect exotic weapons.')


class Weapon(Item):
    def __init__(self, name, description, value, shop_number, damage_amount):
        super(Weapon, self).__init__(name, description, value, shop_number)
        self.damage_amount = damage_amount


class ExoticW(Weapon):
    def __init__(self, name, description, value, shop_number, damage_amount, exoticw_factor):
        super(ExoticW, self).__init__(name, description, value, shop_number, damage_amount)
        self.exoticW_factor = exoticw_factor


ray_gun = ExoticW('Ray Gun', 'A gun from the game called Call of Duty: Black Ops', 600, None, 40,
                  'The most powerful weapon known to mankind.')


wonder_waffle = ExoticW('Wonder Waffle', 'A gun from the game called Call of Duty: Black Ops', 560, 8, 40,
                        'Blows things away from you and also does instant kills but takes 20 seconds to reload.')


ray_gun_mark11 = ExoticW('Ray Gun Mark II', 'A gun from the game called Call of Duty: Black Ops', 550, 9, 40,
                         'Has a 20% chance that gun will nuke the Wal-Mart and win the game for you.')


class RareW(Weapon):
    def __init__(self, name, description, value, shop_number, damage_amount, rarew_factor):
        super(RareW, self).__init__(name, description, value, shop_number, damage_amount)
        self.rareW_factor = rarew_factor


rocket_launcher = RareW('Rocket Launcher', 'A long damage dealing weapon that launches rockets.', 300, None, 30,
                        'Also damages nearby enemies caught or near the blast of the rocket.')


assault_rifle = RareW('Assault Rifle', 'An automatic rifle that does quite a bit of damage.', 280, None, 30,
                      'Can shoot faster than any other weapon in the game.')


revolver = RareW('Revolver', 'A damage dealing pistol that with 6 bullets.', 250, None, 30,
                 'Can shoot the all rounds in less than one second like McCree from Overwatch.')


class CommonW(Weapon):
    def __init__(self, name, description, value, shop_number, damage_amount, commonw_factor):
        super(CommonW, self).__init__(name, description, value, shop_number, damage_amount)
        self.commonW_factor = commonw_factor


pistol = CommonA('Pistol', 'A semi-automatic pistol with 16 bullets in each magazine.', 100, None, 10,
                 'Can only shoot once at a time.')


shotgun = CommonA('Shotgun', 'A shotgun that does more damage than the average common weapon.', 130, None, 15,
                  'Can shoot multiple people wih on shot.')


grenade = CommonA('Grenade', 'A grenade that does an instant kill but only if person is close to grenade.', 150, None,
                  20, 'Can do damage to multiple players at the same time.')

all_armor = [diamond_clothing, emerald_clothing, platinum_clothing, iron_clothing, metal_clothing, wood_clothing,
             bronze_clothing, chain_clothing, cotton_clothing]
all_weapons = [ray_gun, wonder_waffle, ray_gun_mark11, rocket_launcher, assault_rifle, revolver, grenade]


class Potion(Item):
    def __init__(self, name, description, value, shop_number, potion_ability):
        super(Potion, self).__init__(name, description, value, shop_number)
        self.potion_ability = potion_ability


class ExoticP(Potion):
    def __init__(self, name, description, value, shop_number, potion_ability, exoticp_factor):
        super(ExoticP, self).__init__(name, description, value, shop_number, potion_ability)
        self.exoticP_factor = exoticp_factor


ultra_healing_potion = ExoticP('Ultra Healing Potion',
                               'A magical potion from the unknown that has a yellow glow to it.', 500, None,
                               100, 'Can recover 60% of your health.')


reviving_potion = ExoticP('Reviving Potion', 'A potion from the gods that can do the impossible.', 600, None,
                          100,
                          'If you are dead and have the item in your inventory, this can revive you from the dead.')


suicide_potion = ExoticP('Suicide Potion', 'A potion from hell with a devilish look to it.', 1000, None,
                         1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
                         'If potion is drunk, you will get text that will say you win')


class RareP(Potion):
    def __init__(self, name, description, value, shop_number, potion_ability, rare_factor):
        super(RareP, self).__init__(name, description, value, shop_number, potion_ability)
        self.rare_factor = rare_factor


regular_healing_potion = RareP('Regular Healing Potion',
                               'A potion with a yellow tint but not as bright as the Exotic Healing Potion.', 300, None,
                               20, 'Heals 20% of your total health.')


damage_potion = RareP('Damage Potion', 'A potion with a bright red tint with smoke coming out of it.',
                      280, None, 20,
                      'Can be thrown at someone and be spread if other people are near.')


armor_potion = RareP('Armor Potion', 'A potion with a blue tint with blue smoke coming out from the top.',
                     320, None, 40,
                     'Armor can block 20% of any weapon damage.')


class CommonP(Potion):
    def __init__(self, name, description, value, shop_number, potion_ability, common_factor):
        super(CommonP, self).__init__(name, description, value, shop_number, potion_ability)
        self.common_factor = common_factor


common_healing_potion = CommonP('Common Healing Potion',
                                'An almost clear looking potion with a very unnoticeable yellow tint.',
                                10, None, 200, 'Heals 10% of your health.')


common_damage_potion = CommonP('Common Damage Potion', 'A potion that looks very devilish.',
                               10, None, 180, 'Does 10% damage to any_nearby enemy.')


common_armor_potion = CommonP('Common Armor Potion',
                              'A potion that looks like hte fortnite potion that gives you of armor.',
                              10, None, 210, 'Adds 10% of health to your armor.')

healing_potions = [ultra_healing_potion, regular_healing_potion, common_healing_potion]
armor_potions = [armor_potion, common_armor_potion]
damage_potions = [suicide_potion, damage_potion, armor_potion, common_armor_potion]
all_potions = [ultra_healing_potion, regular_healing_potion, common_healing_potion, armor_potion, common_armor_potion,
               suicide_potion, damage_potion, armor_potion, common_armor_potion]


class Characters(object):
    def __init__(self, name, health, char_description, attack, armor, dinero):
        self.name = name
        self.health = health
        self.char_description = char_description
        self.attack = attack
        self.death = False
        self.armor = armor
        self.dinero = dinero

    def take_damage(self, amount):
        self.health -= amount


class Inventory:
    def __init__(self, weapon, armor, potion):
        self.weapon = weapon
        self.armor = armor
        self.potion = potion


you = Characters("Your Name", 100, "You are yourself", 100, 0, 100)
shrek = Characters("Shrek", 100, "A tall green man with a bald head and a huge mouth and nose.", 20, 100, None)
# rip your code


class Room(object):
    def __init__(self, name, north, east, south, west, room_description, item_in_room, is_shrek_room):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.room_description = room_description
        self.item_in_room = item_in_room
        self.is_shrek_room = is_shrek_room

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Rooms


parking_lot = Room("Parking Lot", None, None, 'pharmacy', None, "You are in a parking lot, there are no cars and there "
                   "is an open door in the south to Wal-Mart. There is also some clothing on the ground.",
                   cotton_clothing, shrek)
pharmacy = Room("Pharmacy", 'parking_lot', 'health_and_beauty', 'home', None, "You are in a parking lot, there are no "
                "cars and there is an open door in the south to Wal-Mart. There is also a pistol on the ground.",
                pistol, None)
jewelery = Room("Jewelery", None, None, 'apparel', None, "The jewelery seems to be untouched. To the South of you there"
                "looks to be like clothes. There is also a grenade lying on the ground which seems to be safe.",
                grenade, None)
home = Room("Home", 'pharmacy', 'toys', None, None, "There is a lot of furniture around you and when you walk on the "
            "floor is squeaky. There is also a shotgun on a couch.", shotgun, None)
toys = Room("Toys", 'lawn_and_garden', 'home', 'sporting_goods', None, "You in a section with toys. There are pretend "
            "swords and RC cars. There is also some kind of potion in a toy.", regular_healing_potion, None)
lawn_and_garden = Room("Lawn and Garden", None, None, 'toys', 'cosmetics', "There is one lawn mower left with some soil"
                       "next to it, everything else looks to be old and moldy. There is also a revolver on top of a "
                       "lawn mower.", revolver, None)
cosmetics = Room("Cosmetics", None, 'lawn_and_garden', None, 'health', "All the make up looks untouched. There are "
                 "bushes on the table in front of you. There is also a potion in a makeup box.",
                 common_damage_potion, None)
health_and_beauty = Room("Health and Beauty", None, 'cosmetics', None, 'pharmacy', "There is a lot of lotion and your "
                         "skin is dry. There are extensions for your hair lying on the ground. There is also a wierd "
                         "looking potion on a shelf.", ultra_healing_potion, None)
sporting_goods = Room("Sporting Goods", 'toys', None, 'shoes', None,
                      "There are multiple bats hung up on the wall. There are also some balls on the floor.",
                      platinum_clothing, None)
shoes = Room("Shoes", 'sporting_goods', None, None, 'apparel',
             "There are some very comfortable shoes called the comfortable shoes 9000.", ray_gun, None)
baby = Room("Baby", None, 'apparel', 'pets', None, "There is a baby in one of the cribs. There also looks to be "
                                                   "food to the East of you.", assault_rifle, None)
pets = Room("Pets", 'baby', 'paper_and_cleaning', None, 'books_and_magazines', "You are in the pets section. "
                                                                               "There are multiple fish tanks with a "
                                                                               "lot of dead fish in it.",
            rocket_launcher, None)
paper_and_cleaning = Room("Paper and Cleaning", 'baby', 'groceries', None, 'pets', "There is bleach on the floor "
                                                                                   "and full containers on the shelves."
                                                                                   " There are also some cleaning "
                                                                                   "gloves on the floor.",
                          suicide_potion, None)

groceries = Room("Groceries", None, 'paper_and_cleaning', None, None, "All the food is gone and but there is a lot "
                                                                      "of water in front of you.", damage_potion, None)
apparel = Room("Apparel", 'jewelery', 'shoes', None, 'baby', "There are multiple graphic tees with zombies on them.",
               common_damage_potion, None)
restrooms = Room("Restrooms", None, None, 'books_and_magazines', 'photos', "There is a toilet in front of you with a "
                                                                           "sink next to it with some soap.",
                 reviving_potion, None)
photos = Room("Photos", None, 'restrooms', 'electronics', None, "There are several pictures of families on the wall.",
              metal_clothing, None)
electronics = Room("Electronics", 'photos', None, None, None,
                   "There is an iPhone 20 X on the ground. All the tvs are gone.", common_armor_potion, None)

all_rooms = [parking_lot, pharmacy, jewelery, home, toys, lawn_and_garden, cosmetics, health_and_beauty, sporting_goods,
             shoes, baby, pets, paper_and_cleaning, groceries, apparel, restrooms, photos, electronics]
inventory = Inventory(None, None, None)
# Controller

all_commands = ['north', 'east', 'south', 'west', 'n', 'e', 's', 'w', 'quit', 'attack', 'take', 'drink potion',
                'drop weapon', 'drop potion', 'drop armor', 'health', 'meme big boy', 'bitconnect', 'bad word', 'look',
                'inventory', 'shop', 'buy 1', 'buy 2', 'buy 3', 'buy 4', 'buy 5', 'buy 6', 'buy 7', 'buy 8', 'buy 9',
                'exit', 'snap']
shop_commands = ['buy 1', 'buy 2', 'buy 3', 'buy 4', 'buy 5', 'buy 6', 'buy 7', 'buy 8', 'buy 9', 'exit']
all_items_in_rooms = [cotton_clothing, pistol, grenade, shotgun, regular_healing_potion, revolver, common_damage_potion,
                      ultra_healing_potion, platinum_clothing, ray_gun, assault_rifle, rocket_launcher, suicide_potion,
                      damage_potion, common_damage_potion, reviving_potion, metal_clothing, common_armor_potion]
store_items = [bronze_clothing, chain_clothing, emerald_clothing, diamond_clothing, iron_clothing, metal_clothing,
               wood_clothing, wonder_waffle, ray_gun_mark11]
shrek_location = random.choices(all_rooms)
shrek_dead = 'false'
directions = ['north', 'east', 'south', 'west']
current_node = parking_lot
short_directions = ['n', 'e', 's', 'w']
while True:
    print(current_node.name)
    print(current_node.room_description)
    command = input('>_').lower().strip()
    attack_description = 'true'
    if you.health <= 0:
        print("You have died")
        quit()
    if command == 'quit':
        quit(0)

    elif command in short_directions:
        # Finds the command in short directions (index number)
        # Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions[pos]
    if command == 'shop':
        shop = True
        print("Shop")
        print("Items:")
        for i in store_items:
            print("(%s)%s ----- %s G" % (i.shop_number, i.name, i.value))
        print("If you wish to exit the shop, type 'exit' into the command.")
        while shop is True:
            print("Your Coins: %s G" % you.dinero)
            command = input('>_').lower().strip()
            if command == 'exit':
                print("You have exited the shop.")
                shop = False
            if command == 'buy 1' and inventory.armor is bronze_clothing:
                print("You already own that.")
            elif command == 'buy 2' and inventory.armor is chain_clothing:
                print("You already own that.")
            elif command == 'buy 3' and inventory.armor is emerald_clothing:
                print("You already own that.")
            elif command == 'buy 4' and inventory.armor is diamond_clothing:
                print("You already own that.")
            elif command == 'buy 5' and inventory.armor is iron_clothing:
                print("You already own that.")
            elif command == 'buy 6' and inventory.armor is metal_clothing:
                print("You already own that.")
            elif command == 'buy 7' and inventory.armor is wood_clothing:
                print("You already own that.")
            elif command == 'buy 8' and inventory.weapon is wonder_waffle:
                print("You already own that.")
            elif command == 'buy 9' and inventory.weapon is ray_gun_mark11:
                print("You already own that.")
            if command == 'buy 1' and inventory.armor is not bronze_clothing:
                if you.dinero >= bronze_clothing.value:
                    print("You have bought %s." % bronze_clothing.name)
                    you.dinero = you.dinero - bronze_clothing.value
                    inventory.armor = bronze_clothing
                    you.armor += inventory.armor.armor_amount
                else:
                    print("You don't have enough money to buy that.")

            elif command == 'buy 2' and inventory.armor is not chain_clothing:
                if you.dinero >= chain_clothing.value:
                    print("You have bought %s." % chain_clothing.name)
                    you.dinero = you.dinero - chain_clothing.value
                    inventory.armor = chain_clothing
                    you.armor += inventory.armor.armor_amount
                else:
                    print("You don't have enough money to buy that.")
            elif command == 'buy 3' and inventory.armor is not emerald_clothing:
                if you.dinero >= emerald_clothing.value:
                    print("You have bought %s." % emerald_clothing.name)
                    you.dinero = you.dinero - emerald_clothing.value
                    inventory.armor = emerald_clothing
                    you.armor += inventory.armor.armor_amount
                else:
                    print("You don't have enough money to buy that.")
            elif command == 'buy 4' and inventory.armor is not diamond_clothing:
                if you.dinero >= diamond_clothing.value:
                    print("You have bought %s." % diamond_clothing.name)
                    you.dinero = you.dinero - diamond_clothing.value
                    inventory.armor = diamond_clothing
                    you.armor += inventory.armor.armor_amount
                else:
                    print("You don't have enough money to buy that.")
            elif command == 'buy 5' and inventory.armor is not iron_clothing:
                if you.dinero >= iron_clothing.value:
                    print("You have bought %s." % iron_clothing.name)
                    you.dinero = you.dinero - iron_clothing.value
                    inventory.armor = iron_clothing
                    you.armor += inventory.armor.armor_amount
                else:
                    print("You don't have enough money to buy that.")
            elif command == 'buy 6' and inventory.armor is not metal_clothing:
                if you.dinero >= metal_clothing.value:
                    print("You have bought %s." % metal_clothing.name)
                    you.dinero = you.dinero - metal_clothing.value
                    inventory.armor = metal_clothing
                    you.armor += inventory.armor.armor_amount
                else:
                    print("You don't have enough money to buy that.")
            elif command == 'buy 7' and inventory.armor is not wood_clothing:
                if you.dinero >= wood_clothing.value:
                    print("You have bought %s." % wood_clothing.name)
                    you.dinero = you.dinero - wood_clothing.value
                    inventory.armor = wood_clothing
                    you.armor += inventory.armor.armor_amount
                else:
                    print("You don't have enough money to buy that.")
            elif command == 'buy 8' and inventory.weapon is not wonder_waffle:
                if you.dinero >= wonder_waffle.value:
                    print("You have bought %s." % wonder_waffle.name)
                    you.dinero = you.dinero - wonder_waffle.value
                    inventory.weapon = wonder_waffle
                    you.attack += inventory.weapon.damage_amount
                else:
                    print("You don't have enough money to buy that.")
            elif command == 'buy 9' and inventory.weapon is not ray_gun_mark11:
                if you.dinero >= ray_gun_mark11.value:
                    print("You have bought %s." % ray_gun_mark11.name)
                    you.dinero = you.dinero - ray_gun_mark11.value
                    inventory.weapon = ray_gun_mark11
                    you.attack += inventory.weapon.damage_amount
                else:
                    print("You don't have enough money to buy that.")
            if command not in shop_commands:
                print("Make sure that the you typed it as 'buy #'.")
    if command == 'attack':
        take_damage_or_no = random.randint(0, 1)
        if attack_description == 'true':
            attack_description = 'false'
            if shrek.health <= 0 and shrek_dead == 'false':
                shrek_dead = 'true'
                current_node.is_shrek_room = None
                restrooms.is_shrek_room = shrek
                you.dinero += 200
                print("Shrek is dead and has been resurrected by the Devil and is in a different room.")
                print("+200 G")
            elif current_node.is_shrek_room is None:
                print("Shrek is not in the room.")
            if current_node.is_shrek_room is shrek:
                if shrek.health >= 0:
                    if inventory.armor in all_armor and inventory.armor.armor_amount > 0:
                        inventory.armor -= shrek.attack
                        print("Pew pew!")
                        print("Shrek has lost %s health." % you.attack)
                    elif inventory.armor not in all_armor or inventory.armor.armor_amount <= 0:
                        shrek.health -= you.attack
                        print("Pew pew!")
                        print("Shrek has lost %s health" % you.attack)
                    if inventory.armor in all_armor and inventory.armor.armor_amount > 0:
                            if take_damage_or_no == 1:
                                inventory.armor.armor_amount -= shrek.attack
                                print("Shrek attacked back for %s" % shrek.attack)
                            else:
                                print("Shrek attacked back but you were able to block it.")
                    elif inventory.armor not in all_armor or inventory.armor.armor_amount <= 0:
                            if take_damage_or_no == 1:
                                you.health -= shrek.attack
                                print("Shrek attacked back for %s" % shrek.attack)
                            else:
                                print("Shrek attacked back but you were able to shield it with your mighty armor.")
    if command == 'take':
        if current_node.item_in_room in all_armor:
            print("You picked up a %s" % current_node.item_in_room.name)
            inventory.armor = current_node.item_in_room
            you.armor += inventory.armor.armor_amount
            current_node.item_in_room = None

        elif current_node.item_in_room in all_weapons:
            print("You picked up a %s" % current_node.item_in_room.name)
            inventory.weapon = current_node.item_in_room
            you.attack += inventory.weapon.damage_amount
            current_node.item_in_room = None

        elif current_node.item_in_room in all_potions:
            print("You picked up %s" % current_node.item_in_room.name)
            inventory.potion = current_node.item_in_room
            current_node.item_in_room = None

        else:
            print("There is nothing to take.")

    if command == 'drink potion':
        if inventory.potion in healing_potions:
            you.health += inventory.potion.potion_ability
            inventory.potion = None

        elif inventory.potion in damage_potions:
            you.attack += inventory.potion.potion_ability
            inventory.potion = None

        elif inventory.potion in armor_potions:
            you.armor += inventory.potion.potion_ability
            inventory.potion = None

        else:
            print("You have no potion to drink.")
    if command == 'snap':
        webbrowser.open("https://youtu.be/3jTad1iIc58")

    if command == 'drop weapon':
        current_node.item_in_room = inventory.weapon
        inventory.weapon = None

    if command == 'drop potion':
        current_node.item_in_room = inventory.potion
        inventory.potion = None

    if command == 'drop armor':
        current_node.item_in_room = inventory.armor
        inventory.armor = None

    if command == 'health':
        print("You have %s health and %s armor." % (you.health, you.armor))

    if command == 'meme big boy':
        print("Isn't that from pewdiepie")

    if command == 'hello world':
        print("The world says hi back.")

    if command == 'bitconnect':
        print("BIT-CONNECT!")

    if command == 'bad word':
        print("Not in my Christian minecraft server.")
        quit(0)

    if command == 'look':
        print(current_node.room_description)

    if command == 'inventory':
        if inventory.armor is not None:
            print(inventory.armor.name)

        else:
            print("You don't have armor.")

        if inventory.weapon is not None:
            print(inventory.weapon.name)

        else:
            print("You don't have a weapon.")

        if inventory.potion is not None:
            print(inventory.potion.name)

        else:
            print("You don't have armor.")

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way")

    elif command not in all_commands:
        print("Command not found.")
    print("___________________________________________________________________________________________________")
