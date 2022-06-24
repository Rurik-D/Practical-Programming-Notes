"""
Autor: Rurik

Gli esercizi che troverete di seguito sono pensati per essere svolti interamente in una riga, con la seguente sintassi:
        def funct(*parametri*):
            return *OneLine*                   (per "OneLine" intendo una serie di istruzioni incastrate tutte in una riga che risolvano un determinato problema)

Sconsiglio lo svolgimento di questi esercizi per chi è alle prime armi, in tal caso amio avviso vi conviene prima avere almeno un'idea generale di:
    - Liste e dizionari (con list e dict comprehesion)
    - Funzioni lambda
    - Built in functions (map, filter, all, any ecc...)

Tanto vi dovevo e tanto v'ho detto, detto ciò in bocca al lupo!
"""


#%%
""" ES 0 - banale
Scrivere una funzione che data una lista di interi, ritorni una lista dove ogni valore della lista iniziale è stato sommato con il precedente (eccetto il primo).
"""

def es0(lista):
    return list(map(lambda i : lista[i-1] + lista[i], range(1, len(lista))))

# print(es0([-3, 6, 12, -5, 8, 19, -9]))    # OUT: [3, 18, 7, 3, 27, 10]



#%%
""" ES 1 - facile
Scrivere una funzione che sommi i valori pari di una lista se il loro valore assoluto elevato alla 3, fratto 2 sia multiplo di 3.
"""

def es1(lista):
    return sum(list(filter(lambda y : ((abs(y) ** 3)//2) % 3 == 0, filter(lambda x : x % 2 == 0, l))))
    pass

# print(es1([2, 5, 7, 8, 4, 12, 6]))      # OUT: 18



#%%
""" ES 2 - facile
Scrivere una funzione che prenda in input una lista di stringhe e restituisca una nuova lista contenente solo le stringhe palindrome della lista iniziale.
(non sono considerati spazi, punteggiature e differenza tra maiuscole e minuscole)
"""

def es2(lista):
    return list(filter(lambda stringa : stringa.lower().translate(str.maketrans("", "", ",.!? ")) == stringa[::-1].lower().translate(str.maketrans("", "", ",.!? ")), lista))

# print(es2(["abba", "luna", "Erano usi suonare.", "a bCcBa", "oggi"]))            # OUT: ['abba', 'Erano usi suonare.', 'a bCcBa']



#%%
""" ES 3 - medio
Scrivere una funzione che, data una stringa, ne elimini la punteggiatura e ritorni una tupla tale che:
    tupla = (numeroVocali, numeroConsonanti)
"""

def es3(stringa):
    return list((len(list(filter(lambda x : x not in ("a","e","i","o","u"), stringa.translate(str.maketrans("",""," ,?!.")).lower()))), len(list(filter(lambda y : y in ("a","e","i","o","u"), stringa.translate(str.maketrans("",""," ,.!?")).lower())))))




#%%
""" ES 4 - medio
Scrivere una funzione che sommi due numeri solo se positivi e divisibili per 2, altrimenti ne faccia la sottrazione.
"""

def es4(num1, num2):
    return (lambda : num1 + num2 if all([num1 % 4 == 0, num2 % 4 == 0, num1 > 0, num2 > 0]) else num1 - num2)()

# print(es4(20, 24))                      # OUT: 44['abba', 'Erano usi suonare.', 'a bCcBa']
# print(es4(21, 24))                      # OUT: -3
# print(es4(-20, 24))                     # OUT: -44



#%%
""" ES 5 - medio/facile
Scrivere una funzione che prenda come parametro 2 liste, faccia la moltiplicazione tra gli elementi dello stesso indice e ritorni una 
lista contenente i valori moltiplicati solo se multipli di 5.
"""

def es5(lista1, lista2):
    #Inserisci qui il tuo codice
    pass



#%%
""" ES 6 - medio/difficile
Scrivere una funzione che, date due liste di interi, ritorni una lista contenente i quadrati dei valori assoluti maggiori di 10 della 
divisione dei multipli di 3.
"""

def es6(lista1, lista2):
    return list(map(lambda j : abs(j) ** 2 , filter(lambda w : w > 10, filter(lambda x : x % 3 == 0, map(lambda y, z : z // y, filter(lambda m : m != 0, lista1), filter(lambda n : n != 0, lista2))))))                                               

import random


x =[]
for i in range(1500):
    x.append(random.randint(-20, 40))

y =[]
for i in range(1500):
    y.append(random.randint(-20, 40))

print(es6(x, y))



#%%
""" ES 7 - difficile
Progettare una funzione che prenda in inuput due stringhe, a e b, di soli numeri (es: a = "3542189432185976" e b = "4568281346714923") considerati numeri 
a una cifra, li converta in interi e per ogni numero di a faccia il prodotto con ogni numero di b, salvando ogni valore ottenuto in una nuova lista. 
Bisogna tornare una lista di liste, dove ogni sottolista contiene i risultati dell'n-esimo valore di a moltiplicato per ogni singolo valore di b.
"""

def es7(a, b):
    return list(map(lambda i : list(map(lambda j: list(map(lambda x1: int(x1), a))[i] * list(map(lambda x2: int(x2), b))[j], list(range(len(a))))), list(range(len(b)))))

# print(es7("3542189432185976", "4568281346714923"))
"""
out:
    [[12, 15, 18, 24, 6, 24, 3, 9, 12, 18, 21, 3, 12, 27, 6, 9], 
    [20, 25, 30, 40, 10, 40, 5, 15, 20, 30, 35, 5, 20, 45, 10, 15], 
    [16, 20, 24, 32, 8, 32, 4, 12, 16, 24, 28, 4, 16, 36, 8, 12], 
    [8, 10, 12, 16, 4, 16, 2, 6, 8, 12, 14, 2, 8, 18, 4, 6], 
    [4, 5, 6, 8, 2, 8, 1, 3, 4, 6, 7, 1, 4, 9, 2, 3], 
    [32, 40, 48, 64, 16, 64, 8, 24, 32, 48, 56, 8, 32, 72, 16, 24], 
    [36, 45, 54, 72, 18, 72, 9, 27, 36, 54, 63, 9, 36, 81, 18, 27], 
    [16, 20, 24, 32, 8, 32, 4, 12, 16, 24, 28, 4, 16, 36, 8, 12], 
    [12, 15, 18, 24, 6, 24, 3, 9, 12, 18, 21, 3, 12, 27, 6, 9], 
    [8, 10, 12, 16, 4, 16, 2, 6, 8, 12, 14, 2, 8, 18, 4, 6], 
    [4, 5, 6, 8, 2, 8, 1, 3, 4, 6, 7, 1, 4, 9, 2, 3], 
    [32, 40, 48, 64, 16, 64, 8, 24, 32, 48, 56, 8, 32, 72, 16, 24], 
    [20, 25, 30, 40, 10, 40, 5, 15, 20, 30, 35, 5, 20, 45, 10, 15], 
    [36, 45, 54, 72, 18, 72, 9, 27, 36, 54, 63, 9, 36, 81, 18, 27], 
    [28, 35, 42, 56, 14, 56, 7, 21, 28, 42, 49, 7, 28, 63, 14, 21], 
    [24, 30, 36, 48, 12, 48, 6, 18, 24, 36, 42, 6, 24, 54, 12, 18]] 
"""

#%%
""" ES 8 - 

"""

def es8(a, b):
    #Inserisci qui il tuo codice
    pass


