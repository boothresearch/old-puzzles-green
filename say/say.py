def say(number):
    import inflect
    p = inflect.engine()
    return p.number_to_words(number)
