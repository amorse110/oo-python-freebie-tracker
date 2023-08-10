class Company:
    all = [] #need to collect all to find one specific

    def __init__(self, name, year):
        self.name = name
        self.year = year
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("name should be a string")
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        if isinstance(year, int):
            self._year = year
        else:
            raise Exception("year should be an integer")
        
    def freebies(self):
        from .__init__ import Freebie
        return[freebie for freebie in Freebie.all if freebie.company == self]
    
    def devs(self):
        return list({freebie.dev for freebie in self.freebies()})

    def give_freebie(self, dev, item_name, value):
        from .__init__ import Freebie
        return Freebie(dev, self, item_name, value)
    
    @classmethod
    def oldest_company(cls):
        return min(Company.all, key = lambda company: company.year)