#%% es_1
"""
Scrivere una funzione ricorsiva che, data una stringa, restituisca vero se la 
stringa contiene solo coppie consecutive formate da una cifra numerica e un 
carattere alfabetico; falso altrimenti.
"""

# @trace
def ex1(stringa):
    pass
        

# ex1.trace("3d4f2g")
print(ex1("3d4f2g"))


#%% es_2
"""
Scrivere una funzione ricorsiva booleana che data una stringa, un carattere, 
(stringa di lunghezza 1) e un intero n, restituisca il True se il carattere è 
presente ALMENO n volte nella stringa, False altrimenti.
"""

# @trace
def ex2(stringa, caratere, n):
    pass
        
        
# ex2.trace("trentatre trentini", "t", 4)
print(ex2("trentatre trentini", "t", 4))


#%% es_3
"""
Scrivere una funzione ricorsiva che data una stringa restituisca la stringa 
ottenuta da eliminando le vocali. Ad esempio l"invocazione ex3("pippo") deve
restituire la stringa "ppp".
"""

# @trace
def ex3(stringa):
    pass
    
    
# ex3.trace("trentatre")
print(ex3("trentatre trentini"))


#%% es_4
"""
Scrivere una funzione ricorsiva che, data una stringa, restituisca come 
risultato la stringa ottenuta elimanando tutti i caratteri ripetuti 
consecutivamente, tranne il primo.

Es: 
    ex4("aaabbcccc")  =>  "abc"
    ex4("ababcc")     =>  "ababc"
"""
# @trace
def ex4(stringa):
    pass
    
    
# ex4.trace("aaabbcccc")
print(ex4("aaabbcccc"))


#%% es_5
"""
Scrivere una funzione ricorsiva che data una lista di interi restituisca la 
somma dei soli numeri pari.
"""

# @trace
def ex5(lista_interi):
    pass
    

# ex5.trace([1, 2, 3, 4, 5, 6, 7, 8])
print(ex5([1, 2, 3, 4, 5, 6, 7, 8]))


#%% es_6
"""
Scrivere una funzione ricorsiva che, data una lista di numeri interi (positivi 
o negativi), restituisca True se la somma dei numeri contenuti nella lista è pari, 
False altrimenti (se la lista è vuota, la funzione restituisce il valore True).
"""

# @trace
def ex6(lista_interi):
    pass

# ex6.trace([-2, -3, 4, 5])
print(ex6([-2, -3, 4, 5]))


#%% es_7
"""
Scrivere un funzione ricorsiva che data una stringa controlli se la stringa 
è palindroma.
"""

# @trace
def ex7(stringa):
    pass

# ex7.trace("abmba")
print(ex7("abmba"))


#%% es_8
"""
Scrivere una funzione ricorsiva che, dato una lista di interi, restituisca 
una nuova lista di interi ottenuta a partire dalla lista iniziale, sostituendo 
ogni numero negativo con 0. 

Es:
    ex8([1,-2, 3, 4,-5])  =>  [1, 0, 3, 4, 0]
"""

# @trace
def ex8(lista_interi):
    pass

# ex8.trace()
print(ex8([1,-2, 3, 4,-5]))


#%% es_9
"""
Scrivere una funzione ricorsiva che data una stringa, restituisca una stringa
invertita rispetto alla stringa iniziale. 

Es:
    ex9("pippo")  =>  "oppip"
"""

# @trace
def ex9(stringa):
    pass
    
    
# ex9.trace("pippo")
print(ex9("pippo"))


#%% es_10
"""
Scrivere una funzione ricorsiva che data un stringa, restituisca una stringa 
ottenuta dalla stringa iniziale sostituendo ogni spazio bianco con il carattere 
underscore ("_").

Es:
    ex10("oggi sono andato al mare")  =>  "oggi_sono_andato_al_mare"
"""

# @trace
def ex10(stringa):
    pass
    

# ex10.trace("oggi sono andato al mare")
print(ex10("oggi sono andato al mare"))


#%% es_11
"""
Si definisca una funzione ricorsiva che, data una lista di stringhe e un
carattere, restituisca True se almeno una delle stringhe nella lista
contenga il carattere specificato, e false altrimenti.

Es:
    ex11(["casa", "barca", "albero"], "o")  =>  True

"""

# @trace
def ex11(lista_stringhe, carattere):
    pass
    

# ex11.trace(["casa", "barca", "albero"], "o")
print(ex11(["casa", "barca", "albero"], "o"))


#%% es_12
"""
Si definisca una funzione ricorsiva che, data una lista di stringhe, un
carattere e un intero k, restituisca True se almeno una delle stringhe 
nella lista contiene il carattere specificato esattamente k volte, False 
altrimenti.

Es:
    ex12(["casa", "barca", "albero"], "a", 2)  =>  True
"""

