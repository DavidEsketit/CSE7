walmart = {
    'PARKING LOT': {
        'NAME': 'Parking Lot',
        'DESCRIPTION': 'You are in a parking lot, there are no cars and there is an open door in the south to Walmart',
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
            'NORTH': "PHARMACY",
            'SOUTH': "APPAREL"
        }
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
