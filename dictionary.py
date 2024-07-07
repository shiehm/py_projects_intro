pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

def print_special(dic, key):
    if key in dic.keys():
        print(dic[key])
    else:
        print(None)
        print('<silence>')
        
print_special(pets, 'Cat')
print_special(pets, 'Dog')
print_special(pets, 'Bird')
print_special(pets, 'Lizard')

print(pets.get('Cat'))
print(pets.get('Lizard'))
print(pets.get('Lizard', '<silence>'))