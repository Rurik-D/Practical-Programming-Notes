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
    #Inserisci qui il tuo codice
    pass

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
    #Inserisci qui il tuo codice
    pass

# print(es1([(2, 3, 'þ'), (0, 1, '←'), (1, 4, '╦'), (3, 2, '♠')]))

# OUT:          0    1    2    3
#          0 [['#', '#', '#', '#'], 
#          1  ['←', '#', '#', '#'], 
#          2  ['#', '#', '#', '♠'], 
#          3  ['#', '#', 'þ', '#']]



#%%
""" ES 2 - medio/facile
Riprendendo il codice dell'es 1, implementare la seguente funzionalità opzionale:
    Le tuple possono contenere un quarto valore 'origine' che indichi il punto di origine della matrice, che di default è in alto a sinistra.
    Questo parametro può essere solo uno di tra 4:
        - UL    'UP-LEFT'
        - UR    'UP-RIGHT'
        - DL    'DOWN-LEFT'
        - DR    'DOWN-RIGHT'
    Se il parametro non è presente viene contato l'ultimo quarto valore presente in una tupla precedente (se il valore di origine non è stato alterato
    lo si consideri UL). Se viene passato un valore origine non pertinente la tupla non va considerata.
    Nella lista d'esempio, la terza tupla va ignorata, di consequenza anche il la modifica dell'origine va ignorata.
"""

def es2(lista):
    #Inserisci qui il tuo codice
    pass

# print(es2([(2, 3, 'þ'), (0, 1, '←', "DL"), (1, 4, '╦', "UR"), (3, 2, '♠'), (0, 0, 'O', "UL"), (0, 0, 'O', "DL"), (0, 0, 'O', "UR"), (0, 0, 'O', "DR")]))

# OUT:
#            [['O', '#', '#', 'O'], 
#             ['#', '#', '#', '♠'], 
#             ['←', '#', '#', '#'], 
#             ['O', '#', 'þ', 'O']]



#%%
""" ES 3 - medio
Data in input una matrice di '-', scrivere una funzione che, tramite un ciclo while, consenta di modificare singolarmente ogni elemento della matrice in un
elemento dato in input (eseguendo una stampa a video della matrice ad ogni iterazione). Tramite terminale bisognerà poter scrivere le coordinate e l'elemento 
nel quale modificare il '-'. Se si tenterà di modificare un elemento già modificato, verrà invece modificato il primo elemento successivo non modificato 
(spostandosi quindi verso destra nella matrice). Se tutti gli elementi sono già stati modificati si mandi un messaggio di errore e si chiuda il programma.
Gestire tutti i possibili errori che potrebbero generarsi.
(impostare subito una condizione di uscita dal while, per evitare di creare un ciclo infinito)

Esempio:

    Input:                 -
        coordintate = 2, 0  | -> 9 volte
        nuovo valore = X    |
                           -

    Output:
        - - -   - - X   - - X   - - X   - - X   - - X   - - X   - - X   X - X   X X X   
        - - -   - - -   X - -   X X -   X X X   X X X   X X X   X X X   X X X   X X X   Matrice piena!
        - - -   - - -   - - -   - - -   - - -   X - -   X X -   X X X   X X X   X X X   
"""

def es3():
    #Inserisci qui il tuo codice
    pass

# es3([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])

#%%
""" ES 4 -

"""

def es4():
    #Inserisci qui il tuo codice
    pass
