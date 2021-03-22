from math import *
TEKST = "w naszym domu nie ma takich rzeczy i w tym twoja zrobiona w domu sprawa"

x = TEKST.count("nie")    #ZLICZANIE ELEMENTÓW W TEKŚCIE
print("W tekście słowo 'nie' występuje tyle razy: ",x)


rozdzielenie = TEKST.split()   #ROZDZIELA TEKST
print(rozdzielenie)

imie = 'Genowefa'

print('Pierwsza i przedostatnia litera to:',imie[0],imie[len(imie)-2])   #WYSWIETLA KTORA LITERE CHCEMY