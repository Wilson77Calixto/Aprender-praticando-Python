# Programa que acompanha pacientes diagnosticados com COVID-19 QUADRO LEVE.

print ("UNDIADE BÁSICA DE SAÚDE 'VIDA SAUDÁVEL' ")

print ("================================#===============================#===================")
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
data = input("Digite a data de hoje:")
horas = input("Digite hora atual: ")

if idade >= 60:
 print ("Próximo acompanhamento",nome,"em 24 horas")
else:
 print ("Próximo acompanhamento",nome,"em 48 horas")

print("==================================#==============================#====================")

print("Escreva SIM se apresentar alguns do sintomas abaixo ou NÃO caso esteja sem sintomas.")

doença = input("Faz tratamento de alguma doença?")            
dispnéia = input("Está com dificuldade para respirar?")  #Lista para checar condições de saúde do paciente
tosse = input("Está com tosse?")                         #De acordo com o Ministério da Saúde do Brasil  
garganta = input("Está com dor de garganta?")
febre = input("Está com febre?")  
neuro1 = input("Está sentido tontura?")
neuro2 = input ("Está se sentido confusa/o?")




print ("Clique em ENVIAR ACOMPANHAMENTO")
    


