class Person:
    
    def __init__(self, first, last):
        self._set_name(first, last)
        # print(f'{self.first} {self.last} has been initialized of class {self.__class__.__name__}.')
        
    @property
    def name(self):
        first = self._first.title()
        last = self._last.title()
        return f'{first} {last}'
    
    @name.setter
    def name(self, name):
        first, last = name
        self._set_name(first, last)
        
    @classmethod
    def _validate(cls, name):
        if not name.isalpha():
            raise TypeError('Name must be alphabetic.')
        
    def _set_name(self, first, last):
        Person._validate(first)
        Person._validate(last)
        self._first = first
        self._last = last
        
actor = Person('Mark', 'Sinclair')
print(actor.name) # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name) # Vin Diesel
try:
    actor.name = ('', 'Diesel') # ValueError: Name must be alphabetic.
except Exception as e: 
    print(e)

print()

character = Person('annIE', 'HAll')
print(character.name) # Annie Hall
try:
    character = Person('Da5id', 'Meier') # ValueError: Name must be alphabetic.
except Exception as e: 
    print(e)

print()

friend = Person('Lynn', 'Blake')
print(friend.name) # Lynn Blake
try:
    friend.name = ('Lynn', 'Blake-John') # ValueError: Name must be alphabetic.
except Exception as e: 
    print(e)
