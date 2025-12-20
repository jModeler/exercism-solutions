from string import ascii_uppercase
from string import digits
from random import randrange

class Robot:
    name_archive = []
    def __init__(self):
        self.reset()
        type(self).name_archive.append(self.name)
    
    def gen_name(self):
        alpha_part = "".join([ascii_uppercase[randrange(len(ascii_uppercase))] for _ in range(2)])
        num_part = "".join([digits[randrange(len(digits))] for _ in range(3)])
        self.name = "".join([alpha_part, num_part])   
    
    def reset(self):
        self.gen_name()
        while(self.name in type(self).name_archive):
            self.gen_name()