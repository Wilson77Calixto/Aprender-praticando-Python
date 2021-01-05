# Estudo de função. Calcular gorjeta

def calcular_Gorjeta(valor, percentual = 10):
    return valor * percentual/100

gorjeta = calcular_Gorjeta(400)
print('O valor da gorjeta de 10% de uma conta de R$ 400,00 é R$ {:.2f}'.format (gorjeta))
gorjeta = calcular_Gorjeta(400, 5)
print('O valor da gorjeta de 5% de uma conta de R$ 400,00 é R$ {:.2f}'.format (gorjeta))

