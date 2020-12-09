# Programa multiplica o fatorial de um número

numero = int(input('Digite um número inteiro positivo: '))
fatorial = 1

for i in range (1, numero + 1):
    fatorial = fatorial * i
    
print('O fatorial desse número é', fatorial)    
