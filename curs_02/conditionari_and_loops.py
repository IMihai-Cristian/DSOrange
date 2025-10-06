""" Declaratia IF"""

# if expresie:
#     instructiune (set de instructiuni sau declaratii)

# first_number = 10
# second_number = 20

# if first_number < second_number:
#     print('se respecta prima conditie')
#
# if second_number > first_number:
#     print('se respecta a doua conditie')

# if expresie:
#     intructiune 2
#     intructiune 3
#     intructiune 4
#     intructiune 5
#     intructiune 6
# intructiune 7

# first_number = 10
# second_number = 20
# list_ex = ['rosu', 'galben', 'albastru']

# if 'galben' in list_ex:
#     print('expresia este adevarata') #1
#     if first_number > second_number:
#         print('a intrat pe primul if din interior expresie aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#     print('mesaj 1') #2
#     if first_number <= second_number:
#         print('a intrat pe al doilea if din expresie') #3
#         print('mesaj 2') #4
#     print('mesaj 3') #5
# print('mesaj 4') #6


""" conditiile else si elif """

# if expresie:
#     bloc instructiuni
# else:
#     bloc instructiuni

# var_nr = 50
#
# if var_nr > 50:
#     print('nr. este cel putin mai mare sau egal cu 50')
# else:
#     print('nr este mai mic decat 50')
# print(f'Acesta este numarul ales: {var_nr}')

# val_1 = 20
# expression = False
# if expression:
#     val_1 = 30
# else:
#     val_1 = 20
# print(val_1)


# nume = "Ion"
# if nume == "Vlad":
#     print('linia',  65)
# elif nume == "George":
#     print('linia',  67)
# elif nume == "Radu":
#     print('linia',  69)
# else:
#     print("numele nu exista")

""" operator ternar """

# instructiune 1 if expresie else instructiune 2

# var = 'cuvant'
# val_ex = 10 if 'uv' in var else 20
# print(val_ex)

# if 'uv' in var:
#     val_ex = 10
# else:
#     val_ex = 20
# print(val_ex)

# val_ex = 20
# if 'uv' in var:
#     val_ex = 10

""" instructiunea PASS """

# nume = "Vlad"
# if nume == "Vlad":
#     print('linia',  65)
# elif nume == "George":
#     print('linia',  67)
# elif nume == "Radu":
#     pass
#     # print('linia',  69)
# else:
#     print("numele nu exista")


""" FOR  LOOP """
# este folosit pentru a parcurge un obiect iterabil (lista, tuplu, dict, string) -> iteratia este finita

# for <variabila temporara> in <iterabil>:
    # instructiune

# ex.1
# list_ex = ['unu', 'doi', 'trei']
# for var in list_ex:
#     print(var)

# ex.2
ex_dict = {'key_1': 1, 'key_2': 'abc', 'key_3': 10}
# for x in ex_dict:
#     print(x)

# for x in ex_dict.keys():
#     print(x)

# for x in ex_dict:
#     print(ex_dict[x])

# for x in ex_dict.values():
#     print(x)

# var = ''
# for key, value in ex_dict.items():
#     print(f'Cheia: {key} -> are valoare: {value}')
#     var = key
# print(var)


""" FOR cu enumerate """
list_result = []
list_ex = ['A', 'B', 'C']
# for gigel, elem in enumerate(list_ex, start=888):
#     print(gigel)
#     dict_val = {}
#     dict_val[gigel] = elem
#     print(dict_val)
#     list_result.append(dict_val)
#     print(list_result)
# print(list_result)

# counter = 0
# for elem in list_ex:
#     list_result.append({counter: elem})
#     counter += 1
# print(list_result)

""" FOR cu range"""

for item in range(-100, 101, 10):
    list_result.append(item)
print(list_result)

