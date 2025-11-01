rule_one_string = "ay"
rule_three_string = "qu"
vowels = ['a', 'e', 'i', 'o', 'u']
special_characters = ['xr', 'yt']

def is_vowel(character):
    return character.lower() in vowels

def is_special(characters):
    return "".join(characters) in special_characters

def rule_one(word):
    return "".join([word, rule_one_string])

def other_rules(word):
    result = ""
    remaining = word
    for ii in range(len(word)):
        character = word[ii]
        if is_vowel(character):
            result = "".join([remaining, result])
            return rule_one(result)
        elif character == 'q' and word[ii+1] == 'u':
            remaining = word[(ii+2):]
            result = "".join([remaining, result, rule_three_string])
            return rule_one(result)
        elif character == 'y' and ii != 0:
            remaining = word[ii:]
            result = "".join([remaining, result])
            return rule_one(result)
        else:
            result = "".join([result, character])
            remaining = word[(ii+1):]


def translate(text):
    result = []
    str_list = text.split(" ")
    for word in str_list:
        if is_vowel(word[0]) or is_special([word[0], word[1]]):
            result.append(rule_one(word))
        else:
            result.append(other_rules(word))
    return " ".join(result)
