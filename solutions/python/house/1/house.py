VERSE_START = "This is the"

VERSE_END = "house that Jack built."

THAT = "that"

THE = "the"

CHARACTERS_ACTIONS = {
    "malt": "lay in",
    "rat": "ate",
    "cat": "killed",
    "dog": "worried",
    "cow": "tossed",
    "maiden": "milked",
    "man": "kissed",
    "priest": "married",
    "rooster": "woke",
    "farmer": "kept",
    "horse": "belonged to"
}

CHARACTERS_FEATURES = {
    "cow": "with the crumpled horn",
    "maiden": "all forlorn",
    "man": "all tattered and torn",
    "priest": "all shaven and shorn",
    "rooster": "that crowed in the morn",
    "farmer": "sowing his corn",
    "horse": "and the hound and the horn"
}

def get_verse(verse_number):
    if verse_number == 1:
        return " ".join([VERSE_START, VERSE_END])
    else:
        verse = ""
        # get the characters
        characters = list(CHARACTERS_ACTIONS.keys())
        for ii in range(verse_number - 1):
            if CHARACTERS_FEATURES.get(characters[ii], "") == "":
                verse = " ".join([characters[ii], THAT, CHARACTERS_ACTIONS[characters[ii]], THE, verse])
            else:
                verse = " ".join([characters[ii], CHARACTERS_FEATURES.get(characters[ii], ""), THAT, CHARACTERS_ACTIONS[characters[ii]], THE, verse])
        verse = VERSE_START + " "  + verse + VERSE_END
        return verse    

            
def recite(start_verse, end_verse):
    result = []
    for ii in range(start_verse, end_verse + 1):
        result.append(get_verse(ii))
    return result
