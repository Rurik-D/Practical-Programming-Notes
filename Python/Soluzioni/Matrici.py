"""
Autor: Rurik

Per i seguenti esercizi, a meno che non sia definito diversamente dall'esercizio, si utilizzino matrici composte da liste di liste
"""


#%%
""" ES 0 - banale
Si definisca una funzione che dati in input un valore h, un valore l e un carattere alfanumerico x, ritorni una matrice bidimensionale di altezza
h, larghezza l e composta da soli caratteri k.
"""

def es0(h, l, k):
    return [[k for i in range(h)] for j in range(l)]

# print(es0(3, 3, "#"))
# OUT:   [['#', '#', '#'], 
#         ['#', '#', '#'], 
#         ['#', '#', '#']]



#%%
""" ES 1 - facile
Riutilizzando il codice dell'esercizio precedente, definire una funzione che data in input una lista di tuple, dove ogni tupla contiene una 3 valori
tali che 0 <= lista[0] < l, 0 <= lista[1] < h (rappresentanti coordinate xy) e lista[2] = carattere, modifichi e ritorni una matrice di caratteri 
alfanumerici (definire a piacimento i caratteri h, l, x della funzione precedente).
La matrice ritornata deve avere nelle coordinate (lista[0][0], lista[0][1]) il carattere lista[0][3]. 
Nel caso in cui una tupla cerchi di modificare un punto fuori dalla matrice, la tupla in questione va ignorata.
"""

def es1(lista):
    matrice = [['#' for i in range(4)] for j in range(4)]
    altezza = len(matrice)
    larghezza = len(matrice[0])
    for elemento in lista:
        x = elemento[0]
        y = elemento[1]
        k = elemento[2]
        if 0 <= x < larghezza and 0 <= y < altezza:
            matrice[y][x] = k
    return matrice

print(es1([(2, 3, "þ"), (0, 1, '←'), (1, 4, '╦'), (3, 2, '♠')]))
# OUT:
#            [['#', '#', '#', '#'], 
#             ['←', '#', '#', '#'], 
#             ['#', '#', '#', '♠'], 
#             ['#', '#', 'þ', '#']]



#%%
""" ES 2 -
Riprendendo il codice dell'es 1, implementare la seguente funzionalità opzionale:
    Le tuple possono contenere un quarto valore 'origine' che indichi il punto di origine della matrice, che di default è in alto a sinistra.
    Questo parametro può essere solo uno di tra 4:
        - UL    'UP-LEFT'
        - UR    'UP-RIGHT'
        - DL    'DOWN-LEFT'
        - DR    'DOWN-RIGHT'
    Se il parametro non è presente viene contato l'ultimo quarto valore presente in una tupla precedente (se il valore di origine non è stato alterato
    lo si consideri UL). Se viene passato un valore origine non pertinente la tupla non va considerata.
"""

def es2():
    return 



#%%
""" ES 3 -

"""

def es3():
    return 



#%%
""" ES 4 -

"""

def es4():
    return 
