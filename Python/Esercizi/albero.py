
import copy
import random

class AlberoBinario:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


################### DA QUI IN GIÙ SONO SOLO FUNZIONI NECESSARIE PER I TEST #####################

    @classmethod
    def fromList(cls, lista):
        """
        Costruisce l'albero da una lista [key, sinistro, destro]
        In cui sinistro e destro sono altrettanti alberi oppure il key None
        :param lista:
        :return:
        """
        key, left, right = lista
        if left: left = cls.fromList(left)
        if right: right = cls.fromList(right)
        return cls(key, left, right)

    def toList(self):
        """
        Converte l'albero in lista di liste [key, sinistra, destra]
        :return:
        """
        left = None if not self.left else self.left.toList()
        right = None if not self.right else self.right.toList()
        return [self.key, left, right]

    def __eq__(self, other):
        """
        Confronta due alberi
        :param other:
        :return:
        """
        return other != None and \
               type(self) == type(other) and \
               self.key == other.key and \
               self.left == other.left and \
               self.right == other.right

    def __repr__(self, livello=0):
        """
        Stampa un albero con livello di indentazione dato
        :param livello: indentazione
        :return:
        """
        indent = "|  "*livello
        res = "{0}Nodo_{1}: {2.key}".format(indent, id(self), self)
        indent = "|  "*(livello+1)
        if self.left:
            res += "\n{}".format(self.left.__repr__(livello+1))
        else:
            res += "\n{}{}".format(indent, self.left)
        if self.right:
            res += "\n{}".format(self.right.__repr__(livello+1))
        else:
            res += "\n{}{}".format(indent, self.right)
        return res

    @classmethod
    def randomTree(cls, level):
        """
        Genera un albero casuale di al più level livelli
        :param level:
        :return:
        """
        if random.randint(0, 100) < 10 or level < 0:    # nel 10% dei casi è None
            return None
        key = random.randint(1, 1000000)
        left = cls.randomTree(level - random.randint(1,3)) # accorcio la profondita da 1 a 3 livelli a caso
        right = cls.randomTree(level - random.randint(1,3)) # accorcio la profondita da 1 a 3 livelli a caso
        return cls(key, left, right)

if __name__ == '__main__':
    lista = [1, [2, None, None],
                [3, [4, None, None],
                    [5, None, None],
                ],
            ]
    albero  = AlberoBinario.fromList(lista)
    albero2 = copy.deepcopy(albero)
    albero3 = AlberoBinario.randomTree(10)

    print('A =', albero, sep='\n')
    print('B =', albero2, sep='\n')
    print('A =', albero.toList())
    print('C =', albero3 )
    print('C =', albero3.toList() )
