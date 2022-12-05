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
    #Inserisci qui il tuo codice
    pass

# print(es0([-3, 6, 12, -5, 8, 19, -9]))    # OUT: [-3, 3, 18, 7, 3, 27, 10]



#%%
""" ES 1 - facile
Scrivere una funzione che sommi i valori pari di una lista se il loro valore assoluto elevato alla 3, fratto 2 sia multiplo di 3.
"""

def es1(lista):
    #Inserisci qui il tuo codice
    pass

# print(es1([2, 5, 7, 8, 4, 12, 6]))      # OUT: 18



#%%
""" ES 2 - facile
Scrivere una funzione che prenda in input una lista di stringhe e restituisca una nuova lista contenente solo le stringhe palindrome della lista iniziale.
(non sono considerati spazi, punteggiature e differenza tra maiuscole e minuscole)
"""

def es2(lista):
    #Inserisci qui il tuo codice
    pass

# print(es2(["abba", "luna", "Erano usi suonare.", "a bCcBa", "oggi"]))            # OUT: ['abba', 'Erano usi suonare.', 'a bCcBa']



#%%
""" ES 3 - medio
Scrivere una funzione che, data una stringa, ne elimini la punteggiatura e ritorni una tupla tale che:
    tupla = (numeroVocali, numeroConsonanti)
"""

def es3(stringa):
    #Inserisci qui il tuo codice
    pass

# print(es3("Hello world!(con molta fantasia :))."))          # OUT: (10, 16)





#%%
""" ES 4 - medio
Scrivere una funzione che sommi due numeri solo se positivi e divisibili per 2, altrimenti ne faccia la sottrazione.
"""

def es4(num1, num2):
    #Inserisci qui il tuo codice
    pass

# print(es4(20, 24))                      # OUT: 44
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

# print(es5([1, 3, 6, 5], [5, 7, 10, 9, 4]))     # OUT: [5, 60, 45]





#%%
import random
""" ES 6 - medio/difficile
Scrivere una funzione che, date due liste di interi, ritorni una lista contenente i quadrati dei valori assoluti maggiori di 10 della 
divisione dei multipli di 3.
"""

def es6(lista1, lista2):
    #Inserisci qui il tuo codice
    pass



"""
x = []
for i in range(1500):
    x.append(random.randint(-20, 40))

y = []
for i in range(1500):
    y.append(random.randint(-20, 40))

print(es6(x, y))
"""



#%%
""" ES 7 - difficile
Progettare una funzione che prenda in inuput due stringhe, a e b, di soli numeri (es: a = "3542189432185976" e b = "4568281346714923") considerati numeri 
a una cifra, li converta in interi e per ogni numero di a faccia il prodotto con ogni numero di b, salvando ogni valore ottenuto in una nuova lista. 
Bisogna tornare una lista di liste, dove ogni sottolista contiene i risultati dell'n-esimo valore di a moltiplicato per ogni singolo valore di b.
"""

def es7(a, b):
    #Inserisci qui il tuo codice
    pass

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
""" ES 8 - difficile         (parte di un HW dell'AA22-23)
Dati in input una lista di parole e un dizionario avente per chiavi indici che vanno da 0 alla lunghezza della parola più lunga all'interno della lista-1, e
per valori dei dizionari vuoti; bisogna riempire i dizionari vuoti interni in modo tale che abbiano, per chiavi le lettere delle parole che compaiono all'indice
che fa da chiave a quel dizionario, e per valori la frequenza di quelle lettere.
"""

def es8(occurrences, words):
    #Inserisci qui il tuo codice
    pass

# w = ['house', 'garden', 'kitchen', 'balloon', 'home', 'park', 'affair', 'kite', 'hello', 'portrait', 'angel', 'surfing']
# occ = { k : {} for k in range(max(list(map(lambda x : len(x), words)))) }
# print(es8(occ, w))

"""
out: 
    {
    0: {'h': 3, 'g': 1, 'k': 2, 'b': 1, 'p': 2, 'a': 2, 's': 1}, 
    1: {'o': 3, 'a': 3, 'i': 2, 'f': 1, 'e': 1, 'n': 1, 'u': 1}, 
    2: {'u': 1, 'r': 4, 't': 2, 'l': 2, 'm': 1, 'f': 1, 'g': 1}, 
    3: {'s': 1, 'd': 1, 'c': 1, 'l': 2, 'e': 3, 'k': 1, 'a': 1, 't': 1, 'f': 1}, 
    4: {'e': 2, 'h': 1, 'o': 2, 'i': 2, 'r': 1, 'l': 1}, 
    5: {'n': 2, 'e': 1, 'o': 1, 'r': 1, 'a': 1}, 
    6: {'n': 2, 'i': 1, 'g': 1}, 
    7: {'t': 1}
    }
"""

