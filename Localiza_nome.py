# Programa gera citação a partir de um nome

nome = input('Entre com um nome completo:').strip()

iniciais = ''
inicio = 0
fim = nome.find(' ', inicio)

while fim!= -1:
    iniciais += nome[inicio] + ". "
    inicio = fim + 1
    fim = nome.find(' ', inicio)

sobrenome = nome [inicio:len(nome)].upper()
print(sobrenome + ", " + iniciais.upper().strip())

