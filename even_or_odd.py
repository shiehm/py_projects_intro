def even_or_odd(num):
    if num % 2 == 0:
        print('Even')
    else:
        print('Odd')
        
num = int(input('Enter integer: '))

even_or_odd(num)
print('Ternary: Even' if num % 2 == 0 else 'Ternary: Odd')