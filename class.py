class Tree:
    def __init__(self, name):
        self.name = name 
        print(f'Object called {self.name} of the {self.__class__.__name__} class has been initialized.')
        
    def grow(self):
        print(f'{self.name} is taking in CO2 and releasing O2.')
        
class MangoTree(Tree):
    def fruit(self):
        print(f'{type(self).__name__} {self.name} has produced a Mango.')
        
class PapayaTree(Tree):
    def fruit(self):
        print(f'{type(self).__name__} {self.name} has produced a Papaya.')
        
mango = MangoTree('Mango')
papaya = PapayaTree('Papaya')

mango.fruit()
papaya.fruit()

class Foo:
    def __init__(self, name):
        self.name = name

foo = Foo('foo')

print(f'I am a {type(foo).__name__} object.')
print(f'I am a {foo.__class__.__name__} object.')

print(MangoTree('Bob').name)