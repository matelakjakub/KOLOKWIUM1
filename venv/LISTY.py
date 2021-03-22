lista2 = []

lista2.append(3)
lista2.append("H")                 #DODAJE ELEMENT NA KONIEC LISTY
lista2.append(5)
lista2.insert(0,"jajko")  #DODAJE ELEMENT DO LISTY W WYBRANYM PRZEZ NAS MIEJSCU
lista2.pop(1) #USUWA Z LISTY ELEMENTR WYBRANY PRZEZ NAS
lista2.remove("H")   #USUWA Z LISTY WARTOŚC
# del lista2[1]      #USUWA Z LISTY WARTOSC O PODANYM INDEKSIE
lista2.extend((2,2,'n'))   #DODAJE ELEMENTY DO LISTY
print(lista2)
lista2.reverse()  #ODWRACA KOLEJNOSC LISTY
print(lista2)

lista3 = [3.25,4.82,112,521,0]    #SORTUJE LISTĘ W KOLEJNOSCI OD NAJMNIEJSZEJ DO NAJWIEKSZEJ
lista3.sort()
print(lista3)




