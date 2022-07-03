print("IMC")
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura*altura)
limite = 25
if limite >= imc:
    print("Acima do peso ideal")
else:
    print("está no peso ideal")
print(imc)