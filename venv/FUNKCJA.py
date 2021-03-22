from math import *
def pole_rownoleglobok(e,f):
    pole = 1/2 * e * f
    return pole
print(pole_rownoleglobok(12,6))



def ciag(* liczby):      #DODAJE SOBIE DOWOLNAC ILOSC ZMIENNYCH W * LICZBY
    if len(liczby) == 0:
        return 0
    else:
        iloczyn = 1

        for i in liczby:
            iloczyn*=i
        return iloczyn
print(ciag(1,2,3,4,5))


def jazda (** mleko):
    for x in mleko:
        print("Bardzo lubie: ",mleko[x])


jazda(ekologiczne ='uht', chemiczne = 'gizyckie')


