# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction 
        self.coordinates = (x_pos, y_pos)
    
    def change_direction(self, direction):
        if direction == "R":
            if self.direction < 3:
                self.direction += 1
            else:
                self.direction = 0
        else:
            if self.direction > 0:
                self.direction -= 1
            else: 
                self.direction = 3
    
    def advance(self):
        coordinates = list(self.coordinates)
        if self.direction == NORTH:
            coordinates[1] += 1
        elif self.direction == SOUTH:
            coordinates[1] -= 1
        elif self.direction == EAST:
            coordinates[0] += 1
        else:
            # west
            coordinates[0] -= 1
        self.coordinates = tuple(coordinates)

    def move(self, instructions):
        for ii in instructions:
            if ii in ["R", "L"]:
                self.change_direction(ii)
            if ii == "A":
                self.advance()