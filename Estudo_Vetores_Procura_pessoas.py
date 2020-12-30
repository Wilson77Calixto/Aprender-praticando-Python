# Estudo de Vetores. Encontra a pessoa mais nova

pessoas = []
# Preenche a matriz
for i in range(10):
    nome = input(f'Nome da pessoa {i+1}? ')
    idade = int(input(f' Idade de {nome}? '))
    pessoas.append([nome, idade])

# Procura a pessoa mais nova
menor = 0
for i in range(len(pessoas)):
    if pessoas [i] [1] < pessoas [menor] [1]:
        menor = i

# Imprime a matriz
for pessoa in pessoas:
    print(pessoa)
print(f'A pessoa mais nova é {pessoas[menor] [0]} ')
