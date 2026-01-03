from collections import Counter

# Card rank mapping
RANK_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 11, "Q": 12, "K": 13, "A": 14
}

# Poker hand ranks
HAND_RANKS = {
    "High Card": 1,
    "One Pair": 2,
    "Two Pair": 3,
    "Three of a Kind": 4,
    "Straight": 5,
    "Flush": 6,
    "Full House": 7,
    "Four of a Kind": 8,
    "Straight Flush": 9,
    "Royal Flush": 10
}

def score_hand(cards):
    """
    Score a 5-card poker hand.

    Returns a tuple: (hand_rank, primary_value_or_list_for_tiebreakers)
    """
    ranks = [card[:-1] for card in cards]
    suits = [card[-1] for card in cards]
    values = sorted([RANK_VALUES[r] for r in ranks], reverse=True)
    counts = Counter(values)

    is_flush = len(set(suits)) == 1
    unique = sorted(set(values), reverse=True)

    # Straight detection
    is_straight = len(unique) == 5 and unique[0] - unique[-1] == 4
    straight_high = unique[0]

    # Wheel straight (A-2-3-4-5)
    if unique == [14, 5, 4, 3, 2]:
        is_straight = True
        straight_high = 5

    # Frequency sorting: (count, value) descending
    freq = sorted(
        counts.items(),
        key=lambda x: (x[1], x[0]),
        reverse=True
    )
    ordered = [v for v, c in freq for _ in range(c)]

    # Royal Flush (strict)
    if is_flush and set(values) == {10, 11, 12, 13, 14}:
        return (HAND_RANKS["Royal Flush"],)

    # Straight Flush
    if is_flush and is_straight:
        return (HAND_RANKS["Straight Flush"], straight_high)

    # Four of a Kind
    if freq[0][1] == 4:
        return (HAND_RANKS["Four of a Kind"], ordered)

    # Full House
    if freq[0][1] == 3 and freq[1][1] == 2:
        return (HAND_RANKS["Full House"], ordered)

    # Flush
    if is_flush:
        return (HAND_RANKS["Flush"], ordered)

    # Straight
    if is_straight:
        return (HAND_RANKS["Straight"], straight_high)

    # Three of a Kind
    if freq[0][1] == 3:
        return (HAND_RANKS["Three of a Kind"], ordered)

    # Two Pair
    if freq[0][1] == 2 and freq[1][1] == 2:
        return (HAND_RANKS["Two Pair"], ordered)

    # One Pair
    if freq[0][1] == 2:
        return (HAND_RANKS["One Pair"], ordered)

    # High Card
    return (HAND_RANKS["High Card"], ordered)


def best_hands(hands):
    """
    Given a list of hands (strings like "AH 2D 3C 4S 5H"),
    returns all hands that tie for best.
    """
    parsed = [(hand, hand.split()) for hand in hands]

    # Score each hand
    scored = [(hand, score_hand(cards)) for hand, cards in parsed]

    # Find max score
    best_score = max(score for _, score in scored)

    # Return all hands with that score
    return [hand for hand, score in scored if score == best_score]

