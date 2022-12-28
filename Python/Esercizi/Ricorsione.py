#%% es_1
"""
Scrivere una funzione ricorsiva che, data una stringa s, restituisce vero se la 
stringa contiene solo coppie consecutive formate da una cifra numerica e un 
carattere alfabetico; falso altrimenti.
"""

# @trace
def ex1(s):
    pass
    
    
    
        

# ex1.trace("3d4f2g")
print(ex1("3d4f2g"))


#%% es_2
"""
Scrivere una funzione ricorsiva booleana che, data una stringa s, una stringa c
di lunghezza 1, e un intero n, restituisce il valore vero se c è presente ALMENO
n volte nella stringa s, falso altrimenti.
"""

# @trace
def ex2(s, c, n):
    pass
        
        
# ex2.trace("trentatre trentini", "t", 4)
print(ex2("trentatre trentini", "t", 4))


#%% es_3
"""
Scrivere una funzione ricorsiva che data una stringa s restituisca la stringa 
ottenuta da s eliminando le vocali. Ad esempio l’invocazione eliminaVocali
(‘pippo’) deve restituire la stringa ‘ppp’.
"""

# @trace
def ex3(s):
    pass
    
    
# ex3.trace("trentatre")
print(ex3("trentatre trentini"))


#%% es_4
"""
Scrivere una funzione ricorsiva che, data una stringa s, restituisce come 
risultato una stringa ottenuta elimanando da s tutti i caratteri ripetuti 
consecutivamente, tranne il primo.
Es: se s = ‘aaabbcccc’ la funzione deve restituire ‘abc’;
    se s = ‘ababcc’    la funzione deve restituire ‘ababc’.
"""
# @trace
def ex4(s):
    pass
    
    
# ex4.trace("aaabbcccc")
print(ex4("aaabbcccc"))


#%% es_5
"""
Scrivere una funzione ricorsiva che data una lista di interi l restituisce la 
somma dei soli numeri pari.
"""

# @trace
def ex5(l):
    pass
    

# ex5.trace([1, 2, 3, 4, 5, 6, 7, 8])
print(ex5([1, 2, 3, 4, 5, 6, 7, 8]))


#%% es_6
"""
Scrivere una funzione ricorsiva che, data una lista di numeri interi (positivi 
o negativi), restituisce come risultato il valore vero se la somma dei numeri 
contenuti nella lista è un valori pari, falso altrimenti. Se la lista è vuota, 
la funzione restituisce il valore vero.
"""

# @trace
def ex6(l):
    pass

# ex6.trace([-2, -3, 4, 5])
print(ex6([-2, -3, 4, 5]))

#%% speciale
"""
somma interi della lista
"""
def ex(lista):
    pass

print(ex([-2, -3, 4, 5]))

#%% speciale
"""
somma interi della lista
"""
def ex(lista):
    pass

print(ex([-2, -3, 4, 5]))

#%% es_7
"""
Scrivere un funzione ricorsiva che data una stringa s controlli se la stringa 
è palindroma.
"""

# @trace
def ex7(s):
    pass

# ex7.trace("abmba")
print(ex7("abmba"))


#%% es_8
"""
Scrivere una funzione ricorsiva che, dato una lista di interi l, restituisca 
una nuova lista di interi ottenuto da l sostituendo ogni numero negativo con 0. 
Ad esempio l’invocazione ex8([1,-2, 3, 4,-5]), deve restituire l’array [1, 0, 3, 4, 0].
"""

# @trace
def ex8(l):
    pass

# ex8.trace()
print(ex8([1,-2, 3, 4,-5]))


#%% es_9
"""
Scrivere una funzione ricorsiva che data una stringa s, restituisca una stringa 
costituita dai caratteri di s invertiti. Ad esempio l’invocazione ex9(‘pippo’) 
deve restituire la stringa ‘oppip’.
"""

# @trace
def ex9(s):
    pass
    
    
# ex9.trace("pippo")
print(ex9("pippo"))


#%% es_10
"""
Scrivere una funzione ricorsiva che data un stringa s, restituisca una stringa 
ottenuta da s sostituendo ogni spazio bianco con il carattere underscore (‘_’).
Ad esempio l’invocazione ex10(‘pippo e topolino’) deve restituire la 
stringa ‘pippo_e_topolino’.
"""

