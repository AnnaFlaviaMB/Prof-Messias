#Faça um algoritmo para ler 20 números e armazenar em um vetor./
#Após a leitura total dos 20 números, o algoritmo deve escrever/
#esses 20 números lidos na ordem inversa.

import random
lista = []
for x in range (0, 20):
    lista.append(random.randint(0, 30))
print(lista)

for i in range(0, len(lista)):
    
    maior_numero = lista[i]
    maior_indice = i
    
    for j in range((i+1), len(lista)):
        
        if lista[j] >= maior_numero:
            maior_numero = lista[j]
            maior_indice = j
            
    lista.insert(i, lista.pop(maior_indice))
              
print(lista)