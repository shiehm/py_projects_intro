first_name = input('What is your first name?\n')
last_name = input('What is your last name?\n')

print(f'My name is {first_name} {last_name}.')

current_age = int(input('How old are you?\n'))

print(f'I am {current_age} years old.')

increment = int(10)
time_elapsed = 0
future_age = 0

while future_age < 70:
    time_elapsed += increment
    future_age = current_age + time_elapsed
    print(f'In {time_elapsed} years you will be {future_age} years old.')