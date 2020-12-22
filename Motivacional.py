# Programa escreve elogios para as melhores provas de uma disciplina com 3 alunos



nome1 = input('Informe o nome do aluno 1: ')
nome2 = input('Informe o nome do aluno 2: ')
nome3 = input('Informe o nome do aluno 3: ')

nota1 = float(input(f'Informe a nota de {nome1}: '))
nota2 = float(input(f'Informe a nota de {nome2}: '))
nota3 = float(input(f'Informe a nota de {nome3}: '))

média = (nota1 + nota2 + nota3)/3
print(f'A média da turma é {média:.2f}.')

if nota1 > média:
    print(f'Parabéns {nome1}!')
if nota2 > média:
    print(f'Parabéns {nome2}!')
if nota3 > média:
    print(f'Parabéns {nome3}!')    
