def double(number):
    doubled = 2*number
    if doubled > 9:
        return doubled - 9
    else:
        return doubled

class Luhn(object):
    def __init__(self, card_num):
        # Reverse the list and remove whitespaces
        self.cleaned = list(reversed([int(s) for s in card_num if s.isdigit()]))

        # Double
        self.doubled = [double(num) for ind, num in enumerate(self.cleaned) if (ind%2)==0]

    def valid(self):
        # Check if the sum if divisible by 10
        if sum(self.doubled) % 10 == 0:
            print("Valid")
        else:
            print("Invalid")
