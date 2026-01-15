from itertools import combinations 

def get_plus_index(s):
    return [i for i, ch in enumerate(s) if ch == '+']

def is_horizontal(strings, row, c1, c2):
    return all(strings[row][c] in '-+' for c in range(c1 + 1, c2))

def is_vertical(strings, col, r1, r2):
    return all(strings[r][col] in '|+' for r in range(r1 + 1, r2))

def rectangles(strings):
    rectangles_count = 0
    plus_indexes = list(map(get_plus_index, strings))

    for r1, r2 in combinations(range(len(strings)), 2):
        common_cols = set(plus_indexes[r1]) & set(plus_indexes[r2])

        for c1, c2 in combinations(sorted(common_cols), 2):
            if (
                is_horizontal(strings, r1, c1, c2) and
                is_horizontal(strings, r2, c1, c2) and
                is_vertical(strings, c1, r1, r2) and
                is_vertical(strings, c2, r1, r2)
            ):
                rectangles_count += 1

    return rectangles_count