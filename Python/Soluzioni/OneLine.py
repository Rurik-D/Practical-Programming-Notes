"""
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
""" ES 1
Scrivere una funzione che sommi due numeri solo se positivi e multipli di 2, altrimenti ne faccia la sottrazione.
"""
def es1(a, b):
    return (lambda : a + b if all([a % 4 == 0, b % 4 == 0, a > 0, b > 0]) else a - b)()

print(es1(20, 24))
print(es1(21, 24))
print(es1(-20, 24))


#%%
""" ES 2
Scrivere una funzione che sommi i valori pari di una lista se il loro valore assoluto elevato alla 3,
fratto 2 sia multiplo di 3.
"""
def es2(l):
    return sum(list(filter(lambda y : ((abs(y) ** 3)//2) % 3 == 0, filter(lambda x : x % 2 == 0, l))))

print(es2([2, 5, 7, 8, 4, 12, 6]))

#%%
""" ES 3
Scrivere una funzione che, data una stringa, ne elimini la punteggiatura e ritorni una tupla tale che:
    tupla = (numeroVocali, numeroConsonanti)
"""
def conta_lettere(stringa):
	return list((len(list(filter(lambda x : x not in ("a","e","i","o","u"), stringa.translate(str.maketrans("",""," ,?!.")).lower()))), len(list(filter(lambda y : y in ("a","e","i","o","u"), stringa.translate(str.maketrans("",""," ,.!?")).lower())))))
