# skladnia funkcji:
# def nazwa_funkcji (arg_pozycyjne, arg_domyślny=wartość, *arg, **arg)

# # #1 zadanie:
import math
#
# def rownanie_kwadratowe(a,b,c):
#     delta = b**2 - 4 * a * c
#     if delta < 0:
#         print('brak pierwiastków')
#         return -1
#     elif delta == 0:
#         print('jeden pierwiastek')
#         x = (-b)/2*a
#         return x
#     else:
#         print('dwa pierwiastki')
#         x1 = (-b - math.sqrt(delta))/(2*a)
#         x2 = (-b + math.sqrt(delta))/(2*a)
#         return x1,x2
#
#     print(rownanie_kwadratowe(6,1,3))
#     print(rownanie_kwadratowe(1,2,1))
#     print(rownanie_kwadratowe(1,4,1))

#
#     #PRZYKLAD 2
# #1 sposob:
# from math import *
# def dlugosc_odcinka(x1=0,y1=0,x2=0,y2=0):
#     return math.sqrt((x2-x1)**2 + (y2-y1)**2)
#
# #dla argumentow domyslnych
# print(dlugosc_odcinka())
#
# #2 sposob dla argumentow pozycyjnych:
# print(dlugosc_odcinka(1,2,3,4))
# #dwie pierwsze to x1 i y1, dwa nastepne argumenty to takie do ktorych przypisujemy dana wartosc
# print(dlugosc_odcinka(2, 2, y2=2, x2=1))
# #argumenty nie w kolejności
# print(dlugosc_odcinka(y2=5,x1=2,y1=2,x2=6))
# #wywołanie dla dwóch argumentów, reszta przejmuje wartości domyślne
# print(dlugosc_odcinka(x2=5,y2=5))


# "*" oznacza dowolną ilość argumentów przechowywanych  w krotce
# def ciag(* liczby):
#     if len(liczby) == 0:
#         return 0
#     else:
#         suma = 0
#         for i in liczby:
#             suma += i
#         return suma
#
# print(ciag())
# print(ciag(1,2,3.5,4,5,6,7))

# def to_lubie (** rzeczy):
#     for cos in rzeczy:
#
#         print("To jest cos")
#         print("co lubie")
#         print(rzeczy[cos])
#
# to_lubie(slodycze = 'czekolada', jajka = 'kacze')
# import random
# dana = random.choice(range(10))    # LOSOWA LICZBA
# print(dana)


