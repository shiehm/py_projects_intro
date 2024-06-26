interest = float(0.05)
starting_balance = 1000
years = 5

def compound(starting_balance, years, interest):
    balance = starting_balance * (1 + interest)**years
    return balance

balance = compound(starting_balance, years, interest)

print(f'In {years} years, you will have ${balance:,.2f} dollars.')

def callback_compound(starting_balance, years, interest):
    print(f'1st Year: ${compound(starting_balance, 1, interest):,.2f}')
    print(f'2nd Year: ${compound(starting_balance, 2, interest):,.2f}')
    print(f'3rd Year: ${compound(starting_balance, 3, interest):,.2f}')
    print(f'4th Year: ${compound(starting_balance, 4, interest):,.2f}')
    print(f'5th Year: ${compound(starting_balance, 5, interest):,.2f}')

def augmented_compound(starting_balance, years, interest):
    count = 0
    balance = starting_balance
    while count < 5:
        balance *= (1+interest)
        count += 1
        print(f'In year {count} you have ${balance:.2f}.')
    return balance

augmented_compound(starting_balance, years, interest)