# Estudo de vetore. Calcular média

notas = [[5.0, 4.5,7.0, 5.2, 6.1],
         [2.1, 6.5,8.0, 7.0, 6.7],
         [8.6, 7.0, 9.1,8.7, 9.3]]
cont = soma = 0
for i in range (len(notas)):
    for j in range (len(notas[i])):
        soma += notas [i][j]
        cont += 1

media = soma/cont
print(media)
