# Programa calcula Indíce de Massa Corporal (IMC)


massa = float(input("Qual o seu peso (kg): "))
altura = float(input("Qual a sua altura: "))

imc = massa/altura**2

if imc < 18.5:
    print("Você está abaixo do peso.")

elif imc >= 18.6 and imc <= 24.9:
    print("Você está no peso saudável!")

elif  imc >= 25.0 and imc <= 29.9:
    print("Você está com excesso de peso.")

elif imc >= 30.0 and imc <= 34.9:
    print("Você está com obesidade grau I.")

elif imc >= 35.0 and imc <= 39.9:
    print("Você está com obesidade grau II (severa).")

else:
    print("Você está com obesidade grau III (mórbida).")
