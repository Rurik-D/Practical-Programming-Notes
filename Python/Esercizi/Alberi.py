"""
Autor: Rurik

Per lo svolgimento di questi esercizi verrà usata la libreria 'albero' 
utilizzata durante il corso di fondamenti di programmazione.
Per sciogliere ogni dubbio leggere tale libreria (presente nella cartella 
Python/Librerie).
"""

#%% es_1
"""
Dato un albero binario ritornare il numero di nodi.
"""

import albero

def ex1(tree):
    pass


tree = ['a',                         #            a
          ['b',                      #          /   \
           ['c', None, None],        #        b       g
           ['d',                     #       / \     / \
            ['e', None, None],       #      c   d   h   i
            ['f', None, None]]],     #         / \
          ['g',                      #        e   f
           ['h', None, None],        #
           ['i', None, None]]]

tree = albero.AlberoBinario.fromList(tree)
print(ex1(tree))


#%% es_2
"""
Dato un albero binario con nodi aventi per chiavi numeri in notazione binaria,
ritornare la somma dei soli numeri pari (in notazione decimale).
"""

# @trace
def ex2(tree):
    pass

tree = ['1011',                         #                 1011
          ['0011',                      #               /      \
           ['1001', None, None],        #          0011          0001
           ['1111',                     #         /    \        /    \
            ['0000', None, None],       #      1001    1111  1000    0101
            ['1101', None, None]]],     #             /    \
          ['0001',                      #          0000    1101
           ['1000', None, None],        #
           ['0101', None, None]]]

tree = albero.AlberoBinario.fromList(tree)
print(ex2(tree))
        

#%% es_3
"""
Dato un albero binario ritornare l'altezza massima dell'albero.
"""

import albero

def ex3(tree):
    pass


tree = ['a',                         #            a
          ['b',                      #          /   \
           ['c', None, None],        #        b       g
           ['d',                     #       / \     / \
            ['e', None, None],       #      c   d   h   i
            ['f', None, None]]],     #         / \
          ['g',                      #        e   f
           ['h', None, None],        #
           ['i', None, None]]]

tree = albero.AlberoBinario.fromList(tree)
print(ex3(tree))


#%% es_4
"""
Dato un albero binario con nodi aventi per chiavi caratteri alfabetici, calcolare
la somma dei nodi in valore ascii nelle penultime posizioni, ovvero quei nodi
per i quali nessuno dei figli ha a sua volta dei figli (nel caso sotto d + i).

Produrre una seconda versione in cui vengono considerati "penultimi" tutti i nodi
aventi almeno un figlio senza figli (nel caso sotto b + d + g + i).
"""

import albero

def ex4(tree):
    pass


tree = ['a',                         #            a
          ['b',                      #          /   \
           ['c', None, None],        #        b       g
           ['d',                     #       / \     / \
            ['e', None, None],       #      c   d   h   i
            ['f', None, None]]],     #         / \     /
          ['g',                      #        e   f   j
           ['h', None, None],        #
           ['i',
            ['j', None, None], 
            None]]]

tree = albero.AlberoBinario.fromList(tree)
print(ex4(tree))


#%% es_5
"""
Dato un albero calcolare il numero di nodi al livello k (partendo da 1).
"""

import albero

def ex5(tree, k):
    pass


tree = ['a',                         #            a
          ['b',                      #          /   \
           ['c', None, None],        #        b       g
           ['d',                     #       / \     / \
            ['e', None, None],       #      c   d   h   i
            ['f', None, None]]],     #         / \
          ['g',                      #        e   f
           ['h', None, None],        #
           ['i', None, None]]]

tree = albero.AlberoBinario.fromList(tree)
print(ex5(tree, 3))


#%% es_6
"""
Dato un albero binario con nodi aventi per chiavi caratteri alfabetici, ricercare
la chiave passata come parametro all'interno della funzione, ritornare True o
False a seconda del caso.

Sviluppare questo esercizio con tutte le tipologie di visite ai nodi (pre-order,
in-order e post_order).
"""

