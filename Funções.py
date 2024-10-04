def ExibirMenu():
    print("CALCULADORA DAS OPERAÇÕES BÁSICAS:\n")
    print("Menu de escolha:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Resto da Divisão")
    print("6. Sair")

    opcao = int(input("Digite a sua opção: "))

    return opcao

def capturaValores():
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    return num1, num2


opcao = 0

while True: 
    opcao = ExibirMenu()

    if opcao in [1, 2, 3, 4, 5]:
       n1, n2 = capturaValores()
    
    if opcao == 1:              
        print(f"A soma dos valores é: {n1 + n2}\n")
    elif opcao == 2:
        print(f"A subtração dos valores é: {n1 - n2}\n")
    elif opcao == 3:
        print(f"A multiplicação dos valores é: {n1 * n2}\n")
    elif opcao == 4:
        if n2 != 0:
            print(f"A divisão dos valores é: {n1 / n2}\n")
        else:
            print("Erro: Divisão por zero não é permitida.\n")
    elif opcao == 5:
        if n2 != 0:
            print(f"O resto da divisão dos valores é: {n1 % n2}\n")
        else:
            print("Erro: Divisão por zero não é permitida.\n")
    elif opcao == 6:
        print("Finalizando o código!")
        break
    else:
        print("Opção inválida. Tente novamente.\n")