# @trace
def ex12(lista_stringhe, carattere, k):
    pass
    

# ex12.trace(["casa", "barca", "albero"], "a", 2)
print(ex12(["casa", "barca", "albero"], "a", 2))


#%% es_13
"""
Si definisca una funzione ricorsiva che, data una lista di stringhe, un
carattere e due interi k, m, restituisca True se almeno m stringhe nella 
lista contengano il carattere specificato esattamente k volte, False 
altrimenti.

Es:
    ex13(["casa", "barca", "albero"], "a", 2, 2)  =>  True
"""

# @trace
def ex13(lista_stringhe, carattere, k, m):
    pass
    

# ex13.trace(["casa", "barca", "albero"], "a", 2, 2)
print(ex13(["casa", "barca", "albero"], "a", 2, 2))


#%% es_14
"""
Si definisca una funzione ricorsiva che, data una lista di interi l, e intero x, 
verifica che la lista goda della seguente proprietà:

    Per ogni intero i < len(l)/2: 
        l[i] + l[len(l) - i - 1] = x
    
Nota: se la lista è di lunghezza dispari, il valore dell'elemento centrale è 
ininfluente.
"""

# @trace
def ex14(l, x, i = 0):
    pass
    

# ex14.trace([0, 1, 2, 3], 3)
print(ex14([0, 1, 2, 3], 3))


#%% es_15
"""
Si definisca una funzione ricorsiva che, data una lista, un valore v (tipo 
non definito) e un intero k, restituisca True se v è presente in tutte le 
posizioni della lista il cui indice è multiplo di k, False altrimenti.
"""

# @trace
def ex15(lista, v, k):
    pass
    

# ex15.trace(["v", 3, "v", True, "v"])
print(ex15(["v", 3, "v", True, "v"], 2, "v"))


#%% es_16
"""
Scrivere una funzione ricorsiva che data una lista di interi restituisca la 
lista ordinata dall'elemento più piccolo a quello più grande.
(Ovviamente non è valido l'utilizzo di sort o sorted)
"""

# @trace
def ex16(lista_interi):
    pass
    

# ex16.trace([1, 4, 2, 5, 3, 4])
print(ex16([1, 4, 2, 5, 3, 4]))


#%% es_17
"""
Assegnata una lista di caratteri, scrivere una funzione ricorsiva che ritorni
il massimo valore tra le somme di ogni valore ascii con il successivo.
Es:
    ex17(['b', 'A', 'l', '2', '!'])  =>  173
    
    'b' + 'A' = 98 + 65 = 163
    'A' + 'l' = 65 + 108 = 173   --> MAX
    'l' + '2' = 108 + 50 = 158
    '2' + '!' = 50 + 33 = 83
    
"""

# @trace
def ex17(lista_caratteri):
    pass

# ex17.trace(['b', 'A', 'l', '2', '!'])
print(ex17(['b', 'A', 'l', '2', '!']))


#%% es_18
"""
Assegnata una stringa ed un carattere, scrivere una funzione ricorsiva che 
calcoli le occorrenze del carattere nella stringa.
"""

# @trace
def ex18(stringa, carattere):
    pass
    

# ex18.trace("trentatre trentini", "t")
print(ex18("trentatre trentini", "t"))


#%% es_19
"""
Sia assegnato una lista di interi. Scrivere una funzione ricorsiva che 
trovi il massimo valore tra gli interi della lista.
"""

# @trace
def ex19(lista_interi):
    pass

    

# ex19.trace([4, -7, 15, -1, 32, 0])
print(ex19([4, -7, 15, -1, 32, 0]))


#%% es_20
"""
Definire una funzione ricorsiva che data una stringa resituisca vero se la 
stringa è composta dallo stesso numero di caratteri numerici e alfabetici 
falso altrimenti
"""

# @trace
def ex20(stringa): # senza contatori
    pass

# ex18.trace("a2bct45m23")
print(ex20("a2bct45m23"))


#%% es_21
"""
Scrivere una funzione ricorsiva che, assegnati due interi n1 ed n2, restituisca 
la somma di tutti gli interi strettamente compresi tra n1 ed n2
"""

# @trace
def ex21(n1, n2):
    pass
    

# ex21.trace(5, 10)
print(ex21(5, 10))


#%% es_22
"""
Scrivere e una funzione ricorsiva che stampi il contenuto di una lista.
"""

# @trace
def ex22(lista):
    pass
    

# ex22.trace("[1, "x", True, [3, 4]")
print(ex22([1, "x", True, [3, 4]]))


#%% es_23
"""
Definire una funzione ricorsiva che data una stringa restituisca ogni elemento 
delle stringa diviso dagli altri da uno spazio. 

Es:
    ex23("abcd")  =>  "a b c b"
"""

# @trace
def ex23(stringa):
    pass
    

# ex23.trace("abcd")
print(ex23("abcd"))

