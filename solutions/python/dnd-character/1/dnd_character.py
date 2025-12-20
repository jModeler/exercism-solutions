from random import randrange
from math import floor 

NUM_ATTRS = 6
NUM_ROLLS = 4
ATTRS = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'hitpoints']


class Character:
    def __init__(self):
        for name in ATTRS:
            setattr(self, name, 0)
        self.assign_scores()

    def assign_scores(self):
        for ii in range(NUM_ATTRS):
            dice_rolls = [randrange(1, 7) for _ in range(NUM_ROLLS)]
            setattr(self, ATTRS[ii], self.compute_score(dice_rolls))
        self.hitpoints = modifier(self.constitution) + 10

    def compute_score(self, rolls):
        min_roll = min(rolls)
        index = rolls.index(min_roll)
        rolls.pop(index)
        return sum(rolls)
    
    def ability(self):
        # pick an ability at random
        index = randrange(6)
        ability = ATTRS[index]
        return getattr(self, ability)

def modifier(value):
    result = value - 10
    result /= 2
    return floor(result)

