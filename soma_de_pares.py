#Soma de pares
numero = int(input("Digite um número: "))

soma_pares = 0
contador = 2

while contador <= numero: 
    soma_pares += contador
    contador += 2

print(f"A soma dos números pares até {numero} é: {soma_pares}")
