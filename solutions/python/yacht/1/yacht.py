from collections import Counter

# Score categories.
# Change the values as you see fit.

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):

    counts = Counter(dice)
    total = sum(dice)

    if category == YACHT:
        return 50 if len(counts) == 1 else 0
    elif category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return category * counts[category]
    elif category == FULL_HOUSE:
        return total if sorted(counts.values()) == [2,3] else 0
    elif category == FOUR_OF_A_KIND:
        for value, count in counts.items():
            if count >= 4:
                return value * 4
        return 0
    elif category == LITTLE_STRAIGHT:
        return 30 if sorted(counts.keys()) == [1,2,3,4,5] else 0
    elif category == BIG_STRAIGHT:
        return 30 if sorted(counts.keys()) == [2, 3, 4, 5, 6] else 0
    elif category == CHOICE:
        return total



