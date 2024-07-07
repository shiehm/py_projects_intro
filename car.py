class Car:
    
    engine = 0
    speed = 0
    # distance = 5
    # fuel_used = 0
    
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        print(f'Object of {type(self).__name__} has been initialized.')
        print(f'New car is a {self.color} {self.year} {self.model}.')
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError('Model must be a string.')
        self._model = model
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError('Year must be an integer.')
        self._year = year
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('Color must be a string.')
        self._color = color
    
    def start_engine(self):
        self.engine = 1
        print('Engine is on.')
        
    def accelerate(self):
        if self.engine != 1:
            raise ValueError('Engine is not on.')
        self.speed += 1
        # self.distance += 1
        # self.fuel_used += 1
        print(f'Speed is now {self.speed}.')
        
    def brake(self):
        if self.engine != 1:
            raise ValueError('Engine is not on.')
        self.speed -= 1
        print(f'Speed is now {self.speed}.')
        
    def stop_engine(self):
        self.engine = 0
        print('Engine is off.')
        
    def check_speed(self):
        print(f'Speed is now {self.speed}.')
        
    def spray_paint(self, color):
        print(f'Spray painting the {self.year} {self.model} to {color}.')
        self.color = color
        print(f'The {self.year} {self.model} is now {color}')
    
    # def gas_mileage(self):
    #     return (self.fuel_used / self.distance)
    
    # @classmethod
    # def gas_mpg(cls, gal, miles):
    #     return (miles/gal)
        
    @staticmethod
    def gas_mpg(gal, miles):
        return (miles/gal)
        
car = Car('Toyota', 1996, 'White')

car.check_speed()
car.start_engine()
car.accelerate()
car.brake()
car.stop_engine()
car.check_speed()

print(car.color)
print(car.year)
print(car.model)

print()

car.color = 'Black'
car.model = 'Honda'
car.year = int(1997)

print(car.color)
print(car.year)
print(car.model)

print()

car.start_engine()

while car.speed < 10:
    car.accelerate()
    
car.check_speed()

car2 = Car('Ford', 1911, 'Black')
car2.check_speed()

car.check_speed()

car2.spray_paint('Purple')

# print(f'{car.color} {car.year} {car.model} has {car.gas_mileage()} mpg.')
# print(f'{car2.color} {car2.year} {car2.model} has {car2.gas_mileage()} mpg.')

print(f'{car.color} {car.year} {car.model} has {car.gas_mpg(12, 300)} mpg.')
print(f'{car2.color} {car2.year} {car2.model} has {car2.gas_mpg(11, 420)} mpg.')