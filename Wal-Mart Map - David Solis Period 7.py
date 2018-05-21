walmart = {
    'PARKING LOT': {
        'NAME': 'Parking Lot',
        'DESCRIPTION': 'You are in a parking lot, there are no cars and there is an open door in the south to Wal-Mart',
        'PATHS': {
            'South': "PHARMACY"
        }
    },
    'PHARMACY': {
        'NAME': 'Pharmacy',
        'DESCRIPTION': 'You are in the pharmacy, the supplies seem to be all gone except some bandages. There are some'
                'automatic doors to the South and another aisle to the East.',
        'PATHS': {
            'North': "PARKING LOT",
            'South': "HOME",
            'East': "HEALTH AND BEAUTY"
        }
    },
    'JEWELERY': {
        'NAME': 'Jewelery',
        'DESCRIPTION': 'The jewelery seems to be untouched. To the South of you there looks to be like clothes.',
        'PATHS': {
            'SOUTH': "APPAREL",
        }
    },
    'HOME': {
        'NAME': 'Home',
        'DESCRIPTION': 'There is a lot of furniture around you and when you walk on the floor is squeaky.',
        'PATHS': {
            'NORTH': "PHARMACY",
            'WEST': "HOME AND OFFICE",
            'EAST': "TOYS"
        }
    },
    'TOYS': {
        'NAME': 'Home',
        'DESCRIPTION': 'You in a section with toys. There are pretend swords and RC cars.',
        'PATHS': {
            'NORTH': "LAWN AND GARDEN",
            'EAST': "HOME",
            'SOUTH': "SPORTING GOODS"
        }
    },
    'LAWN AND GARDEN': {
        'NAME': 'Lawn and Garden',
        'DESCRIPTION': 'There is one lawn mower left with some soil next to it,'
                       'everything else looks to be old and moldy',
        'PATHS': {
            'WEST': "COSMETICS",
            'SOUTH': "TOYS",
        }
    },
    'COSMETICS': {
        'NAME': 'Cosmetics',
        'DESCRIPTION': 'All the make up looks untouched. There are bushes on the table in front of you.',
        'PATHS': {
            'EAST': "LAWN AND GARDEN",
            'WEST': "HEALTH AND BEAUTY"
        }
    },
    'HEALTH AND BEAUTY': {
        'NAME': 'Health and Beauty',
        'DESCRIPTION': 'There is a lot of lotion and your skin is dry. There are extensions for your hair lying'
                       'on the ground',
        'PATHS': {
            'EAST': "COSMETICS",
            'WEST': "PHARMACY"
        }
    },
    'SPORTING GOODS': {
        'NAME': 'Sporting Goods',
        'DESCRIPTION': 'There are multiple bats hung up on the wall. There are also some balls on the floor.',
        'PATHS': {
            'NORTH': "TOYS",
            'SOUTH': "AUTO CARE"
        }
    },
    'SHOES': {
        'NAME': 'Shoes',
        'DESCRIPTION': 'There are some very comfortable shoes called the comfortable shoes 9000.',
        'PATHS': {
            'WEST': "APPAREL"
        }
    },
    'BABY': {
        'NAME': 'Shoes',
        'DESCRIPTION': 'There is a baby in one of the cribs. There also looks to be food to the East of you.',
        'PATHS': {
            'EAST': "APPAREL",
            'SOUTH': "PETS"
        }
    },
    'PETS': {
        'NAME': 'Pets',
        'DESCRIPTION': 'You are in the pets section. There are multiple fish tanks with a lot of dead fish in it.',
        'PATHS': {
            'NORTH': "BABY",
            'WEST': "BOOKS AND MAGAZINES",
            'EAST': "PAPER AND CLEANING"
        }
    },
    'PAPER AND CLEANING': {
        'NAME': 'Paper and Cleaning',
        'DESCRIPTION': 'There is bleach on the floor and full containers on the shelves. There are also some cleaning'
                       'gloves on the floor.',
        'PATHS': {
            'NORTH': "BABY",
            'WEST': "PETS",
            'EAST': "GROCERIES"
        }
    },
    'GROCERIES': {
        'NAME': 'Groceries',
        'DESCRIPTION': 'All the food is gone and but there is a lot of water in front of you.',
        'PATHS': {
            'EAST': "PAPER AND CLEANING"
        }
    },
    'APPAREL': {
        'NAME': 'Apparel',
        'DESCRIPTION': 'There are multiple graphic tees with zombies on them.',
        'PATHS': {
            'NORTH': "JEWELERY",
            'WEST': "BABY",
            'EAST': "SHOES"
        }
    },
    'RESTROOMS': {
        'NAME': 'Restrooms',
        'DESCRIPTIONS': 'There is a toilet in front of you with a sink next to it with some soap.',
        'PATHS': {
            'SOUTH': "BOOKS AND MAGAZINES",
            'WEST': "PHOTOS"
        }
    },
    'PHOTOS': {
        'NAME': 'Photos',
        'DESCRIPTIONS': 'There are several pictures of families on the wall.',
        'PATHS': {
            'SOUTH': "ELECTRONICS",
            'EAST': "RESTROOMS"
        }
    },
    'ELECTRONICS': {
        'NAME': 'Electronics',
        'DESCRIPTIONS': 'There is an iPhone 20 X on the ground. All the tvs are gone.',
        'PATHS': {
            'NORTH': "PHOTOS",
            'SOUTH': "HOME AND OFFICE",
            'EAST': "CRAFTS"
        }
    },
    'HOME AND OFFICE': {
        'NAME': 'Home and Office',
        'DESCRIPTIONS': 'There are lamps and beds '
    }
}

current_node = walmart['PARKING LOT']
directions = ['North', 'South', 'East', 'West']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = walmart[name_of_node]
        except KeyError:
            print("You cannot go that way")
    else:
        print("Command not found.")
        print()
