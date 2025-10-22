# from fisier_ptr_exemple_module import suma
# print(suma(1, 2, 3, 4, 5, 6, c=7, bb=8, x=10), 'linia 3')
import os
import sys

# from fisier_ptr_exemple_module import suma as functie_importata
# print(functie_importata(1, 2, 3, 4, 5, 6, c=7, bb=8, x=10), 'linia 3')

# from fisier_ptr_exemple_module import model_var
# print(model_var)
# model_var = 'nu mai este la fel'
# print(model_var)

# from fisier_ptr_exemple_module import *
# print(suma(1, 2, 3, 4, 5, 6, c=7, bb=8, x=10), 'linia 13')

# import fisier_ptr_exemple_module
# print(fisier_ptr_exemple_module.suma(1, 2, 3, 4, 5, 6, c=7, bb=8, x=10))
# print(fisier_ptr_exemple_module.__file__)

# import fisier_ptr_exemple_module as mod
# print(mod.suma(1, 2, 3, 4, 5, 6, c=7, bb=8, x=10))

from fisier_ptr_exemple_module import model_var

# print(dir(model_var))

# a = [1, 2]
# print(dir(a))

""" pachete """
# VAR 1
# from curs_03.exemplu_pachete import calc
# print(calc(20))
# print(sys.path)
# # /home/mihai/Digital Stack/DSOrange
# sys.path.append('/home/mihai/Digital Stack/DSOrange')
# print(sys.path)
# from curs_03.exemplu_pachete import calc
# print(calc(20))

# VAR 2

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE)
sys.path.append(BASE)
# from curs_02.conditionari_and_loops import var
# print(var)

import math, numbers