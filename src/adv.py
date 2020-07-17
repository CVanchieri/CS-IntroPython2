import sys
from room import Room
from player import Player

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     """to the North its as if you can hear the mountains calling your name.
You take a look around at the surroundings, you see something interesting on the ground.
Do you want to pick it up?""", "dirty satchel"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east, there is a strange smell in the air."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! The tales were correct, you see the most beautiful gems in front of you,
if you have something to put them in you can pick up the gems. The only exit is to the south."""),
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

# Main
program = 0
commands = ['n', 's', 'e', 'w', 'q', 'pick up', 'drop']
command = commands
# Make a new player object that is currently in the 'outside' room.
player_1 = Player(name='Charles', location=room['outside'])
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
print (f'{player_1.name} you are at the {player_1.location.name}, {player_1.location.description}.')

# Write a loop that:
while program == 0:
# * Waits for user input and decides what to do.
    input_entry = input("""What would you like to do next? \n"""
    """(enter a command) [n' head north', s'head south', e'head east', w'head west', p'pick up', d'drop', q'leave the game'] = """
    )
# If the user enters a cardinal direction, attempt to move to the room there.
    if input_entry == 'n':
        if player_1.location.n_to is None:
            print("You can't go that way, try again.")
        else:
            player_1.location = player_1.location.n_to
            print(f'You are now at the {player_1.location.name}, {player_1.location.description}?')
    elif input_entry == 'e':
        if player_1.location.e_to is None:
            print("You can't go that way, try again.")
        else:
            player_1.location = player_1.location.e_to
            print(f'You are now at the {player_1.location.name}, {player_1.location.description}')
    elif input_entry == 's':
        if player_1.location.s_to is None:
            print("You can't go that way, try again.")
        else:
            player_1.location = player_1.location.s_to
            print(f'You are now at the {player_1.location.name}, {player_1.location.description}')
    elif input_entry == 'w':
        if player_1.location.w_to is None:
            print("You can't go that way, try again.")
        else:
            player_1.location = player_1.location.w_to
            print(f'You are now at the {player_1.location.name}, {player_1.location.description}')


    elif input_entry == 'p':
        if player_1.location.name is "Outside Cave Entrance":
            player_1.items = ['dirty satchel']
            print("you pick up the dirty satchel and throw it over your shoulder, surprisingly its a great fit.")
        elif input_entry == 'p':
            if (player_1.location.name is "Treasure Chamber") & (player_1.items is not None):
                print("You pick up the shiny gems and place them in your dirty satchel.")
            elif input_entry == 'p':
                if (player_1.location.name is "Treasure Chamber") & (player_1.items is None):
                    print("Hmm seems you need something to place them in, have you seen anything along the way?")
                elif input_entry == 'p':
                    if (player_1.items is None):
                        print("You reach for the floor and pick up some old dust, there is nothing here.")


    elif input_entry == 'd':
        if player_1.items is not None:
            print("You drop it on the ground, dust rises as it hits the floor and disintegrates.")
        else:
            print("You have nothing to drop., if you notice something maybe you can pick it up.")
# Print an error message if the movement isn't allowed.
    elif input_entry != commands:
            print("Please use one of these commands [n'north', s'south', e'east', w'west', q'quit'].")
# If the user enters "q", quit the game.
    if input_entry == 'q':
        print("Thank you for playing the game, goodbye!")
        exit()
