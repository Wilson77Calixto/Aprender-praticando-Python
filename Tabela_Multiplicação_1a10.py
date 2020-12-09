# Programa cria tabela de multiplicação de 1 a 10

for table1 in (1, 2, 3, 4, 5, 6, 7, 8, 9,10):
    for table2 in (1, 2, 3, 4, 5, 6, 7, 8, 9,10):
        resp = table1 * table2
        print(table1, 'x', table2, '=', resp)
