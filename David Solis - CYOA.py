#  1. import statements
#  2. Class Definitions
#       Items
#       Characters
#       Rooms
#  Instantiation of classes
#  Controller


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Armor(Item):
    def __init__(self, name, description, armor_amount):
        super(Armor, self).__init__(name, description)
        self.armor_amount = armor_amount


class ExoticA(Armor):  # A stands for Armor
    def __init__(self, name, description, armor_amount, exotica_factor):
        super(ExoticA, self).__init__(name, description, armor_amount)
        self.exoticA_factor = exotica_factor


class DiamondC(ExoticA):  # C stands for clothing
    def __init__(self):
        super(DiamondC, self).__init__('Diamond Clothing',
                                       'A very heavy clothing but gives you the power to summon diamond walls.',
                                       100, 'Gives you the power to summon walls that block damage.')


class EmeraldC(ExoticA):
    def __init__(self):
        super(EmeraldC, self).__init__('Emerald Clothing', 'A more light weight clothing made out of emerald.', 100,
                                       'Allows you to deflect 40% of the damage.')


class PlatinumC(ExoticA):
    def __init__(self):
        super(PlatinumC, self).__init__('Platinum Clothing', 'A heavy piece of armor that is made of platinum.', 100,
                                        'Gives you the power to now be affected by common weapons.')


class RareA(Armor):
    def __init__(self, name, description, armor_amount, rarea_factor):
        super(RareA, self).__init__(name, description, armor_amount)
        self.rareA_factor = rarea_factor


class IronC(RareA):
    def __init__(self):
        super(IronC, self).__init__('Iron Clothing', 'A reasonable weight armor that is made of Iron', 50,
                                    'Can block 20% of the damage from any weapon except exotic weapons.')


class MetalC(RareA):
    def __init__(self):
        super(MetalC, self).__init__('Metal Clothing', 'An armor made out of metal on the more heavy side.', 60,
                                     'Can block 25% of the damage from any weapon except exotic weapons.')


class WoodC(RareA):
    def __init__(self):
        super(WoodC, self).__init__('Wood Clothing', 'An armor made out of wood that is very light weight.', 40,
                                    'Can block 15% of the damage from any weapon except exotic weapons.')


class CommonA(Armor):
    def __init__(self, name, description, armor_amount, commona_factor):
        super(CommonA, self).__init__(name, description, armor_amount)
        self.commonA_factor = commona_factor


class CottonC(CommonA):
    def __init__(self):
        super(CottonC, self).__init__('Cotton Clothing', 'A regular t-shirt.', 0, 'Has a 0.0000000001% '
                                                                                  'chance that you will become '
                                                                                  'invincible to everything.')


class BronzeC(CommonA):
    def __init__(self):
        super(BronzeC, self).__init__('Bronze Clothing', 'A light weight armor that is made out of bronze.', 20,
                                      'Can block 10% of damage conflicted by anything except exotic weapons.')


class ChainC(CommonA):
    def __init__(self):
        super(ChainC, self).__init__('Chain Clothing', 'An armor made out of chain.', 10,
                                     'Can block 5% of damage conflicted by anything expect exotic weapons.')


class Weapon(Item):
    def __init__(self, name, description, damage_amount):
        super(Weapon, self).__init__(name, description)
        self.damage_amount = damage_amount


class ExoticW(Weapon):
    def __init__(self, name, description, damage_amount, exoticw_factor):
        super(ExoticW, self).__init__(name, description, damage_amount)
        self.exoticW_factor = exoticw_factor


class RayG(ExoticW):
    def __init__(self):
        super(RayG, self).__init__('Ray Gun', 'A gun from the game called Call of Duty: Black Ops', 40,
                                   'The most powerful weapon known to mankind.')


class WonderW(ExoticW):
    def __init__(self):
        super(WonderW, self).__init__('Wonder Waffle', 'A gun from the game called Call of Duty: Black Ops', 40,
                                      'Blows things away from you and also does instant kills '
                                      'but takes 20 seconds to reload.')


class RaygII(ExoticW):
    def __init__(self):
        super(RaygII, self).__init__('Ray Gun Mark II', 'A gun from the game called Call of Duty: Black Ops', 40,
                                     'Has a 20% chance that gun will nuke the Wal-Mart and win the game for you.')


class RareW(Weapon):
    def __init__(self, name, description, damage_amount, rarew_factor):
        super(RareW, self).__init__(name, description, damage_amount)
        self.rareW_factor = rarew_factor


class Rocketl(RareW):
    def __init__(self):
        super(Rocketl, self).__init__('Rocket Launcher', 'A long damage dealing weapon that launches rockets.', 30,
                                      'Also damages nearby enemies caught or near the blast of the rocket.')