import albero

def ex6(tree, key):
    pass
    
tree = ['a',                         #            a
          ['b',                      #          /   \
           ['c', None, None],        #        b       g
           ['d',                     #       / \     / \
            ['e', None, None],       #      c   d   h   i
            ['f', None, None]]],     #         / \     /
          ['g',                      #        e   f   j
           ['h', None, None],        #
           ['i',
            ['j', None, None], 
            None]]]

tree = albero.AlberoBinario.fromList(tree)
print(ex6(tree, 'h'))


#%% es_7
"""
Dato un albero binario con nodi aventi per chiavi caratteri alfabetici, ricercare
la chiave passata come parametro all'interno della funzione e ritornare il numero
di visite effettuate; se la chiave non viene trovata ritornare -1.

Consiglio:
    implementa l'esercizio con due funzioni.
"""

import albero

def ex7(tree, key):
    pass
    
tree = ['a',                         #            a
          ['b',                      #          /   \
           ['c', None, None],        #        b       g
           ['d',                     #       / \     / \
            ['e', None, None],       #      c   d   h   i
            ['f', None, None]]],     #         / \     /
          ['g',                      #        e   f   j
           ['h', None, None],        #
           ['i',
            ['j', None, None], 
            None]]]

tree = albero.AlberoBinario.fromList(tree)
print(ex7(tree, 'h'))


#%% es_8
"""
Esame fondamenti di programmazione 20 giugno 23:
    Dato un albero binario composto da nodi aventi per chiave degli interi, si
    trasformi l'albero in modo tale che ogni figlio sinistro sia minore del figlio
    destro; se questa proprietà non viene rispettata bisogna scambiare la posizione
    dei due figli.
    La funzione restituisce il numero di cambi effettuati.
    
    Esempio:
        
            ______2______                      ______2______
           |             |                    |             |
        __ 7__        ___5___              __ 5__        ___7___
       |      |      |       |     =>     |      |      |       |
      _4_     3_    _0_     _5_          _3_     4_    _0_     _5_
     |   |      |  |   |   |   |        |   |      |  |   |   |   |
     2   -1     1  8   3   2   9       -1   2      1  3   8   2   9

       expected = 4
       
    NB:
        l'albero va solo modificato, non ritornato.
"""

import albero

def ex8(tree):
    pass

tree = [2,
          [7,
            [4, 
              [2, None, None], 
              [-1, None, None]],
            [3, None, 
              [1, None, None]]],
          [5,         
            [0,
              [8, None, None]
              [3, None, None]],
            [5, 
              [2, None, None], 
              [9, None, None]]]]

tree = albero.AlberoBinario.fromList(tree)
print(ex8(tree))


#%% es_9
"""
Esame introduzione agli algoritmi 27 giugno 2022:
    Dato un albero binario di ricerca (ovvero un albero dove ogni sottoalbero
    sinistro ha valori più bassi del nodo padre, e ogni sottoalbero destro ha
    valori maggiori del nodo padre), modificare il valore di ciascun nodo in modo
    che il nuovo valore del nodo risulti la somma di tutte le chiavi che nell'albero 
    iniziale avevano un valore maggiore della sua chiave originaria.

                 10                     61    
               /   \                  /   \    
             7      15             80      20
           /  \    /  \     =>    /  \    /  \     
          3    9  12  20         87  71  49   0
                   \                      \         
                   14                     35
"""

import albero

def ex9(tree):
    pass

tree = [10,                          #           10
          [7,                        #          /   \
           [3, None, None],          #        7      15
           [9, None, None]],         #       / \     / \
          [15,                       #      3   9   12  20          
           [12, None,                #               \
            [14, None, None]],       #                14
           [20, None, None]]]

tree = albero.AlberoBinario.fromList(tree)
print(ex9(tree))

