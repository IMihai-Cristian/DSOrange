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
# ex_dict = {'key_1': 1, 'key_2': 'abc', 'key_3': 10}
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
# list_result = []
# list_ex = ['A', 'B', 'C']
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

# for item in range(-100, 101, 10):
#     list_result.append(item)
# print(list_result)


""" BREAK si CONTINUE """

# for animal in ['urs', 'maimuta', 'melc', 'vulpe', 'magar']:
#     if animal.startswith('m'):
#         continue
#     print(animal)

# for animal in ['urs', 'maimuta', 'melc', 'vulpe', 'magar']:
#     if animal.startswith('m'):
#         break
#     print(animal)

# for animal in ['urs', 'maimuta', 'melc', 'vulpe', 'magar']:
#     if animal.startswith('m'):
#         pass
#     print(animal)


""" FOR poate avea si ELSE """

# for animal in ['urs', 'maimuta', 'melc', 'vulpe', 'magar']:
#     print(animal)
#     break
# else:
#     print('OK')





""" WHILE """

# nr = 0
# while nr > 0:
#     nr -= 1
#     print(nr)

# animal = ['urs', 'maimuta', 'melc', 'vulpe', 'magar']
# while animal:
#     print(animal.pop(-1))
#     print(animal)

# nr_ex = 1
# while nr_ex:
#     print('OK')
#     nr_ex -= 1


""" BREAK si CONTINUE """

# nr = 5
# while nr > 0:
#     nr -= 1
#     if nr == 1:
#         continue
#     print(nr)
# print('FINAL')

""" ELSE """


# nr = 5
# while nr > 0:
#     nr -= 1
#     print(nr)
# else:
#     print('OK')

""" DECLARATIILE MATCH / CASE """


# car = "Dacia"
#
# match car:
#     case 'Audi' | 'BMW':
#         print('German Cars')
#     case 'Dacia':
#         print('Romanian Cars')
#     case 'Fiat':
#         print('Italian Cars')
#     case _:
#         print('Other Cars')

"""Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
afisati numarul pozitiv."""

# var = int(input('Introduceti nr.:'))
# if var > 0:
#     print('Nr este pozitiv')
#     if var < 10:
#         print('Nr este mai mic decat 10')
#     else:
#         print('Nr este mai mare sau egal 10')
# elif var == 0:
#     print('Nr este 0')
# else:
#     print(f'Nr este negativ. Valoarea lui este {abs(var)}')


var = int(input('Introduceti nr.:'))
if 0 < var < 10:
    print('Nr este pozitiv. Nr este mai mic decat 10')
elif var >= 10:
        print('Nr este mai mare sau egal 10')
elif var == 0:
    print('Nr este 0')
else:
    print(f'Nr este negativ. Valoarea lui este {abs(var)}')