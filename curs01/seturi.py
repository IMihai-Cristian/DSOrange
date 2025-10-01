""" Seturile sunt colectii de date imutabile, neordonate si care nu permit duplicate"""

# var_set = set()
# var_set_2 = {1, 2, "3", 4, 2}
# print(var_set_2)

""" pot contine o varietate de elemente dar ATENTIE doar imutabile """
# var_set = {10, 22.2, 'abc', True, (2, 3, 4)}
# print(var_set)

""" len ca la liste/tupluri"""
""" operatori in  si not in la fel ca la liste """
"""operatii seturi """
# var_set_1 = {'a', 'b', 'c'}
# var_set_2 = {'a', 'e', 'f'}
#
# # 1. UNION (preia toate elementele gasite, o singura data)
# print(var_set_1.union(var_set_2))
# print(var_set_1 | var_set_2)

# var_set_1 = {'a', 'b', 'c'}
# var_set_2 = {'a', 'e', 'f'}
#
# # 2. INTERSECTION (preia doar elementele comune dintre colectiile intersectate)
# print(var_set_1.intersection(var_set_2))
# print(var_set_1 & var_set_2)


# var_set_1 = {'a', 'b', 'c'}
# var_set_2 = {'a', 'e', 'f'}
#
# # 3. DIFFERENCE (preia din primul set ce nu gaseste comun in al doilea)
# print(var_set_1.difference(var_set_2)) # {'b', 'c'}
# print(var_set_2.difference(var_set_1)) # {'e', 'f'}
#
# print(var_set_1 - var_set_2) # {'b', 'c'}
# print(var_set_2 - var_set_1) # {'e', 'f'}


# var_set_1 = {'a', 'b', 'c'}
# var_set_2 = {'a', 'e', 'f'}

# # 4. SYMETRIC DIFFERENCE (preia din toate doar ce nu este comun)
# print(var_set_1.symmetric_difference(var_set_2))
# print(var_set_2.symmetric_difference(var_set_1))
#
# print(var_set_1 ^ var_set_2)
# print(var_set_2 ^ var_set_1)

""" Metode la seturi """
var_set_1 = {'a', 'b', 'c'}
var_set_2 = {'a', 'e', 'f'}

# UPDATE
# var_set_1.update(var_set_2)
# print(var_set_1)
# print(var_set_2)

# ADD
# var_set_1.add('d')
# print(var_set_1)

# REMOVE
# var_set_1.remove('a')
# print(var_set_1)

# DISCARD
# var_set_1.discard('g')
# print(var_set_1)

# POP
# var_set_1.pop()
# print(var_set_1)

# CLEAR goleste setul

# name = ['11', 22, 31, 'als', 22]
# print(list(set(name)))