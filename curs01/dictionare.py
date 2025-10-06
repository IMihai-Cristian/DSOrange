""" sunt colectii de obiecte mutabile si ordonate(indexabile)"""
# var_dict = {}
# var_dict_2 = dict()

# var_dictionar = {'cheie_1': 'valoare_1', 'cheie_2': 'valoare_2'} # cheile trebuie sa fie mereu imutabile. cheile nu pot fi duplicate
# var_ex = {(1, 2): 'aaaaa'}
# print(var_ex)

""" len ca la restul"""
"""indexare"""
# print(var_dictionar['cheie_2'])

""" dictionare intretesute """
# ex_dict = {'key_1': {'key_2': {'key_3': ['a', 1.1, [333, (23, )]]}, 'key_4': 10}, 'key_5': 'key_6'}
# print(ex_dict['key_1']['key_2']['key_3'][2][1][0])

"""alocare elemente noi"""
ex_dict = {'key_1': 1, 'key_2': 'abc', 'key_3': 10}
# ex_dict['key_2'] = 3
# print(ex_dict)

"""metode"""
# clear goleste dictionarul
# print(ex_dict['key_3'])
# get
# print(ex_dict.get('key_3', ''))

# items() # returneaza lista de tupluri (cheie, valoare)
print(ex_dict.items())

# keys() # returneaza lista de chei
# print(ex_dict.keys())

# values() # returneaza lista de valori
# print(ex_dict.values())

# ex_dict = {'key_1': 1, 'key_2': 'abc', 'key_3': 10}
# pop()
# print(ex_dict.pop('key_2'))
# var_ex = ex_dict.pop('key_2')
# print(var_ex)
# print(ex_dict)

# popitem()
# print(ex_dict.popitem())
# print(ex_dict)

# update()
# dict_2 = {'key_1': 5, 20: 10}
# ex_dict.update(dict_2)
# print(ex_dict)