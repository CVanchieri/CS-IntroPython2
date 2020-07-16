import sys
from room import Room
from player import Player

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
program = 0
commands = ['n', 's', 'e', 'w', 'q']
command = commands
player_1 = Player(name='Charles', location=room['outside'])
print (f'{player_1.name} you are at the {player_1.location.name}, {player_1.location.description}.')

while program == 0:
    input_entry = input(
    """Where do you want to go?
    (enter a command) [n'north', s'south', e'east', w'west', q'quit'] = """
    )
    if input_entry == 'n':
        if player_1.location.n_to is None:
            print("You can't go that way, try again.")
        else:
            player_1.location = player_1.location.n_to
            print(f'Your on the move now, you are at the {player_1.location.name}, {player_1.location.description}?')
    elif input_entry == 'e':
        if player_1.location.e_to is None:
            print("You can't go that way, try again.")
        else:
            player_1.location = player_1.location.e_to
            print(f'Your on the move now, you are at the {player_1.location.name}, {player_1.location.description}')
    elif input_entry == 's':
        if player_1.location.s_to is None:
            print("You can't go that way, try again.")
        else:
            player_1.location = player_1.location.s_to
            print(f'Your on the move now, you are at the {player_1.location.name}, {player_1.location.description}')
    elif input_entry == 'w':
        if player_1.location.w_to is None:
            print("You can't go that way, try again.")
        else:
            player_1.location = player_1.location.w_to
            print(f'Your on the move now, you are at the {player_1.location.name}, {player_1.location.description}')
    elif input_entry == 'q':
            print("Thank you for playing the game, goodbye!")
            exit()
    elif input_entry != commands:
            print("Please use one of these commands [n'north', s'south', e'east', w'west', q'quit'].")

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
