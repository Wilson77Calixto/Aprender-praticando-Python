# Estudo de função.

def calcula_Tempo(velocidade, distancia):
    tempo = distancia/velocidade
    return tempo

def calcula_Distancia(velocidade, tempo):
    distancia = velocidade * tempo
    return distancia

t = calcula_Tempo(10, 5)
print(t)
d = calcula_Distancia(5, 4)
print(d)

