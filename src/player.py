# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: # player class
    def __init__ (self, location): # init method with attribute
        self.location = location # player attribute
    def __str__ (self): #str method to use print statement.
        output = (
            f'You are in the {self.location} room.'
            )
        return (output)

if __name__ == "__main__":
    player = Player(location='foyer')
    print(player)
