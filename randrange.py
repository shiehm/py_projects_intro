import random

highest = int(input('Enter integer: '))
number = 0

while number != highest:
    number = random.randrange(highest + 1)
    print(number)
    
# Solution:

while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break