class Dev:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name:
            self._name = name
        else:
            raise Exception("name should be a string")

    def freebies(self):
        from .__init__ import Freebie
        return[freebie for freebie in Freebie.all if freebie.dev == self]

    def companies(self):
        return list({freebie.company for freebie in self.freebies()})
    