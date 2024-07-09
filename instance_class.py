class Tree:
    def __init__(self, name):
        self.name = name 
        print(f'Object called {self.name} of the {self.__class__.__name__} class has been initialized.')
        
    def grow(self):
        print(f'{self.name} is taking in CO2 and releasing O2.')
        
class MangoTree(Tree):
    
    count = 0
    
    def __init__(self, name):
        super().__init__(name)
        # self.count += 1
        MangoTree.count += 1 #This increments the class variable vs. an instance variable
    
    def counter(self):
        return MangoTree.count
    
    def fruit(self):
        print(f'{type(self).__name__} {self.name} has produced a Mango.')
        
class PapayaTree(Tree):
    def fruit(self):
        print(f'{type(self).__name__} {self.name} has produced a Papaya.')
        
mango1 = MangoTree('mango1')
mango2 = MangoTree('mango2')
mango3 = MangoTree('mango3')

print(mango1.counter())