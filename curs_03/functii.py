""" Definitie generala """

# def nume_functie(parametru/parametrii):
#     set instructiuni (corpul functiei)
# val = 10
# def my_function():
#     var = 'Rezultat'
#     print(var)
#     print(val)
#     return var
#
# func = my_function()
# print(func)
# # print(var)

""" Parametrii si Argumentele Functiilor """

# def func(nume, cantitate, device):
#     result = f'{nume} a comandat {cantitate} bucati din categoria {device}'
#     return result

# info = func('Mihai', 20, 'calculatoare')
# print(info, 24)


""" Argumente Keyword """

# print(func(nume='Cristi', device='telefoane', tipuri=4))
# print(func(nume='Cristi', device=4, 'telefoane'))
# print(func('telefoane', 'Cristi', device=4))

""" Parametrii Default(standard) """

def func_2(nume='Radu', cantitate=100, device='ceasuri'):
    result = f'{nume} a comandat {cantitate} bucati din categoria {device}'
    return result

# print(func_2())
# print(func_2('Ion', 50))
# print(func_2(device='tablete'))
# print(func_2('Alina', device='tablete'))
print(func_2('Alina', nume='tablete'))