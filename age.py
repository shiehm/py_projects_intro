age = int(input('How old are you? '))

print(f'You are now {age} years old.')

def aging(age, increment):
    print(f'In {increment} years you will be {age + increment}.')
    print(f'In {increment * 2} years you will be {age + increment * 2}.')
    print(f'In {increment * 3} years you will be {age + increment * 3}.')
    print(f'In {increment * 4} years you will be {age + increment * 4}.')
    
aging(age, 10)

print()

for i in range(10, 41, 10):
    print(f'in {i} years you will be {age + i} years old.')