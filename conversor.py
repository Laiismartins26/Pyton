   #celsius para fahrenheit
def celsius_fahrenheit(c):
    return (c * 9/5) + 32
   #celsius para kelvin
def  celsius_kelvin(c):
    return c + 273.15
   #fahrenheit para kelvin
def  fahrenheit_kelvin(f):
    return (f - 32) * 5/9 + 273.15
   #kelvin para celsius
def   kelvin_celsius(k):
    return k - 273.15
   #kelvin para fahrenheit 
def   kelvin_fahrenheit(k):
    return (k- 273.15) * 9/5 + 32
   #fahrenheit para celsius
def    fahrenheit_celsius(f):
    return (f - 32) * 5/9


# função principal
def conversor():
    print("conversor de temperaturas")
    while True: 
        print("\nEscolha a operação: ")
        print("1 - celsius para fahrenheit")
        print("2 - celsius para kelvin")
        print("3 - fahrenheit para celsius")
        print("4 - fahrenheit para kelvin")
        print("5 - kelvin para celsius")
        print("6 - kelvn para fahrenheit")
        print("7 - sair")
        
        opcao = int(input("Digite o número da operação desejada: "))

        if opcao == 7:
            print("Saindo...")
            break

        if opcao in [1, 2, 3, 4, 5, 6]:
            temperatura = float(input("Digite a temperatura: "))

        if opcao==1: 
            resultado=celsius_fahrenheit(temperatura)
            print(f"{temperatura}° C é igual a {resultado} f" )
        elif opcao==2:
            resultado=celsius_kelvin(temperatura)
            print(f"{temperatura}° C é igual a {resultado} k" )
        elif  opcao==3:
            resultado=fahrenheit_celsius(temperatura)
            print(f"{temperatura}° F é igual a {resultado} c" )
        elif opcao==4:
            resultado=fahrenheit_kelvin(temperatura)
            print(f"{temperatura}° F é igual a {resultado} k" )
        elif opcao==5:
            resultado=kelvin_celsius(temperatura)
            print(f"{temperatura}°  K é igual a {resultado} c" )
        elif opcao==6:
            resultado=kelvin_fahrenheit(temperatura)
            print(f"{temperatura}° K é igual a {resultado} f" )
        else:
            print("Opção inválida.")
        


#inicio do programa
conversor()
