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
la chiave passata come parametro all'interno della funzione e ritornare il numero
di visite effettuate; se la chiave non viene trovata ritornare -1.

Consiglio:
    implementa l'esercizio con due funzioni.
"""

import albero

def ex6(tree, key):
    result = ricerca(tree, key)
    
    if result[1]:
        return result[0]
    else:
        return -1
    
    
def ricerca(tree, key):
    if not tree:
        return 0, False
    
    if tree.key == key:
        return 1, True
    
    visite = 1
    trovato = False
    
    visite_l, trovato = ricerca(tree.left, key)
    visite += visite_l
    
    if trovato:
        return visite, True
    
    visite_r, trovato = ricerca(tree.right, key)
    visite += visite_r
    
    if trovato:
        return visite, True
    
    return visite, False
    
    
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

