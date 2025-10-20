""" Functie lambda (anonima) """

# element = lambda x: x * 10
#
# def element_1(x):
#     return x * 10

# print(element_1)
#
# print(element(10))
# print(element_1(10))
#
# element_2 = lambda x, y: x + y
# print(element_2(11, 21))


""" Filter """
# list_1 = [1, 5, 3, 6, 8, 12, 4, 3, 11]
#
# # ex cu filter
# list_2 = filter(lambda x: (x % 2 == 0), list_1)
# print(list(list_2))
#
# # ex cu for:
# list_3 = []
# for i in list_1:
#     if i % 2 == 0:
#         list_3.append(i)
# print(list_3)
#
# # ex functie clasica:
#
# def filtrare(var):
#     if var % 2 == 0:
#         return True
#     else:
#         return False
#
# apelare = filter(filtrare, list_1)
# print(list(apelare))


""" MAP """
# list_1 = [1, 5, 3, 6, 8, 12, 4, 3, 11]
# list_2 = map(lambda x: x * 2 if x % 2 == 0 else x * 10 , list_1)
# print(list(list_2))

""" ZIP """

# list_with_int = [1, 2, 3, 4, 5, 6]
# list_with_str = ['one', 'two', 'three', 'four', 'five', 'six']

# result = zip(list_with_int, list_with_str)
# print(list(result))

# list_with_decimals = [1.1, 2.2, 3.3, 4.4, 5.5]

# result_2 = zip(list_with_int, list_with_str, list_with_decimals)
# print(list(result_2))

""" UNZIP """

# val_1, val_2 = zip(*result)
# print('val_1 -> ', list(val_1))
# print('val_2 -> ', list(val_2))


""" COMPREHENSION LIST """

var = 'comprehension'
# caz cu for
# list_ex = []
# for elem in var:
#     list_ex.append(elem)
# print(list_ex)
#
# # caz cu map
# list_map = list(map(lambda x: x, var))
# print(list_map)
#
# # caz cu comprehension:
# list_comp = [elem for elem in var]
# print(list_comp)
#
# list_comp_2 = [elem for elem in var if elem in ['c', 'h', 'n']]
#
# list_with_int = [elem for elem in range(100) if elem % 2 == 0 if elem % 5 == 0]
# print(list_with_int)
# result_3 = ["par" if elem % 2 == 0 else "impar" for elem in range(20)]
# print(result_3)


"""DICTIONARY COMPREHENSION"""

# squared_numbers = {num: num for num in range(1, 11)}
# print(squared_numbers)


"""ANY SI ALL si ISINSTANCE """

# print(isinstance(40, int))

a = [40, 45]
b = [1, 41]
c = [41, 45]

# print(any(i in a for i in b))
# print(all(i in a for i in c))