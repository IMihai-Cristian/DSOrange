var = 10
# print(var/0)

""" Raise Exception """

# var = 10
# if var > 5:
#     raise Exception('Aici este o eroare')

""" try / exception """

# my_text = input('Introduceti un numar: ')
# try:
#     value = int(my_text)
#     print(value)
#     print(variabila_nedeclarata)
# except ValueError:
#     print('Nu pot converti acest sir de caractere')
# except NameError:
#     variabila_nedeclarata = 100
#     print(f'nu stiu ce valoare ai vrut sa aloci, am asignat default valoarea {variabila_nedeclarata}')
# except Exception as e:
#     print('intra pe exceptie', e)

"""ELSE si FINALLY"""


my_text = input('Introduceti un numar: ')
try:
    value = int(my_text)
    print(value)
except ValueError:
    print('Nu pot converti acest sir de caractere')
except NameError:
    variabila_nedeclarata = 100
    print(f'nu stiu ce valoare ai vrut sa aloci, am asignat default valoarea {variabila_nedeclarata}')
except Exception as e:
    print('intra pe exceptie', e)
else:
    print('nu sunt exceptii')
finally:
    print('Printeaza intotdeauna')
