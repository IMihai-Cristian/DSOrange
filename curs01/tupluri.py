""" tuplurile sunt colectii de obiecte si sunt imutabile si ordonate (deci indexabile). Permit elemente duplicate """

tuple_1 = ()
tuple_2 = tuple()

# la fel ca la liste:
#  - ordonare
# - pot sa contina o varietate de elemente
# - concatenare
# - multiplicare
# - len
# - indexare
# - slicing
# - copiere
# - in si not in
# - tupluri intretesute
    # exemplu
var_tuple = (1, [2.4, 'ana', True, None, ['1', 2, False]], ['mere', (2, ), 'abc'], 1)
print(type((2)), type((2, )))

# metode tupluri
# count
print(var_tuple.count(1))
# index