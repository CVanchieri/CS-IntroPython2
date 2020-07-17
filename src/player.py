# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: # player class
    def __init__ (self, name, location, items=None): # init method with attribute
        self.name = name
        self.location = location # player attribute
        self.items = items
    def __str__ (self): #str method to use print statement.
        output = (
            f'You are in the {self.location} room, and are holding a {self.items}'
            )
        return (output)

if __name__ == "__main__":
    player = Player(name='Charles', location='outside', items='dirty apple')
    print(player)
