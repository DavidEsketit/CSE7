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
    if command == 'hello world':
        print("The world says hi back.")
    if command == 'bitconnect':
        print("BIT-CONNECT!")
    if command == 'fuck':
        print("Profanity is not allowed in my game.")
        quit(0)
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way")
    else:
        print("Command not found.")
    print()
