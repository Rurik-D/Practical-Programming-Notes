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
    for tupla in lista:
        x = tupla[0]
        y = tupla[1]
        k = tupla[2]
        if 0 <= x < larghezza and 0 <= y < altezza:
            matrice[y][x] = k
    return matrice

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
    matrice = [['#' for i in range(4)] for j in range(4)]
    altezza = len(matrice) - 1
    larghezza = len(matrice[0]) - 1
    origine = "UL"
    for tupla in lista:
        x = tupla[0]
        y = tupla[1]
        k = tupla[2]
        if 0 <= x <= larghezza and 0 <= y <= altezza:
            if len(tupla) == 4:
                origine = tupla[3]

            if origine == "UL":
                matrice[y][x] = k
            elif origine == "UR":
                matrice[y][altezza - x] = k
            elif origine == "DL":
                matrice[altezza - y][x] = k
            elif origine == "DR":
                matrice[altezza - y][altezza - x] = k
            
    return matrice

# print(es2([(2, 3, 'þ'), (0, 1, '←', "DL"), (1, 4, '╦', "UR"), (3, 2, '♠'), (0, 0, 'O', "UL"), (0, 0, 'O', "DL"), (0, 0, 'O', "UR"), (0, 0, 'O', "DR")]))

# OUT:
#            [['O', '#', '#', 'O'], 
#             ['#', '#', '#', '♠'], 
#             ['←', '#', '#', '#'], 
#             ['O', '#', 'þ', 'O']]




#%%
""" ES 3 - medio/facile
Data in input una matrice (quadrata), si ritorni la somma delle diagonali
"""

def es3(matrice):
    somma = 0
    i, j = 0, len(matrice[0]) - 1

    for riga in matrice:
        somma += riga[i] + riga[j]
        i += 1
        j -= 1

    return somma


# print(es3([[ 8,  2,  6, -9,  3,  4, -5], 
#            [ 7, -3, -5,  2, -7,  9,  1], 
#            [ 4, -6, -8,  3,  5,  7,  4], 
#            [-1,  7,  3, -6,  9,  5,  5], 
#            [-6,  2,  9,  6, -5, -1,  2], 
#            [ 5, -4, -7, -3,  6,  8, -2], 
#            [-2,  4,  7,  4,  8, -8,  9]]))

# OUTPUT : 9




