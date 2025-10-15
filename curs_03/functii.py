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

# def func_2(nume='Radu', cantitate=100, device='ceasuri'):
#     result = f'{nume} a comandat {cantitate} bucati din categoria {device}'
#     return result

# print(func_2())
# print(func_2('Ion', 50))
# print(func_2(device='tablete'))
# print(func_2('Alina', device='tablete'))
# print(func_2('Alina', nume='tablete'))

# rezumat:
# CAZ 1: parametrii pozitionali: def func(a, b, c)
# 1. argumente pozitionale func(10, 20, 30) -> conteaza atat ordinea cat si ca nr. argumente = nr. parametrii
# 2. argumente keyword(c=10, a=20, b=30) -> nu conteaza ordinea ci doar nr. argumente = nr. parametrii
# 3. argumente mix(10, c=20, b=30) -> conteaza ca intotdeauna pozitional inainte si keyword dupa iar nr. argumente = nr. parametrii

# CAZ 2: parametrii default: def func(a=1, b=3, c=7)
# 1. argumente pozitionale func(10, 20, 30) -> conteaza ordinea si ca nr. argumente <= nr. parametrii
#                                              (daca sunt mai putine argumente, dupa ultimul furnizat restul preiau
#                                              valoarea default a parametrilor iar daca sunt mai multi-->eroare)
# 2. argumente keyword(c=10, a=20, b=30) -> nu conteaza ordinea ci doar ca nr. argumente <= nr. parametrii
# #                                        (daca sunt mai putine argumente, cele care lipsesc preiau
# #                                        valoarea default a parametrilor iar daca sunt mai multi-->eroare)
# 3. argumente mix(10, c=20, b=30) -> conteaza ca intotdeauna pozitional inainte si keyword dupa, iar nr. argumente <= nr. parametrii
# #                                        (daca sunt mai putine argumente, cele care lipsesc preiau
# #                                        valoarea default a parametrilor iar daca sunt mai multi-->eroare)

# CAZ 3: parametrii mix(pozitional cu default): def func(a, b=3, c=7)  # se respecta ordinea cu param pozitionali primii
# unde am param pozitional se respecta regulile de la caz 1
# unde am param default se respecta regulile de la caz 2

""" return """

# def calc(x):
#     if x < 0:
#         return
#     if x > 10:
#         return
#     print(x)
#
# # res = calc(-2)
# res = calc(5)
# print(res)

""" ANOTARI """

# def calcul(a: int , b: int, c: int) -> int:
#     return a + b + c
#
# print(calcul('20', '10', '30'))


""" args si kwargs """

# def suma(a, b=0, *args):
    # print(type(args))
    # initial = a + b
    # total = 0
    # for elem in args:
    #     total += elem
    # return initial + total
#
# var = suma(1, 2, 3, 4, 5, 6)
# print(var)
# print(suma(10))


# def suma(a, b=0, *args, **kwargs):
#     initial = a + b
#     print(initial)
#     total = 0
#     for elem in args:
#         total += elem
#     for key, value in kwargs.items():
#         total += value
#     # print(kwargs)
#     return initial + total
#
# # var = suma(1, 2, 3, 4, 5, 6, c=7, bb=8, x=10)
# var = suma(2, c=10, bb=20, x=30, d=15)
# print(var)

""" RECURSIVITATE """

def test_func(nr):
    if nr > 100:
        return nr
    else:
        print(f'Nr. este acum {nr}')
        return test_func(nr+10)

val = test_func(57)
print(val)
