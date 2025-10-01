""" sunt colectii de obiecte mutabile si ordonate(indexabile)"""
# var_dict = {}
# var_dict_2 = dict()

# var_dictionar = {'cheie_1': 'valoare_1', 'cheie_2': 'valoare_2'} # cheile trebuie sa fie mereu imutabile
# var_ex = {(1, 2): 'aaaaa'}
# print(var_ex)

""" len ca la restul"""
"""indexare"""
# print(var_dictionar['cheie_2'])

""" dictionare intretesute """
# ex_dict = {'key_1': {'key_2': {'key_3': ['a', 1.1, [333, (23, )]]}, 'key_4': 10}, 'key_5': 'key_6'}
# print(ex_dict['key_1']['key_2']['key_3'][2][1][0])

"""alocare elemente noi"""
ex_dict = {'key_1': 1, 'key_2': 'abc'}
# ex_dict['key_2'] = 3
# print(ex_dict)

"""metode"""
# clear goleste dictionarul
# print(ex_dict['abc'])
# get
print(ex_dict.get('key_2', 'Nu exista'))