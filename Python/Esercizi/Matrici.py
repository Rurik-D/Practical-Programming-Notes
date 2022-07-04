"""
Autor: Rurik

Ricordiamo che per matrice si intende un array bidimensionale (array di array) contenente, in ciascun sotto-array, qualsiasi tipo di valore. In python le rappresentiamo come
liste di liste.

Conoscenze richieste:
    - Manipolazione delle strutture dati
    - Manipolazione delle stringhe
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
""" ES 4 - medio/facile
Data in input una matrice, si ritorni la somma delle diagonali
"""

def es4(matrice):
    return 



# print(es4([[ 8,  2,  6, -9,  3,  4, -5], 
#            [ 7, -3, -5,  2, -7,  9,  1], 
#            [ 4, -6, -8,  3,  5,  7,  4], 
#            [-1,  7,  3, -6,  9,  5,  5], 
#            [-6,  2,  9,  6, -5, -1,  2], 
#            [ 5, -4, -7, -3,  6,  8, -2], 
#            [-2,  4,  7,  4,  8, -8,  9]]))




#%%
""" ES 5 - medio
Data in input una matrice, si sommino i bordi della matrice. Ogni elemento deve essere sommato con i precedenti, partedo dal vertice in alto a sinistra e facendo una roatazione oraria
sui 4 bordi della matrice. L'ultima somma dovrà quindi avvenire sull'elemento (0,1). Si ritorni la matrice modificata e il valore che, lungo i bordi, è stato incontrato più di frequente,
in caso di parità si ritorni il maggiore.
"""

def es5(lista1, lista2, matrice):
    return 

# print(es5([[ 8,  2,  6, -9,  3,  4, -5], 
#            [ 7, -3, -5,  2, -7,  9,  1], 
#            [ 4, -6, -8,  3,  5,  7,  4], 
#            [-1,  7,  3, -6,  9,  5,  5], 
#            [-6,  2,  9,  6, -5, -1,  2], 
#            [ 5, -4, -7, -3,  6,  8, -2], 
#            [-2,  4,  7,  4,  8, -8,  9]]))




#%%
"""ES 6 - difficile
Progettiamo il nostro primo gioco sulle matrici!
La nostra funzione questa volta non riceverà parametri in input e non ritornerà nulla, si svolgerà tutto interamente sul terminale.
Il gioco si svolgerà su una matrice 11x11 dove ogni valore sarà equivalente ad uno spazio bianco. Il nostro personaggio (PG), rappresentato dal carattere '@' partirà in posizione 5,5 
(al centro della matrice) e potrà spostarsi dentro di essa tramite i classici comandi WASD. Quando il PG attraversa un bordo della matrice, riappare dall'altra parte (effetto PAC-MAN).
Al disopra della matrice (o dovunque preferiate) dovrà esserci un contatore delle vite del personaggio e un contatore dei punti.
All'interno dell matrice saranno presenti degli NPC nemici, rappresentati con il carattere '#' che ad od ogni turno si sposteranno in una casella casuale adiacente (non in diagonale).
Se un NPC entra a contatto con il  nostro PG, (si trovano quindi sulla stessa casella), il PG verrà spostato su una casella adiacente casuale (anche in diagonale) e perderà una vita.
L'obbiettivo del PG è quello di raccogliere punti '+' in giro per la matrice. Il primo punto apparirà in una posizione casuale diversa da quella del PG e del NPC. I successivi punti
compariranno sempre in posizioni casuali diverse da quelle del PC e degli NPC (che andranno aumentando ogni 3 punti raccolti, comparendo in caselle casuali diverse da quella del PG, di
altri NPC e del punto).
Il gioco va in GAME OVER quando il PG perde tutte e 3 le sue vite.

Per lo svolgimento di questo esercizio consiglio di usare copiare la traccia su uno script vuoto, strutturando il programma su più funzioni con ruoli ben precisi. 
L'esercizio può essere svolto anche utilizzando la programmazione ad oggetti.
"""
import random

def es6():
    pass

es6()