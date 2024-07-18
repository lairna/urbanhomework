my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print('Dict:', my_dict)
print('Existing value:', my_dict['Vasya'])
print('None existing value:', my_dict.get('Kamila'))
my_dict.update({'Kamila': 1981, 'Artem': 1915})
a = my_dict.pop('Egor')
print('Delited value:', a)
print('Modified Dict:', my_dict)
my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко'}
print('Set:', my_set)
my_set.update(((5, 6, 1.6), 13))
my_set.discard(1)
print('Modified Set', my_set)
