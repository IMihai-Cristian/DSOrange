"""
r -> modul de CITIRE (nu adauga in fisier si daca fisierul nu exista, atunci cand am valoare r, o sa am eroare)
w -> modul de SCRIERE (daca fisierul nu exista, Py il creaza iar daca exista ceva in fisier, Py rescrie)
a -> modul de APPENDUIRE (daca fisierul nu exista, Py il creaza iar daca exista ceva in fisier, Py scrie in continuare)
"""
import csv

# file = open('data.txt', 'r')
# print(file)

# file = open('data.txt', 'w')
# file.write('Astazi este miercuri')
# file.close()

# file = open('data.txt', 'a')
# file.write('Astazi este miercuri')
# file.close()

# file = open('data.txt', 'r+')
# file.write('Astazi este miercuri')
# file.close()

# file = open('data.txt', 'w')
# try:
#     file.write('Astazi este miercuri')
# finally:
#     file.close()

""" Context manager """

# with open('data2.txt', 'w') as file:
#     file.write('Astazi este miercuri')

""" Citire din fisiere """

# VAR 1
# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)

# VAR 2
# with open('data.txt', 'r') as file:
#     # print(list(file))
#     for line in list(file):
#         print(line)

# VAR 3
# with open('data.txt', 'r') as file:
#     while True:
#         line = file.readline()
#         print(line)
#         if not line:
#             break


""" CSV file """

# with open('fisier_csv.csv', 'r') as csv_file:
#     rows = csv.reader(csv_file, delimiter=',')
#     # print(rows)
#     # print(type(rows))
#     for row in rows:
#         print(row)

# """Adaugare randuri"""
#
# car_list =[
#     ['Dacia', 'Logan', 2015, 90],
#     ['BMX', 'X5', 2023, 250]
# ]
#
# with open('fisier_csv.csv', 'a', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     csv_writer.writerows(car_list)
    # for line in car_list:
    #     csv_writer.writerow(line)


# import datetime
from datetime import datetime, timedelta
time_now = datetime.now() + timedelta(days=30)
print(time_now)
# print(time_now.strptime('22:01:23 10:50', '%d%m%Y %H%M'))
# print(time_now.strftime('%d%m%Y %H%M'))