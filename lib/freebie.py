class Freebie:
    all = []

    def __init__(self, dev, company, item_name, value):
        self.dev = dev
        self.company = company
        self.item_name = item_name
        self.value = value
        type(self).all.append(self)
    
    def __repr__(self):
        return(f"{self.item_name} for {self.value} at {self.company.name} for {self.dev.name}")

    @property
    def dev(self):
        return self._dev
    
    @dev.setter
    def dev(self, dev):
        if isinstance(dev, Dev):
            self._dev = dev
        else:
            raise Exception("dev should be a Dev object")
    
    @property
    def company(self):
        return self._company
    
    @company.setter
    def company(self, company):
        if isinstance(company, Company):
            self._company = company
        else:
            raise Exception("company should be a Company object")
    
    @property
    def item_name(self):
        return self._item_name
    
    @item_name.setter
    def item_name(self, item_name):
        if isinstance(item_name, str):
            self._item_name = item_name
        else:
            raise Exception("item_name should be a string")
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, int):
            self._value = value
        else:
            raise Exception("value should be a integer")
        
    def print_details(self):
        return (f"{self.dev.name} owns a {self.item_name} from {self.company.name}")
        
    
from .__init__ import Dev
from .__init__ import Company