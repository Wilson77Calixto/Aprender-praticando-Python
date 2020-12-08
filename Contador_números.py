# Programa que imprime a quantidade de números pares de 100 até 200

numero = 100
contador_pares = 0

while numero <= 200:
    if numero % 2 == 0:
        contador_pares += 1
    numero += 1

print(contador_pares)    
