class Room(object):
    def __init__(self, name, north, east, south, west, description):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.description = description


    def move(self, direction):
        current_node = globals()[getattr(self, direction)]
        global current_node


parking_lot = Room("Parking Lot", None, None, 'pharmacy', None, "You are in a parking lot, there are no cars and there "
                                                                "is an open door in the south to Wal-Mart.")
pharmacy = Room("Pharmacy", 'parking_lot', 'health_and_beauty', 'home', None, "You are in a parking lot, there are no "
                                                                              "cars and there is an open door in the "
                                                                              "south to Wal-Mart")
jewelery = Room("Jewelery", None, None, 'apparel', None, "The jewelery seems to be untouched. To the South of you there"
                                                         "looks to be like clothes.")
home = Room("Home", 'pharmacy', 'toys', None, 'home_and_office', "There is a lot of furniture around you and when you "
                                                                 "walk on the floor is squeaky.")
toys = Room("Toys", 'lawn_and_garden', 'home', 'sporting_goods', None, "You in a section with toys. There are pretend "
                                                                       "swords and RC cars.")
lawn_and_garden = Room("Lawn and Garden", None, None, 'toys', 'cosmetics', "There is one lawn mower left with some soil"
                                                                           "next to it, everything else looks to be old"
                                                                           " and moldy")
cosmetics = Room("Cosmetics", None, 'lawn_and_garden', None, 'health')