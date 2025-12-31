from enum import Enum, auto 

class Bottles(Enum):
    One = auto()
    Two = auto()
    Three = auto()
    Four = auto()
    Five = auto()
    Six = auto()
    Seven = auto()
    Eight = auto()
    Nine = auto()
    Ten = auto()

START = "green bottles hanging on the wall,"
MIDDLE = "And if one green bottle should accidentally fall,"
END_START = "There'll be"
END_END = "green bottles hanging on the wall."

END_ONE = "green bottle hanging on the wall."
START_ONE = "green bottle hanging on the wall,"

def recite(start, take=1):
    result = []
    bottles = Bottles(start) # will throw valueError if start is not in range(1, 11)
    for verse_number in range(take):
        bottle_num = bottles.value - verse_number
        bottle_name = Bottles(bottle_num).name
        if bottle_num >= 2:
            verse = [" ".join([bottle_name, START])] * 2
            verse.append(MIDDLE)
            # get the name for the bottles one less than bottle_num
            new_name = Bottles(bottle_num-1).name
            if bottle_num - 1 >= 2:
                verse.append(" ".join([END_START, new_name.lower(), END_END]))
            else:
                verse.append(" ".join([END_START, new_name.lower(), END_ONE]))
        else: 
            verse = [" ".join([Bottles(1).name, START_ONE])] * 2
            verse.append(MIDDLE)
            verse.append(" ".join([END_START, "no", END_END]))
        if result:
            result.append("")
            result.extend(verse)
        else:
            result.extend(verse)
    return result

