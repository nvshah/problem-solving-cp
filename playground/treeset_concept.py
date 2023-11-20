import bisect as bi 

class TreeSet: 
    def __init__(self, iterable):
        self.s = set(iterable)
        self.b = sorted(self.s)

    def add(self, e):
        self.s.add(e)
        bi.insort(self.b, e)