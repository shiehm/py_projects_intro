# Return a list of all integers from my_tuple

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(collection):
    integers = []
    for i in collection:
        if type(i) is int:
            integers.append(i)
    return integers

integers = find_integers(my_tuple)
print(integers)                 

def find_integers2(collection):
    return [value for value in collection if type(value) is int]

integers2 = find_integers2(my_tuple)
print(integers2)                 
