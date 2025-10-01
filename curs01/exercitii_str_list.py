
# 1. Primești un cuvânt și afișează primele 3 litere.
# var = input('Te ascult: ')
# var1 = input('Introduceti nr.')
# print(var[:3])
# print(var[-2:])

# 2. Dintr-un string dat, creează unul nou cu literele în ordine inversă.
# print(var[::-1])

# 3. Primești un string și un număr n.
# Construiește un nou string obținut prin repetarea textului de n ori.
# rezultat = var * int(var1)
# print(rezultat)

# 4.Primești două cuvinte și unește-le cu spațiu între ele.
# var = input('primul str: ')
# var1 = input('al doilea str: ')
# print(var + " " + var1)

# 5. Primești o listă și afișează primul și ultimul element.
# list_1 = [10, 20, 30, 40]
# print([list_1[0], list_1[-1]])

# 6.Dintr-o listă de numere, extrage elementele de pe pozițiile 2, 3 și 4.
# list_1 = [10, 20, 30, 40, 50, 60, 70]
# print(list_1[2:5])

# 7.Primești o listă și creează alta care repetă conținutul de 3 ori.
# list_1 = [1, 2]
# list_2 = list_1 * 3
# print(list_2)

# 8.Primești un cuvânt și transformă-l într-o listă de litere.
# text = 'mere'
# print(list(text))

# 9.Primești o listă de cuvinte și unește-le într-un singur string cu spații între ele.
# lista = ['Ana', 'are', 'mere']
# print(" ".join(lista))

# 10. Primești un string și împarte-l în două bucăți aproape egale, puse într-o listă.
var_a = input("introduceti textul: ")
jumatate = len(var_a) // 2
print([var_a[:jumatate], var_a[jumatate]])