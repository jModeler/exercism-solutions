START_PHRASE = "On the "
END_PHRASE = " day of Christmas my true love gave to me:"

DAY_COUNT = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
}

GIFTS = [
    "a Partridge in a Pear Tree",
    "Turtle Doves",
    "French Hens",
    "Calling Birds",
    "Gold Rings",
    "Geese-a-Laying",
    "Swans-a-Swimming",
    "Maids-a-Milking",
    "Ladies Dancing",
    "Lords-a-Leaping",
    "Pipers Piping",
    "Drummers Drumming"
]

GIFT_COUNT = {
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve"
}

def compose_gift_list(verse_number):
    ii = verse_number
    gift_list = ""
    while ii > 0:
        if ii == 1:
            gift_list = "".join([gift_list, " and ", GIFTS[ii-1], "."])
        else:
            gift_list = "".join([gift_list, " ", GIFT_COUNT[ii], " ", GIFTS[ii-1], ","])
        ii -= 1
    return gift_list

def recite(start_verse, end_verse):
    result = []
    for ii in range(start_verse, end_verse+1):
        verse = "".join([START_PHRASE, DAY_COUNT[ii], END_PHRASE])
        if ii == 1:
            verse = " ".join([verse, GIFTS[ii-1]])
            verse = verse + "."
        else:
            verse = "".join([verse, compose_gift_list(ii)])
        result.append(verse)
    return result
    

