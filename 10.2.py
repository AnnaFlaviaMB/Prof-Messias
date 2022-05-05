from random import randint

from collections import Counter

lista = [randint(0, 9) for p in range(0, 50)]
print(lista)
c = Counter(lista)

for numero, repeticoes in c.items():
    if repeticoes > 1:
        result = [indice for indice, item in enumerate(lista) if item == numero]
        print(f'O número "{numero}" se repete nos índices {result}.')
