# Voto obrigatório

nome = input("Digite seu nome:")
idade = float(input("Digite sua idade:"))

if (idade >=18 and idade <=64):
    print(nome, "seu voto é obrigatório.")
elif (idade>= 16):
      print(nome, " o seu voto é opcional.")
else:
    print (nome, "você não pode votar.")