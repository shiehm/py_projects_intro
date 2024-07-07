my_list = [6, 3, 0, 11, 20, 4, 17]

i = 0
while i < len(my_list):
    if my_list[i] % 2 == 0:
        print(my_list[i])
    i += 1
    
print()

for i in my_list:
    if i % 2 != 0:
        print(i)
        
nested_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

print()

for inner_list in nested_list:
    for i in inner_list:
        if i % 2 ==0:
            print(i)
            
even_list = [i 
    for inner_list in nested_list
    for i in inner_list
    if i % 2 == 0
]

print(even_list)

new_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

even_or_odd = ['even' if i % 2 == 0 else 'odd' for i in new_list]

print(even_or_odd)

for num, val in zip(new_list, even_or_odd):
    print(f'{num} is {val}')

print()

def even_or_odd_func(num):
    return 'even' if i % 2 == 0 else 'odd'

even_or_odd_list = list()

# even_or_odd_list_1 = [even_or_odd_func(num) for num in new_list] ## ???

for i in new_list:
    value = even_or_odd_func(i)
    even_or_odd_list.append(value)
    
print(even_or_odd_list)
# print(even_or_odd_list_1)