#%%
""" ES 4 - medio
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

def es4(matrice):
    ALTEZZA = len(matrice)
    LARGHEZZA = len(matrice[0])

    print()
    for y in range(len(matrice)):                                       # stampo la matrice vuota prima del while
            for x in range(len(matrice[y])):
                print(matrice[y][x], end = " ")
            print()

    while True:
        try:                                                            # Gestisco l'eccezione di ValueError in caso non vengano passati numeri
            coordinate = tuple(map(int, input("\nInserire coordinate x,y:\n-> ").translate(str.maketrans(",;./", "    ")).split()))
        except ValueError:
            print("\nLe coordinate inserite non sono valide!\n")
            continue

        riga, colonna = coordinate[1], coordinate[0]
        
        if not(0 <= riga < ALTEZZA and 0 <= colonna < LARGHEZZA):       # gestisco il caso di OutOfRange
            print("\nLe coordinate inserite non sono valide!\n")
            continue

        new_value = input("\nInserire il nuovo valore:\n-> ")

        if matrice[riga][colonna] != '-':                               # se valore occupato cerco valore libero tra i valori successivi
            for y in range(riga, len(matrice)):
                if y == riga:
                    partenza = colonna +1
                else:
                    partenza = 0
                
                for x in range(partenza, len(matrice[y])):
                    if matrice[y][x] == '-':
                        matrice[y][x] = new_value
                        break
                else:
                    continue
                break

            else:                                                       # cerco valore libero nella sezione precedente
                if riga == 0:
                    for x in range(len(matrice[0])):
                        if matrice[0][x] == '-':
                            matrice[0][x] = new_value
                            break
                    else:                                               # valore libero non trovato nella sezione precedente con riga == 0 (range(0) non effettua iterazioni)
                        print("\nLa matrice è piena!\n")
                        break

                else:
                    for y in range(riga):
                        for x in range(len(matrice[0])):
                            if matrice[y][x] == '-':
                                matrice[y][x] = new_value
                                break
                        else:
                            continue
                        break
                    else:                                               # valore libero non trovato nella sezione precedente
                        print("\nLa matrice è piena!\n")
                        break

        else:
            matrice[riga][colonna] = new_value

        print()
        for y in range(len(matrice)):
            for x in range(len(matrice[y])):
                print(matrice[y][x], end = " ")
            print()


# es4([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])


#%%
""" ES 5 - medio
Data in input una matrice, si sommi ogni elemento con il precedente, seguendo una spirale che parte dall'origine e gira in senso orario. Si ritorni la matrice modificata e il 
valore che, lungo la spirale, è stato calcolato più di frequente, in caso di parità si ritorni il valore maggiore.
"""

def es5(matrice):
    riga = 0
    colonna = 0
    run = True
    somme = {}

    bordoSup, bordoDx, bordoInf, bordoSx = 0, len(matrice[0]) - 1, len(matrice) - 1, 0
    faseSup, faseDx, faseInf, faseSx = True, False, False, False


    while run:
        run = False
        if faseSup and colonna + 1 <= bordoDx:
            run = True
            colonna += 1
            matrice[riga][colonna] += matrice[riga][colonna-1]
            valore = matrice[riga][colonna]
            somme[valore] = somme.get(valore, 0) + 1

            if colonna == bordoDx:
                faseSup, faseDx = False, True
                bordoSup += 1

        elif faseDx and riga + 1 <= bordoInf:
            run = True
            riga += 1
            matrice[riga][colonna] += matrice[riga-1][colonna]
            valore = matrice[riga][colonna]
            somme[valore] = somme.get(valore, 0) + 1

            if riga == bordoInf:
                faseDx, faseInf = False, True
                bordoDx -= 1

        elif faseInf and colonna - 1 >= bordoSx:
            run = True
            colonna -= 1
            matrice[riga][colonna] += matrice[riga][colonna+1]
            valore = matrice[riga][colonna]
            somme[valore] = somme.get(valore, 0) + 1

            if colonna == bordoSx:
                faseInf, faseSx = False, True
                bordoInf -= 1

        elif faseSx and riga - 1 >= bordoSup:
            run = True
            riga -= 1
            matrice[riga][colonna] += matrice[riga+1][colonna]
            valore = matrice[riga][colonna]
            somme[valore] = somme.get(valore, 0) + 1

            if riga == bordoSup:
                faseSx, faseSup = False, True
                bordoSx += 1

    sommeFinali = list(somme.items())
    sommeFinali.sort(key = lambda x : x[0], reverse = True)
    sommeFinali.sort(key = lambda x : x[1], reverse = True)
    SOMMA_MAGGIORE = sommeFinali[0][0]
    return matrice, SOMMA_MAGGIORE

print(es5([[ 8,  2,  6, -9,  3,  4, -5],        # OUT : [[8,  10, 16, 7,  10, 14, 9],
           [ 7, -3, -5,  2, -7,  9,  1],        #        [50, 47, 42, 44, 37, 46, 10],
           [ 4, -6, -8,  3,  5,  7,  4],        #        [43, 60, 52, 55, 60, 53, 14], 
           [-1,  7,  3, -6,  9,  5,  5],        #        [39, 66, 82, 76, 69, 58, 19],
           [-6,  2,  9,  6, -5, -1,  2],        #        [40, 59, 79, 70, 64, 57, 21],
           [ 5, -4, -7, -3,  6,  8, -2],        #        [46, 57, 61, 68, 71, 65, 19],
           [-2,  4,  7,  4,  8, -8,  9]]))      #        [41, 43, 39, 32, 28, 20, 28]] , 10




#%%
"""ES 6 - difficile
Progettiamo il nostro primo gioco sulle matrici!
La nostra funzione questa volta non riceverà parametri in input e non ritornerà nulla, si svolgerà tutto interamente sul terminale.
Il gioco si svolgerà su una matrice 11x11 dove ogni valore sarà equivalente ad un under score '_'. Il nostro personaggio (PG), rappresentato dal carattere '@' partirà in posizione 5,5 
(al centro della matrice) e potrà spostarsi dentro di essa tramite i classici comandi WASD. Quando il PG attraversa un bordo della matrice, riappare dall'altra parte (effetto PAC-MAN).
Al disopra della matrice (o dovunque preferiate) dovrà esserci un contatore delle vite del personaggio e un contatore dei punti.
All'interno dell matrice saranno presenti dei nemici, rappresentati con il carattere '#' che ad od ogni turno si sposteranno in una casella casuale adiacente (non in diagonale).
Se un nemico entra a contatto con il  nostro PG, si trovano quindi sulla stessa casella, il PG  perderà una vita.
L'obbiettivo del PG è quello di raccogliere punti '+' in giro per la matrice. Il primo punto apparirà in una posizione casuale diversa da quella del PG e del nemico. I successivi punti
compariranno sempre in posizioni casuali diverse da quelle del PC e dei nemici (che andranno aumentando ogni volta che il punto cambia posizione, comparendo in caselle casuali diverse 
da quella del PG, di altri NPC e del punto). Anche i nemici posono prendere i punti '+', facendo comparire altri nemici.
Il gioco va in GAME OVER quando il PG perde tutte e 3 le sue vite.

