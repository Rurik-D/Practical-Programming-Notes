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
Scrivere una funzione che somma i valori pari di una lista se il loro valore assoluto elevato alla 3,
fratto 2 sia multiplo di 3.
"""
def es2(l):
    return sum(list(filter(lambda y : ((abs(y) ** 3)//2) % 3 == 0, filter(lambda x : x % 2 == 0, l))))

print(es2([2, 5, 7, 8, 4, 12, 6]))