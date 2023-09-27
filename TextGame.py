rooms = {
    'Start Point': {'North': 'Pillar of Pride', 'South': 'Hall of Gluttony', 'West': 'Secret Passage of Sloth', 'East': 'Library of Lust', 'item': 'no item'},
    'Pillar of Pride': {'East': 'Galley of Greed', 'West': 'Embodiment of Sins', 'South': 'Starting Point', 'item': 'gauntlet'},
    'Secret Passage of Sloth': {'North': 'Embodiment of Sins', 'South': 'Warehouse of Wrath', 'East': 'Start Point', 'item': 'ring'},
    'Hall of Gluttony': {'North': 'Start Point', 'West': 'Warehouse of Wrath', 'East': 'Chamber of Envy', 'item': 'cloak'},
    'Library of Lust': {'North': 'Galley of Greed', 'South': 'Chamber of Envy', 'West': 'Start Point', 'item': 'eyes'},
    'Galley of Greed': {'South': 'Library of Lust', 'West': 'Pillar of Pride', 'item': 'potion'},
    'Chamber of Envy': {'West': 'Hall of Gluttony', 'North': 'Library of Lust', 'item': 'armor'},
    'Warehouse of Wrath': {'North': 'Secret Passage of Sloth', 'East': 'Hall of Gluttony', 'item': 'sword'}
}
def player_location():
    print('You are in the {}' .format(current_room))
    if rooms[current_room]['item'] not in inventory:
        print('You see a {}' .format(rooms[current_room]['item']))
    else:
        print('You have the item in this room already.')
    print('Inventory', inventory)
    print()
current_room = 'Start Point'
inventory = []
move = ''
while current_room != 'Embodiment of Sins':
    player_location()
    move = input('Enter a move.')
    if move == 'get':
        item = input('Pick your item.')
        if item in rooms[current_room]['item']:
            if item not in inventory:
                inventory.append(item)
            else:
                print('You already have that item.')
        else:
            print('That item is not in the room.')
    elif move in rooms[current_room]:
        current_room = rooms[current_room][move]
    else:
        print('Invalid input')
if len(inventory) != 7:
    print('You have reached the Embodiment of Sins, but dont have all the items. You lose')
else:
    print('You have defeated the Embodiment of Sins. You win')




