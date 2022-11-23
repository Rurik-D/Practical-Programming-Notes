"""
Autor: Rurik

In questo file verranno trattati esercizi inerenti alle stringhe e alla loro manipolazione.
Sono richieste conoscenze basilari sulle strutture dati, ma perfettamente abbordabili per chi sta alle prime armi con la programmazione.
"""


#%%
""" ES 0 - banale
Data in input una stringa, si eliminino tutte le vocali e si torni una tupla contenente la stringa modificata e il numero di vocali eliminate.
"""

def es0(stringa):
    pass


# es0("Ciao! come stai?")               # OUT : ("C! cm st?", 7)



#%%
""" ES 1 - facile
Scriva una funzione che prende in input un indirizzo e-mail e ritorna un valore booleano se esso è valido o meno.
Per essere valido l'indirizzo deve avere le seguenti caratteristiche:
    - deve iniziare con un nome terminato con la @
    - subito dopo la @ deve essere presente "gmail", "yahoo" o "hotmail" seguito dall'estensione ".com" o ".it" che termina la stringa
    - nella parte iniziale non sono permessi caratteri speciali al difuori da _ e .
"""

def es1(stringa):
    pass


# es1("esempio_94@gmail.com")               # OUT : True
# es1("esempio_94!@gmail.com")              # OUT : False
# es1("esempio_94@termostato.com")          # OUT : False
# es1("esempio_94@gmail.")                  # OUT : False
# es1("@gmail.com")                         # OUT : False
# es1("esempio_94#gmail.com")               # OUT : False



#%%
""" ES 2 - facile
Scrivere una funzione che prenda in input una stringa, inverta maiuscole e minuscole, e ritorni una tupla contenente la stringa modificata, 
il numero di caratteri diventati minuscoli, il numero di caratteri diventati maiuscoli e il numero di caratteri ignorati (numeri o caratteri 
speciali)).
"""

def es2(stringa):
    pass


# es2("Ciao! Come Stai?")               # OUT : ("cIAO! cOME sTAI?", 2, 9, 4)



""" ES 3 - facile
Scrivere una funzione che prenda come parametri una stringa e una lista di caratteri. Si ritorni una lista, di lunghezza pari alla lista passata 
come parametro, ma avente per valori degli interi che rappresentano il numero di occorrenze di ogni carattere (presente nella lista passata) 
nella stringa.
    
    Es:
        es3("ciao, come stai?", ["a", "s", "c"])
        
        OUTPUT => [2, 1, 2]
"""

def es3(stringa, caratteri):
    pass


# es3("ciao, come stai?", ["a", "s", "c"])



#%%
""" ES 4 - facile
Scrivere una funzione che controlli se una stringa è palindroma (attenzione ai caratteri speciali).
In caso positivo ritorni un messaggio di avviso.
In caso negativo ritorni la stringa invertita.
"""

def es4(stringa):
    pass


# es4("Ciao! come stai?")               # OUT : "?iats emoc !oaiC"
# es4("I Topi, Non Avevano Nipoti.")    # OUT : La stringa è palindroma



#%%
""" ES 5 - facile
Scrivere una funzione in cui, data una stringa si ritorni una lista avente per valori il numero di
caratteri alfabetici, dei caratteri numerici e dei caratteri speciali (lo spazio non va contato come
carattere speciale).
"""

def es5(stringa):
    pass


# es5("C140! c0m3 st41?\n0gg1 3 un4 b3ll4 g10rn4t4! :)")
# OUT : [16, 17, 5]



#%%
""" ES 6 - medio/facile
Data in input una stringa, ritornare una stringa modificata secondo i seguenti parametri:
    'a' -> '4'      'A' -> 'a'      'm' -> 'N'      'x', 'y', 'z' -> '*'
    'e' -> '3'      'E' -> 'e'      'M' -> 'n'      'k', 'j', 'w' -> '#'
    'i' -> '1'      'I' -> 'i'      'n' -> 'M'      
    'o' -> '0'      'O' -> 'o'      'N' -> 'm'      

Infine gli spazi ' ' vengono tradotti in trattini bassi '_'.
"""

def es6(stringa):
    # inserisci qui il tuo codice
    pass


# print(es6("Testo di Esempio cOn Molta fantasia xyz kjw"))
# OUT : T3st0_d1_es3Np10_coM_n0lt4_f4Mt4s14_***_###


