# Implement a class to hold room information. This should have name and
# description attributes.

class Room: # room class.
    def __init__ (self, name, description, items=None, n_to=None, s_to=None, e_to=None, w_to=None): # inint method with attributes
        self.name = name
        self.description = description # attribute
        self.items = items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __str__ (self): #str method to use print statement.
        output = (
            f'{self.name}, Welcome to the {self.description}, there is a {self.items} on the ground in front of you.' # description output
            )
        return (output)

if __name__ == "__main__":
    room = Room('Charles', 'Outside Cave Entrance, North of you, the cave mount beckons', 'dirty satchel')
    print(room)
