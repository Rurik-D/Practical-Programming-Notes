"""
Autor: Rurik

Per lo svolgimento di questi esercizi verrà usata la libreria albero utilizzata
durante il corso di fondamenti di programmazione.
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
print(tree)
print(ex1(tree))


#%% es_2
"""

"""

# @trace
def ex2(stringa, caratere, n):
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
        

