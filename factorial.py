def factorial(n):
    total = 1
    for i in range(n, 0, -1):
        print(f'{i} * {total}')
        total *= i
    print(f'{n}! = {total}')
    return total
    
num = int(input('Enter an integer: '))
factorial(num)