# @trace
def ex10(s):
    pass
    

# ex10.trace("tua madre è leggenda")
print(ex10("tua madre è leggenda"))


#%% es_11
"""
Si definisca una funzione ricorsiva che, data una lista di stringhe e una 
stringa x di un carattere, restituisce true se almeno una di queste stringhe 
contiene il carattere specificato da x, e false altrimenti.
"""

# @trace
def ex11(l, x):
    pass
    

# ex11.trace(["casa", "barca", "albero"], "o")
print(ex11(["casa", "barca", "albero"], "o"))


#%% es_12
"""
Si definisca una funzione ricorsiva che, data una lista di interi l, e un 
valore intero x, verifica che la lista goda della seguente proprietà:

    Per ogni intero i < len(l)/2 : l[i] + l[len(l) - i - 1] = x

Nota: se la lista è di lunghezza dispari, il valore dell’elemento centrale è 
ininfluente.
"""

# @trace
def ex12(l, x):
    pass
    

# ex12.trace([0, 1, 2, 3], 3)
print(ex12([0, 1, 2, 3], 3))


#%% es_13
"""
Si definisca una funzione ricorsiva che, data una lista l, un valore v e un
intero k, restituisce true se il valore v è presente in tutte le posizioni
della lista il cui indice è multiplo di k, e false altrimenti.
"""

# @trace
def ex13(l, v, k):
    pass
    

# ex13.trace(["v", 3, "v", True, "v"])
print(ex13(["v", 3, "v", True, "v"], 2, "v"))


#%% es_14
"""
Scrivere una funzione ricorsiva che data una lista di interi restituisce la 
lista ordinata dall’elemento più piccolo a quello più grande.
"""

# @trace
def ex14(l):
    pass
    

# ex14.trace([1, 4, 2, 5, 3, 4])
print(ex14([1, 4, 2, 5, 3, 4]))


#%% es_15
"""
Assegnato una lista l di float, scrivere una funzione ricorsiva che calcoli il 
massimo valore tra la somma di ogni elemento con il successivo (escluso l’ultimo)
"""

# @trace
def ex15(l):
    pass
    

# ex15.trace([5.1, 7.2, 3.5, 2.4])
print(ex15([5.1, 7.2, 3.5, 2.4]))


#%% es_16
"""
Assegnata una stringa S ed un carattere c, scrivere una funzione ricorsiva che 
calcoli le occorrenze di c in S
"""

# @trace
def ex16(s, c):
    pass
    

# ex16.trace("trentatre trentini", "t")
print(ex16("trentatre trentini", "t"))


#%% es_17
"""
Sia assegnato una lista l di interi. Scrivere una funzione ricorsiva che 
calcoli il massimo valore degli elementi di l.
"""

# @trace
def ex17(l):
    pass

    

# ex17.trace([4, -7, 15, -1, 32, 0])
print(ex17([4, -7, 15, -1, 32, 0]))


#%% es_18
"""
Definire una funzione ricorsiva che data una stringa s resituisce vero se la 
stringa e composta dallo stesso numero di caratteri numerici e alfabetici 
falso altrimenti
"""

# @trace
def ex18(s): # senza contatori
    pass

# ex18.trace("a2bct45m23")
print(ex18("a2bct45m23"))


#%% es_19
"""
Scrivere una funzione ricorsiva che, assegnati due interi N1 ed N2, restituisca 
la somma di tutti gli interi strettamente compresi tra N1 ed N2
"""

# @trace
def ex19(n1, n2):
    pass
    

# ex19.trace(5, 10)
print(ex19(5, 10))


#%% es_20
"""
Scrivere e una funzione ricorsiva che stampi il contenuto di una lista.
"""

# @trace
def ex20(l):
    pass
    

# ex20.trace("[1, "x", True, [3, 4]")
print(ex20([1, "x", True, [3, 4]]))


#%% es_21
"""
Definire una funzione ricorsiva che data una stringa restituisca ogni elemento 
delle stringa diviso dagli altri da uno spazio. Es. ‘abcd’ diventa ‘a b c b’.
"""

# @trace
def ex21(s):
    pass
    

# ex21.trace("abcd")
print(ex21("abcd"))

