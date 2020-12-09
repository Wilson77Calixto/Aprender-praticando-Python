# Programa realiza soma acumulada

num1 = int(input('Digite uo valor inicial: '))
num2 = int(input('Digite o valor final: '))

soma = 0

while num1 <= num2:
    if num1 % num2 == 0:
        soma = soma + num1
    num1 += 1
print('A soma é', soma)
    
