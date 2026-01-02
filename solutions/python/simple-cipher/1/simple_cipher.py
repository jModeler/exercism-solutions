from string import ascii_lowercase
from secrets import choice

SHIFT_KEY = dict(zip(ascii_lowercase, range(26)))
DEFAULT_KEY_LENGTH = 100

class Cipher:
    def __init__(self, key=None):
        if key:
            self.key = key 
        else:
            self.key = "".join(choice(ascii_lowercase) for _ in range(DEFAULT_KEY_LENGTH))
        self.key_length = len(self.key)
        self.chars_length = len(ascii_lowercase)

    @staticmethod
    def shift_operation(ch, shift, chars_length, encode=True):
        ind = ascii_lowercase.index(ch)
        if encode:
            if (ind + shift) >= chars_length:
                new_ind = (ind + shift) % chars_length
            else:
                new_ind = ind + shift
        else:
            if shift > ind:
                new_ind = ind + chars_length - shift
            else:
                new_ind = ind - shift
        return ascii_lowercase[new_ind]

    def encode(self, text):
        key_index = 0
        result = ""
        for ch in text:
            shift = SHIFT_KEY[self.key[key_index]]
            ech = Cipher.shift_operation(ch, shift, self.chars_length)
            result = "".join([result, ech])
            key_index += 1
            if key_index == self.key_length:
                key_index = 0
        return result 
    
    def decode(self, text):
        key_index = 0
        result = ""
        for ch in text:
            shift = SHIFT_KEY[self.key[key_index]]
            dch = Cipher.shift_operation(ch, shift, self.chars_length, encode=False)
            result = "".join([result, dch])
            key_index += 1
            if key_index == self.key_length:
                key_index = 0
        return result