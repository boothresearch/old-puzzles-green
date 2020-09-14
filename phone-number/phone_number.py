class Phone(object):
    def __init__(self, phone_number):
        self.raw = phone_number

    def clean(self):
        self.cleaned = [s for s in self.raw if s.isdigit()]
        if len(self.cleaned) > 10:
            self.cleaned = self.cleaned[1:]
        return "".join(self.cleaned)
