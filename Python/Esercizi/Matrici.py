"""
Autor: Rurik

Ricordiamo che per matrice si intende un array bidimensionale (array di array) 
contenente, in ciascun sotto-array, qualsiasi tipo di valore. In python le 
rappresentiamo come liste di liste.

Conoscenze richieste:
    - Manipolazione delle strutture dati
    - Manipolazione delle stringhe
"""



#%%
""" ES 0 - banale
Si definisca una funzione che dati in input un valore h, un valore l e un carattere 
alfanumerico x, ritorni una matrice bidimensionale di altezza h, larghezza l e 
composta da soli caratteri k.
"""

def es0(h, l, k):
    #inserisci qui il tuo codice
    pass

# print(es0(3, 3, "#"))
# OUT:   [['#', '#', '#'], 
#         ['#', '#', '#'], 
#         ['#', '#', '#']]



#%%
""" ES 1 - facile
Riutilizzando il codice dell'esercizio precedente, definire una funzione che 
data in input una lista di tuple, dove ogni tupla contiene 3 valori tali 
che 0 <= lista[0] < l, 0 <= lista[1] < h (rappresentanti coordinate xy) e 
lista[2] = carattere, modifichi e ritorni una matrice di caratteri alfanumerici 
(definire a piacimento i caratteri h, l, x della funzione precedente).
La matrice ritornata deve avere nelle coordinate (lista[0][0], lista[0][1]) il 
carattere lista[0][3]. 
Nel caso in cui una tupla cerchi di modificare un punto fuori dalla matrice, la 
tupla in questione va ignorata.
"""

def es1(lista):
    #inserisci qui il tuo codice
    pass

# print(es1([(2, 3, 'þ'), (0, 1, '←'), (1, 4, '╦'), (3, 2, '♠')]))

# OUT:          0    1    2    3
#          0 [['#', '#', '#', '#'], 
#          1  ['←', '#', '#', '#'], 
#          2  ['#', '#', '#', '♠'], 
#          3  ['#', '#', 'þ', '#']]




#%%
""" ES 2 - facile
Data in input una matrice (quadrata), si ritorni la somma delle diagonali
"""

def es2(matrice):
    #inserisci qui il tuo codice
    pass


# print(es2([[ 8,  2,  6, -9,  3,  4, -5], 
#            [ 7, -3, -5,  2, -7,  9,  1], 
#            [ 4, -6, -8,  3,  5,  7,  4], 
#            [-1,  7,  3, -6,  9,  5,  5], 
#            [-6,  2,  9,  6, -5, -1,  2], 
#            [ 5, -4, -7, -3,  6,  8, -2], 
#            [-2,  4,  7,  4,  8, -8,  9]]))

# OUTPUT : 9




#%%
""" ES 3 - medio/facile
Date 2 matrici 4x4 di interi, sommare i valori con stesse coordinate e salvare 
i risultati in una matrice 8x2 da ritornare.
"""
def es3(matrice1, matrice2):
    #inserisci qui il tuo codice
    pass



# print(es3([[4, 2, 3, 4],           # OUT :
#            [3, 1, 3, 4],           #   [[6, 7, 12, 6, 9, 2, 10, 13],
#            [6, 8, 3, 2],           #    [8, 10, 4, 8, 10, 8, 8, 10]]
#            [2, 4, 3, 3]],
#             
#           [[2, 5, 9, 2], 
#            [6, 1, 7, 9], 
#            [2, 2, 1, 6], 
#            [8, 4, 5, 7]]))




#%%
""" ES 4 - medio/facile
Riprendendo il codice dell'es 1, implementare la seguente funzionalità opzionale:
    Le tuple possono contenere un quarto valore 'origine' che indichi il punto 
    di origine della matrice, che di default è in alto a sinistra.
    Questo parametro può essere solo uno di tra 4:
        - UL    'UP-LEFT'
        - UR    'UP-RIGHT'
        - DL    'DOWN-LEFT'
        - DR    'DOWN-RIGHT'
    Se il parametro non è presente viene contato l'ultimo quarto valore presente 
    in una tupla precedente (se il valore di origine non è stato alterato
    lo si consideri UL). Se viene passato un valore origine non pertinente la 
    tupla non va considerata.
    Nella lista d'esempio, la terza tupla va ignorata, di consequenza anche il 
    la modifica dell'origine va ignorata.
"""

def es4(lista):
    #inserisci qui il tuo codice
    pass

# print(es4([(2, 3, 'þ'), (0, 1, '←', "DL"), (1, 4, '╦', "UR"), (3, 2, '♠'), (0, 0, 'O', "UL"), (0, 0, 'O', "DL"), (0, 0, 'O', "UR"), (0, 0, 'O', "DR")]))

# OUT:
#            [['O', '#', '#', 'O'], 
#             ['#', '#', '#', '♠'], 
#             ['←', '#', '#', '#'], 
#             ['O', '#', 'þ', 'O']]




#%%
""" ES 5 - medio
Data in input una matrice di '-', scrivere una funzione che, tramite un ciclo 
while, consenta di modificare singolarmente ogni elemento della matrice in un
elemento dato in input (eseguendo una stampa a video della matrice ad ogni 
iterazione). Tramite terminale bisognerà poter scrivere le coordinate e l'elemento 
nel quale modificare il '-'. Se si tenterà di modificare un elemento già modificato, 
verrà invece modificato il primo elemento successivo non modificato (spostandosi 
quindi verso destra nella matrice). Se tutti gli elementi sono già stati modificati 
si mandi un messaggio di errore e si chiuda il programma.
Gestire tutti i possibili errori che potrebbero generarsi.
(impostare subito una condizione di uscita dal while, per evitare di creare un ciclo infinito)

Esempio:

    Input:
        coordintate = 2, 0
        nuovo valore = X


    Output:
        - - -   - - X   - - X   - - X   - - X   - - X   - - X   - - X   X - X   X X X   
        - - -   - - -   X - -   X X -   X X X   X X X   X X X   X X X   X X X   X X X   Matrice piena!
        - - -   - - -   - - -   - - -   - - -   X - -   X X -   X X X   X X X   X X X   
"""

def es5(matrice):
    #inserisci qui il tuo codice
    pass


# es5([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])




#%%
""" ES 6 - medio
Data in input una matrice, si sommi ogni elemento con il precedente, seguendo 
una spirale che parte dall'origine e gira in senso orario. Si ritorni la matrice 
modificata e il valore che, lungo la spirale, è stato calcolato più di frequente, 
in caso di parità si ritorni il valore maggiore.
"""

def es6(matrice):
    #inserisci qui il tuo codice
    pass

# print(es6([[ 8,  2,  6, -9,  3,  4, -5],        # OUT : [[8,  10, 16, 7,  10, 14, 9],
#            [ 7, -3, -5,  2, -7,  9,  1],        #        [50, 47, 42, 44, 37, 46, 10],
#            [ 4, -6, -8,  3,  5,  7,  4],        #        [43, 60, 52, 55, 60, 53, 14], 
#            [-1,  7,  3, -6,  9,  5,  5],        #        [39, 66, 82, 76, 69, 58, 19],
#            [-6,  2,  9,  6, -5, -1,  2],        #        [40, 59, 79, 70, 64, 57, 21],
#            [ 5, -4, -7, -3,  6,  8, -2],        #        [46, 57, 61, 68, 71, 65, 19],
#            [-2,  4,  7,  4,  8, -8,  9]]))      #        [41, 43, 39, 32, 28, 20, 28]] , 10