Per lo svolgimento di questo esercizio consiglio di usare copiare la traccia su uno script vuoto, strutturando il programma su più funzioni con ruoli ben precisi. 
L'esercizio può essere svolto anche utilizzando la programmazione ad oggetti.
"""
import random

def main():
    LATO = 11
    POSIZIONI_TOTALI = [(x, y) for x in range(LATO) for y in range(LATO)]
    PG = [[5, 5], '@']
    GAME_OVER = False
    griglia = resetGriglia(LATO)
    vite = 3
    contaPunti = 0

    posizioniEscluseNemici = []
    posizioniEsclusePunto = []

    posizioniEscluseNemici.append(PG[0])
    nemici = [posizioneCasuale(POSIZIONI_TOTALI, posizioniEscluseNemici), '#']

    posizioniEsclusePunto.append(PG[0])
    posizioniEsclusePunto.append(nemici[0])
    punto = [posizioneCasuale(POSIZIONI_TOTALI, posizioniEsclusePunto), '+']

    while True:
        griglia = aggiornaPosizioni(PG, LATO, griglia, nemici, punto)
        stampaGriglia(LATO,griglia, vite, contaPunti, nemici[:-1])
        if GAME_OVER:
            break
        PG = movimento(PG, LATO)
        for npc in range(len(nemici) - 1):
            nemX = nemici[npc][0]
            nemY = nemici[npc][1]
            nemici[npc] = movimentoCasuale(LATO, nemX, nemY)

        vite, contaPunti, cambiaPosPunto, GAME_OVER = collisioni(PG[0], nemici[:-1], punto[0], vite, contaPunti)
        if cambiaPosPunto:
            posizioniEsclusePunto = [PG[0]]
            for npc in nemici[:-1]:
                posizioniEsclusePunto.append(npc)
            punto[0] = posizioneCasuale(POSIZIONI_TOTALI, posizioniEsclusePunto)

            posizioniEscluseNemici = [tuple(PG[0])]
            posizioniEscluseNemici.append(punto[0])
            for npc in nemici[:-1]:
                posizioniEscluseNemici.append(npc)
            nemici.insert(0, posizioneCasuale(POSIZIONI_TOTALI, posizioniEscluseNemici))
    
    print("GAME OVER!")    
    
def collisioni(PG, nemici, punto, vite, contaPunti):
    cambiaPosPunto = False
    GAME_OVER = False
    if tuple(PG) == punto:                                                                                  # collisione giocatore/punto
        contaPunti += 1
        cambiaPosPunto = True

    for npc in nemici:
        if tuple(PG) == npc:                                                                                # collisione nemico/giocatore
            vite -= 1
        if npc == punto:                                                                                    # collisione nemico/punto
            cambiaPosPunto = True

    if vite <= 0:
        GAME_OVER = True
    return vite, contaPunti, cambiaPosPunto, GAME_OVER


def movimento(PG, LATO):                                                                                    # movimento del personaggio con risoluzione "effetto PAC-MAN"
    m = {'w': lambda coord : coord[1] - 1 if coord[1] - 1 >= 0 else LATO -1,                                # se la posizione è valida, allora muovi, altrimenti effetto PAC-MAN
         'a': lambda coord : coord[0] - 1 if coord[0] - 1 >= 0 else LATO -1,
         's': lambda coord : coord[1] + 1 if coord[1] + 1 < LATO else 0,
         'd': lambda coord : coord[0] + 1 if coord[0] + 1 < LATO else 0}

    asse = {'w': 1,
            'a': 0,
            's': 1,
            'd': 0}

    direzione = input().lower()
    PG[0][asse.get(direzione, 0)] = m.get(direzione, lambda coord : coord[0])(PG[0])                        # se il comando immesso non è valido il personaggio resta fermo
    return PG

def resetGriglia(LATO):                                                                                     # refresh della griglia
    return [["_" for l in range(LATO)] for h in range(LATO)]

def aggiornaPosizioni(PG, LATO, griglia, nemici, punto):                                                    # refresh della griglia + aggiornamento di tutte le posizioni
    griglia = resetGriglia(LATO)
    x, y = punto[0][0], punto[0][1]
    griglia[y][x] = punto[1]
    x, y = PG[0][0], PG[0][1]
    griglia[y][x] = PG[1]

    for npc in nemici[:-1]:
        x, y = npc[0], npc[1]
        griglia[y][x] = nemici[-1]

    return griglia

def stampaGriglia(LATO, griglia, vite, punti, nemici):                                                      # stampo griglia con bordi, vite, punti e numero nemici
    print(f"\n\nvite : {vite}\tpunti : {punti}")
    print("-" * (2 * LATO + 3))
    for riga in range(LATO):
        print("|", end = " ")
        for colonna in range(LATO):
            print(griglia[riga][colonna], end = " ")
        print("|")
    print("-" * (2 * LATO + 3))
    print(f"nemici : {len(nemici)}")


def posizioneCasuale(posTot, posEscluse):                                                                   # spawn nemici e punti, escluse posizioni occupate da altri oggetti
    posTotTmp = posTot.copy()
    for posizione in posEscluse:
        try:
            posTotTmp.remove(tuple(posizione))
        except ValueError:
            continue
    nuovaPosizione = random.choice(posTotTmp)
    return nuovaPosizione[0], nuovaPosizione[1]

def movimentoCasuale(LATO, x, y):                                                                           # movimento nemici con risoluzione "effetto PAC-MAN"
    asse = random.choice(['x', 'y'])
    movimento = random.choice([-1, 1])
    if asse == 'x':
        x += movimento
        if x >= LATO:
            x = 0
        elif x < 0:
            x = LATO - 1

    else:
        y += movimento
        if y >= LATO:
            y = 0
        elif y < 0:
            y = LATO - 1

    return x, y

# main()
