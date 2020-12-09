# Programa conta quantidade de números pares fornecidos pelo usuário

num1 = int(input('Digite uo valor inicial: '))
num2 = int(input('Digite o valor final: '))

soma = 0

for i in range (num1,num2 + 1):
    if num1 % num2 == 0:
        soma += 1
    
print('A soma é', soma)
    
