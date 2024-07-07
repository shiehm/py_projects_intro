my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

keys = list(my_set)
values = [len(key) for key in keys]

my_dict = {key:value for (key, value) in zip(keys, values) if value % 2 != 0}
print(my_dict)

# A more elegant solution, don't need to create lists
new_dict = {name: len(name) for name in my_set if len(name) % 2 != 0}
print(new_dict)