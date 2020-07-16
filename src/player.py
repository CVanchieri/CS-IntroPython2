# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: # player class
    def __init__ (self, name, location): # init method with attribute
        self.name = name
        self.location = location # player attribute
    def __str__ (self): #str method to use print statement.
        output = (
            f'You are in the {self.location} room.'
            )
        return (output)

if __name__ == "__main__":
    player = Player(name='Charles', location='outside')
    print(player)
