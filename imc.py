# IMC = peso/altura² ou altura*altura
   
peso = float(input("Digite o valor do seu peso (kg): "))
altura = float(input("Digite o valor da sua altura (m):"))
imc = peso/(altura**2)

print("Seu IMC é: ", imc)

if(imc<18.5):
    print("Abaixo do peso")
elif(imc<25):
    print("\n Peso normal")
elif(imc<30):
    print("\n Acima do peso")
else:
    print("\n Obesidade")