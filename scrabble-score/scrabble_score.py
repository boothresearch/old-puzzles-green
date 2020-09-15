def score_sub(letter):
    letter_temp = letter.lower()
    if letter_temp in ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]:
        value = 1
    elif letter_temp in ["d", "g"]:
        value = 2
    elif letter_temp in ["b", "c", "m", "p"]:
        value = 3
    elif letter_temp in ["f", "h", "v", "w", "y"]:
        value = 4
    elif letter_temp in ["k"]:
        value = 5
    elif letter_temp in ["j", "x"]:
        value = 8
    elif letter_temp in ["q", "z"]:
        value = 10
    else:
        value = 0

    return value


def score(word):
    letter_list = list(word)
    n = len(word)
    tot_value_temp = 0
    for x in range(0,n):
        tot_value_temp = tot_value_temp + score_sub(letter_list[x])
    print("Total value for ", word, " is ", str(tot_value_temp))
    return tot_value_temp

print(score("cabbage"))
print(score("CABBAGE"))