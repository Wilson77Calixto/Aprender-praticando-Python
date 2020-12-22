# Programa escreve elogios para as melhores provas de uma disciplina com 40 alunos

num_alunos = 40
nomes = []
notas = []
média = 0

for i in range(num_alunos):
    nomes.append(input(f'Informe o nome do aluno (1+1): '))
    notas.append(float(input(f'Informe a nota de nomes {nomes[i]}: ')))
    média = média + notas[i]

média = média / num_alunos
print(f'A média da turma é {média:.2f}.')

for i in range(num_alunos):
    if notas [i] > média:
        print(f'Parabéns {nomes[i]}!')

                 

                 

                 

            
