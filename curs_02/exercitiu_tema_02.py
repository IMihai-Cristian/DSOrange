""" Cu ajutorul celor invatate in ultima saptamana la curs se va realiza un calculator, astfel:
- calculatorul detine cifre de la 0 la 9,
- semnele matematice cu ajutorul carora se vor putea realiza operatii matematice sunt urmatoarele: + (adunare), - (scadere), / (impartire), * (inmultire)
- pe langa cifrele amintite anterior si semnele matematice se va putea sterge cu ajutorul litere C
- toate operatiile presupun interactiunea cu utilizatorul (functii de tip input)

Mini-proiectul se va adauga pe GitLab si mi se va trimite linkul prin email."""






"""Validator CNP

Se doreste realizarea unui validator de CNP. Mai jos se gasesc regulile.

Codul numeric personal sau CNP este codul unic al fiecărei persoane născute în România, format din exact 13 cifre.
De regulă el este atribuit la naștere fiecărui nou născut, din acest motiv el poate fi regăsit pe certificatul de naștere.
CNP figurează și pe buletinul de identitate sau cartea de identitate precum și pe permisul de conducere.
A fost introdus ca element obligatoriu în actele de identitate, de stare civilă și în alte acte personale printr-un
decret prezidențial semnat de Nicolae Ceaușescu, la 2 martie 1978.

Format: S AA LL ZZ JJ NNN C

S

S reprezintă sexul și secolul în care s-a născut persoana care posedă acel CNP. Persoanelor de sex masculin le sunt
atribuite numerele impare iar persoanelor de sex feminin numerele pare.

Prima cifră a CNP-ului este: (sex bărbătesc / sex femeiesc)

●      1 / 2 - născuți între 1 ianuarie 1900 și 31 decembrie 1999

●      3 / 4 - născuți între 1 ianuarie 1800 și 31 decembrie 1899

●      5 / 6 - născuți între 1 ianuarie 2000 și 31 decembrie 2099

●      7 / 8 - pentru persoanele străine rezidente în România.

●      În plus 9 - pentru persoanele străine.

AA

AA este un număr format din 2 cifre și reprezintă ultimele 2 cifre din anul nașterii.
O persoană născută în anul 1970 va avea la AA 70. (SAA = 170)

Daca o persoana va avea prima cifra cu una din valorile 7,8 (rezidenti) sau 9,
atunci se va considera secolul 20. ex SAA =771 anul nasterii va fi 1971.

LL

LL este un număr format din 2 cifre și reprezintă luna nașterii persoanei.


ZZ

ZZ reprezintă ziua nașterii în format de 2 cifre. Pentru zilele de la 1 la 9 se adaugă 0 înaintea datei.
Spre exemplificare, o persoană născută în prima zi a lunii va avea codul 01.

JJ

JJ este un număr format din două cifre și este reprezentat de codul județului sau sectorului în care s-a născut
persoana ori în care avea domiciliul sau reședința în momentul acordării C.N.P.

De exemplu, pentru Buzău acest număr este 10. Pentru București,
codul este un număr din intervalul 41 și 46 și reprezintă sectorul în care s-a născut acea persoană.

Codurile județelor sunt în ordinea alfabetică a acestora, cu unele excepții.

NNN

NNN este un număr format din 3 cifre din intervalul 001 - 999. Numerele din acest interval se împart pe județe,
birourilor de evidență a populației, astfel încât un anumit număr din acel interval să fie alocat unei singure
persoane într-o anumită zi.

C

C este cifră de control (un cod autodetector) aflată în relație cu toate celelate 12 cifre ale CNP-ului.
Cifra de control este calculată după cum urmează: fiecare cifră din CNP este înmulțită cu cifra de pe aceeași poziție
din numărul 279146358279; rezultatele sunt însumate, iar rezultatul final este împărțit cu rest la 11.
Dacă restul este 10, atunci cifra de control este 1, altfel cifra de control este egală cu restul


- sa am mesaj daca cnp-ul este introdus incorect adica daca are lungimea corespunzatoare (daca nu sa ma puna sa il repet)
- sa am mesaj prin care se confirma eligibilitatea CNP-ului deci cifra de control este verificata
- sa am mesaj final cu informatiile rezultate din analiza cnp-ului (sexul, data nasterii si locul nasterii)"""

locatii = [("01", "Alba")]
# 02	Arad
# 03	Argeș
# 04	Bacău
# 05	Bihor
# 06	Bistrița-Năsăud
# 07	Botoșani
# 08	Brașov
# 09	Brăila
# 10	Buzău
# 11	Caraș-Severin
# 12	Cluj
# 13	Constanța
# 14	Covasna
# 15	Dâmbovița
# 16	Dolj
# 17	Galați
# 18	Gorj
# 19	Harghita
# 20	Hunedoara
# 21	Ialomița
# 22	Iași
# 23	Ilfov
# 24	Maramureș
# 25	Mehedinți
# 26	Mureș
# 27	Neamț
# 28	Olt
# 29	Prahova
# 30	Satu Mare
# 31	Sălaj
# 32	Sibiu
# 33	Suceava
# 34	Teleorman
# 35	Timiș
# 36	Tulcea
# 37	Vaslui
# 38	Vâlcea
# 39	Vrancea
# 40	București
# 41	București - Sector 1
# 42	București - Sector 2
# 43	București - Sector 3
# 44	București - Sector 4
# 45	București - Sector 5
# 46	București - Sector 6
# 51	Călărași
# 52	Giurgiu
# 47	Bucuresti - Sector 7 (desfiintat)
# 48	Bucuresti - Sector 8 (desfiintat)


# var = eval('2 + 2 / 3 - 1 * 5')
# var = eval('{"a": "b"}')
# print(var, type(var))