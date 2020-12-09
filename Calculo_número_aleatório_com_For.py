# Programa calcula números aleatórios

import random

x = int(input('Digite um número entre 1 e 10: '))
soma = 0

for contador in range (x):
    numero_sorteado = random.randint(1,10)
    print(numero_sorteado)
    soma = soma + numero_sorteado
    

print('A soma é', soma)          
    
    
