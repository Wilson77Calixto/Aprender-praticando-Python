# Programa calcula números aleatórios

import random

num = int(input('Digite um número entre 1 e 10: '))
soma = 0
numero_sorteado = random.randint(1,10)
print(numero_sorteado)

while num != numero_sorteado:
    soma = soma + numero_sorteado
    numero_sorteado = random.randint(1,10)
    print(numero_sorteado)

print('A soma é', soma)          
    
    