class Assaultr(RareW):
    def __init__(self):
        super(Assaultr, self).__init__('Assault Rifle', 'An automatic rifle that does quite a bit of damage.', 30,
                                       'Can shoot faster than any other weapon in the game.')


class Revolver(RareW):
    def __init__(self):
        super(Revolver, self).__init__('Revolver', 'A damage dealing pistol that with 6 bullets.', 30,
                                       'Can shoot the all rounds in less than one second like McCree from Overwatch.')


class CommonW(Weapon):
    def __init__(self, name, description, damage_amount, commonw_factor):
        super(CommonW, self).__init__(name, description, damage_amount)
        self.commonW_factor = commonw_factor


class Pistol(CommonA):
    def __init__(self):
        super(Pistol, self).__init__('Pistol', 'A semi-automatic pistol with 16 bullets in each magazine.', 10,
                                     'Can only shoot once at a time.')


class Shotgun(CommonA):
    def __init__(self):
        super(Shotgun, self).__init__('Shotgun', 'A shotgun that does more damage than the average common weapon.', 15,
                                      'Can shoot multiple people wih on shot.')


class Grenade(CommonA):
    def __init__(self):
        super(Grenade, self).__init__('Grenade', 'A grenade that does an instant kill but only if '
                                                 'person is close to grenade.', 20, 'Can do damage to multiple '
                                                                                    'players at the same time.')


class Potion(Item):
    def __init__(self, name, description, potion_ability):
        super(Potion, self).__init__(name, description)
        self.potion_ability = potion_ability


class ExoticP(Potion):
    def __init__(self, name, description, potion_ability, exoticp_factor):
        super(ExoticP, self).__init__(name, description, potion_ability)
        self.exoticP_factor = exoticp_factor


class HealingP(ExoticP):
    def __init__(self):
        super(HealingP, self).__init__('Ultra Healing Potion',
                                       'A magical potion from the unknown that has a yellow glow to it.',
                                       'A potion that significantly heals you.', 'Can recover 60% of your health.')


class RevivingP(ExoticP):
    def __init__(self):
        super(RevivingP, self).__init__('Reviving Potion', 'A potion from the gods that can do the impossible.',
                                        'Can recover 100% of your health.',
                                        'If you are dead and have the item in your inventory, '
                                        'this can revive you from the dead.')


class SuicideP(ExoticP):
    def __init__(self):
        super(SuicideP, self).__init__('Suicide Potion', 'A potion from hell with a devilish look to it.',
                                       'Can kill you in an instant.',
                                       'If potion is drunk, you will get text that will say you win')


class RareP(Potion):
    def __init__(self, name, description, potion_ability, rare_factor):
        super(RareP, self).__init__(name, description, potion_ability)
        self.rare_factor = rare_factor


class RegHealP(RareP):
    def __init__(self):
        super(RegHealP, self).__init__('Regular Healing Potion',
                                       'A potion with a yellow tint but not as bright as the Exotic Healing Potion.',
                                       'Can heal a small portion of your health.', 'Heals 20% of your total health.')


class DamageP(RareP):
    def __init__(self):
        super(DamageP, self).__init__('Damage Potion', 'A potion with a bright red tint with smoke coming out of it.',
                                      'Can damage other characters by 20% over time.',
                                      'Can be thrown at someone and be spread if other people are near.')


class ArmorP(RareP):
    def __init__(self):
        super(ArmorP, self).__init__('Armor Potion',
                                     'A potion with a blue tint with blue smoke coming out from the top.',
                                     'When drunken, it gives you 40% armor.',
                                     'Armor can block 20% of any weapon damage.')


class CommonP(Potion):
    def __init__(self, name, description, potion_ability, common_factor):
        super(CommonP, self).__init__(name, description, potion_ability)
        self.common_factor = common_factor


class CommonHealingP(CommonP):
    def __init__(self):
        super(CommonHealingP, self).__init__('Common Healing Potion',
                                             'An almost clear looking potion with a very unnoticeable yellow tint.',
                                             'Can heal a small amount of your health.', 'Heals 10% of your health.')


class CommonDamageP(CommonP):
    def __init__(self):
        super(CommonDamageP, self).__init__('Common Damage Potion', 'A potion that looks very devilish.',
                                            'Can deal a small amount of damage to another character''s health.',
                                            'Does 10% damage to any_nearby enemy.')


class CommonArmorPotion(CommonP):
    def __init__(self):
        super(CommonArmorPotion, self).__init__('Common Damage Potion',
                                                'A potion that looks like hte fortnite potion that gives you of armor.',
                                                'Can add a small amount of health to your armor.',
                                                ' Adds 10% of health to your armor.')


class Characters(object):
    def __init__(self, name, health, damage, heal, takedamage, description):
        self.name = name
        self.health = health
        self.description = description
        self.damage = damage
        self.heal = heal
        self.takeDamage = takedamage


