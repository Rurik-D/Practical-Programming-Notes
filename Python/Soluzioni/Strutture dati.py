"""
Autor: Rurik

In questo file verranno trattati esercizi inerenti a liste, dizionari, tuple e insiemi.
"""


#%%
""" ES 0 - banale
Data in input una lista di valori, restituire un dizionario contenente per chiavi i valori contenuti nella lista e per valori il numero di
occorrenze del valore nella lista
"""

def es0(lista):
    # inserisci qui il tuo codice
    pass

# print(es0([1, 2, 4, 2, 6, 3, 4, 2, 2, 1, 0, 9]))

# OUT:  {1: 2, 
#        2: 4, 
#        4: 2, 
#        6: 1, 
#        3: 1, 
#        0: 1, 
#        9: 1}



#%%
""" ES 1 - facile
Data in input una lista di interi, scrivere una funzione che ritorni una lista dove il primo elemento è stato sommato con l'ultimo, il secondo
con il penultimo ecc... 
(La nuova lista avrà quindi la metà dei valori, inoltre, se la lista aveva lunghezza dispari, l'ultimo valore non verrà modificato)

"""

def es1(lista):
    # inserisci qui il tuo codice
    pass

# print(es1([4, 7, 15, 8, 2, 1, 4, 13, 1, 11, 10]))
# out : [14, 18, 16, 21, 6, 1]



#%%
""" ES 2 - facile
Scrivi una funzione che, data una lista di numeri, fornisce in output un istogramma basato su questi numeri, usando
asterischi per disegnarlo.
Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:
    ***
    *******
    *********
    *****
"""

def es2(lista):
    # inserisci qui il tuo codice
    pass

# es2([3, 7, 9, 5])



#%%
""" ES 3 - facile
Scrivi una funzione che data in ingresso una stringa contenente n parole separate da spazi o trattini bassi, restituisca 
in output una lista di n interi che rappresentano il numero di consonati di ciascuna parola contenuta nella stringa.
"""

def es3(stringa):
    # inserisci qui il tuo codice
    pass


# es3("Questa, è una_stringa_di_prova!")
# out : [3, 0, 1, 5, 1, 3]



#%%
""" ES 4 - medio
Data una lista di interi ritornare una tupla che contenga in sequenza:
    1. la somma di tutti i valori nella lista
    2. il massimo di tutti i valori
    3. il minimo di tutti i valori
    4. il massimo dei valori pari
    5. il minimo dei valori dispari
    6. il valore presente nell'indice medio della lista 
        (se la lista ha lunghezza pari, la somma dei due valori centrali)
    7. il più piccolo dei valori dispari, con indice pari, compreso tra due valori pari
        (in caso non esista un valore del genere: -1)

Sviluppare su più funzioni.
"""

def es4(lista):
    pass


# es4([-23, 83, 11, 42, 17, 84, 89, -53, -49, 58, -36, 73, 60, 65, 71, -78, 33, -22, -5, -58])

# OUT : (362, 89, -58, 84, -53, 22, -49)



#%%
""" ES 5 - medio
Data una lista di interi, ritornare due liste contenenti l'una i numeri pari della lista e l'altra 
i numeri dispari. La lista dei pari deve essere ordinata in ordine crescente, la lista dei dispari 
in ordine decrescente.
"""

def es5(lista):
    pass


# es5([-23, 83, 11, 42, 17, 84, 89, -53, -49, 58, -36, 73, 60, 65, 71, -78, 33, -22, -5, -58])
# OUT : [-78, -58, -36, -22, 42, 58, 60, 84], [89, 83, 73, 71, 65, 33, 17, 11, -5, -23, -49, -53]



#%%
""" ES 6 - medio
Date due liste di interi, unirle eliminando i numeri negativi e alternando sempre un numero pari
ad uno dispari, seguendo l'ordine crescente (il valore successivo deve essere strettamente più
grande del precedente). Nel caso non ci siano abbastanza pari, o abbastanza dispari, i numeri 
restanti vengono eliminati.
Ritornare la lista finale.
"""
def es6(lista1, lista2):
    pass


# es6([62, -35, 9, 27, 62, -94, -56, -20, 15, 55], [62, -59, 54, 16, -24, 22, -83, 73, 73, 8])
# OUT :  [8, 9, 16, 27, 54, 55, 62, 73]


