word_map = {
    'WESTHOUSE': {
        'NAME': 'WEST OF HOUSE',
        'DESCRIPTION': 'You are west of a small house',
        'PATHS': {
            'NORTH': "NORTHHOUSE",
            'SOUTH': "SOUTH HOUSE"
        }
    },
    'SOUTHHOUSE': {
        'NAME': 'SOUTH OF HOUSE',
        'DESCRIPTION': 'Insert description here.',
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    }
}

current_node = word_map['WESTHOUSE']
print(current_node["NAME"])
print(current_node["DESCRIPTION"])
