class Luhn(object):
    def __init__(self, card_num):
        self_cleaned = card_num.replace(" ", "")
        self_doubled = [2*int(x) for ind, x in enumerate(self_cleaned) if (ind%2)==0]

    def valid(self):
        pass
