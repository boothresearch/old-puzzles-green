# Needs to install inflect pacakge
# pip3 install inflect

def say(number):
    if number >=0 and number < 1000000000000:
        import inflect
        p = inflect.engine()
        result = p.number_to_words(number).replace(",", "")
        return result
    else:
        raise ValueError("Number not in the range")