inventory = [RayG, Revolver]
you = Characters("Your Name", 200, 30, 20, 30, "You are yourself") and inventory

shrek = Characters("Shrek", 200, 30, 20, 30, "A tall green man with a bald head and a huge mouth and nose.")

print(RayG.description)


def description_of_enemy():
    print("Your enemy is %s" % shrek.description.lower())


if shrek.health > 0 or you.health > 0:
    def attack():
        shrek.health -= you.damage
        print("You have attacked Shrek.")
        print("Shrek's health is now at %s" % shrek.health)


def heal_yourself():
    print("Healing...")
    you.health += you.heal
    print("Your health is now at %s" % you.health)


def take_damage():
    you.health -= shrek.damage
    print("Shrek has attacked you.")
    print("Your health is now at %s" % you.health)


class Room(object):
    def __init__(self, name, north, east, south, west, description):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Rooms


parking_lot = Room("Parking Lot", None, None, 'pharmacy', None, "You are in a parking lot, there are no cars and there "
                                                                "is an open door in the south to Wal-Mart.")
pharmacy = Room("Pharmacy", 'parking_lot', 'health_and_beauty', 'home', None, "You are in a parking lot, there are no "
                                                                              "cars and there is an open door in the "
                                                                              "south to Wal-Mart")
jewelery = Room("Jewelery", None, None, 'apparel', None, "The jewelery seems to be untouched. To the South of you there"
                                                         "looks to be like clothes.")
home = Room("Home", 'pharmacy', 'toys', None, None, "There is a lot of furniture around you and when you walk on the "
                                                    "floor is squeaky.")
toys = Room("Toys", 'lawn_and_garden', 'home', 'sporting_goods', None, "You in a section with toys. There are pretend "
                                                                       "swords and RC cars.")
lawn_and_garden = Room("Lawn and Garden", None, None, 'toys', 'cosmetics', "There is one lawn mower left with some soil"
                                                                           "next to it, everything else looks to be old"
                                                                           " and moldy")
cosmetics = Room("Cosmetics", None, 'lawn_and_garden', None, 'health', "All the make up looks untouched. There are "
                                                                       "bushes on the table in front of you.")
health_and_beauty = Room("Health and Beauty", None, 'cosmetics', None, 'pharmacy', "There is a lot of lotion and your "
                                                                                   "skin is dry. There are extensions "
                                                                                   "for your hair lying on the ground")
sporting_goods = Room("Sporting Goods", 'toys', None, 'auto_care', None, "There are multiple bats hung up on the wall. "
                                                                         "There are also some balls on the floor.")
shoes = Room("Shoes", None, None, None, 'apparel', "There are some very comfortable shoes "
                                                   "called the comfortable shoes 9000.")
baby = Room("Baby", None, 'apparel', 'pets', None, "There is a baby in one of the cribs. There also looks to be "
                                                   "food to the East of you.")
pets = Room("Pets", 'baby', 'paper_and_cleaning', None, 'books_and_magazines', "You are in the pets section. "
                                                                               "There are multiple fish tanks with a "
                                                                               "lot of dead fish in it.")
paper_and_cleaning = Room("Paper and Cleaning", 'baby', 'groceries', None, 'pets', "There is bleach on the floor "
                                                                                   "and full containers on the shelves."
                                                                                   " There are also some cleaning "
                                                                                   "gloves on the floor.")
groceries = Room("Groceries", None, 'paper_and_cleaning', None, None, "All the food is gone and but there is a lot "
                                                                      "of water in front of you.")
apparel = Room("Apparel", 'jewelery', 'shoes', None, 'baby', "There are multiple graphic tees with zombies on them.")
restrooms = Room("Restrooms", None, None, 'books_and_magazines', 'photos', "There is a toilet in front of you with a "
                                                                           "sink next to it with some soap.")
photos = Room("Photos", None, 'restrooms', 'electronics', None, "There are several pictures of families on the wall.")
electronics = Room("Electronics", 'photos', 'crafts', None, None, "There is an iPhone 20 X on the ground. All the tvs "
                                                                  "are gone.")

# Controller

directions = ['north', 'east', 'south', 'west']
current_node = parking_lot
short_directions = ['n', 'e', 's', 'w']
while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions[pos]
    if command == 'meme big boy':
        print("Memes are bad for you.")
        quit(0)
    if command == 'hello world':
        print("The world says hi back.")
    if command == 'bitconnect':
        print("BIT-CONNECT!")
    if command == 'bad word':
        print("Not in my Christian minecraft server.")
        quit(0)
    if command == 'look':
        print(current_node.description)
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way")
    elif command is not True:
        print("Command not found.")
    print()
