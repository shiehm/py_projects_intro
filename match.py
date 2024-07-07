# Write a function that takes a single integer argument and prints a message that describes whether:

# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0

def sorter(value):
    if value in (range(51)):
        print(f'the value {value} is between 0 and 50 (inclusive)')
    elif value in (range(51, 101)):
        print(f'the value {value} is between 51 and 100 (inclusive)')
    elif value > 100:
        print(f'the value {value} is greater than 100')
    elif value < 0:
        print(f'the value {value} is less than 0')
    else:
        print('Nothing')
       
num = float(input('Enter Number: '))
sorter(num)     python