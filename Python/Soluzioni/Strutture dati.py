"""
Autor: Rurik

In questo file verranno trattati esercizi inerenti a liste, dizionari, tuple e insiemi.
Non sono necessarie conoscenze di altri argomenti per affrontare gli esercizi.
"""



#%%
"""
ES 0 - banale
Data in input una lista di valori, restituire un dizionario contenente per chiavi i valori contenuti nella lista e per valori il numero di
occorrenze del valore nella lista
"""

def es0(lista):
    dizionario = {}
    for val in lista:
        dizionario[val] = dizionario.get(val, 0) + 1
    return dizionario

# print(es0([1, 2, 4, 2, 6, 3, 4, 2, 2, 1, 0, 9]))

# OUT:  {1: 2, 
#        2: 4, 
#        4: 2, 
#        6: 1, 
#        3: 1, 
#        0: 1, 
#        9: 1}




#%%
"""
ES 1 - banale
Data in input una stringa, ritornare una stringa modificata secondo i seguenti parametri:
    'a' -> '4'      'A' -> 'a'      'm' -> 'N'      'x', 'y', 'z' -> '*'
    'e' -> '3'      'E' -> 'e'      'M' -> 'n'      'k', 'j', 'w' -> '#'
    'i' -> '1'      'I' -> 'i'      'n' -> 'M'      
    'o' -> '0'      'O' -> 'o'      'N' -> 'm'      

Infine gli spazi ' ' vengono tradotti in trattini bassi '_'.
"""

def es1(stringa):
    traduzione = {'a' : '4', 'A' : 'a', 'm' : 'N', 'x' : '*', 'y' : '*', 'z' : '*', 
                  'e' : '3', 'E' : 'e', 'M' : 'n', 'k' : '#', 'j' : '#', 'w' : '#', 
                  'i' : '1', 'I' : 'i', 'n' : 'M', 'o' : '0', 'O' : 'o', 'N' : 'm', ' ' : '_'}
    
    return stringa.translate(str.maketrans(traduzione))
    # return stringa.translate(str.maketrans("aeioAEIOmMnNxyzkjw ", "4310aeioNnMm***###_"))

# print(es1("Testo di Esempio cOn Molta fantasia xyz kjw"))

# OUT : T3st0_d1_es3Np10_coM_n0lt4_f4Mt4s14_***_###




#%%
"""
ES 2 - 

"""

def es2():
    # inserisci qui il tuo codice
    pass




#%%
"""
ES 3 - 

"""

def es3():
    # inserisci qui il tuo codice
    pass