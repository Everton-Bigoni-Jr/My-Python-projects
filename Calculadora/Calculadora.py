print("-------------------------------------------------")
print("Calculator by @evertin_bg " " - " " Hello World")
print("-------------------------------------------------")

print("***************************************************")
print("***************************************************")

while True:

    print("------------------------------------")
    print("Olá! Seja bem-vindo à calculadora :)")
    print("------------------------------------")

    # Entrando com os números
    print("Entre com seus números")
    n1 = float(input("Escreva o primeiro número: "))
    n2 = float(input("Escreva o segundo número: "))

    # Escolhendo a operação
    print("------------------------------------")
    print("1) Digite 1 para Adição")
    print("2) Digite 2 para Subtração")
    print("3) Digite 3 para Multiplicação")
    print("4) Digite 4 para Divisão")
    print("------------------------------------")

    operacao = int(input("Escolha sua operação: "))

    print("------------------------------------")

    # SE - SENÃO para calcular o resultado
    if operacao == 1:
        resultado = n1 + n2
        print("✅ Sua soma é igual a:", resultado)

    elif operacao == 2:
        resultado = n1 - n2
        print("✅ Sua subtração é igual a:", resultado)

    elif operacao == 3:
        resultado = n1 * n2
        print("✅ Sua multiplicação é igual a:", resultado)

    elif operacao == 4:
        if n2 != 0:
            resultado = n1 / n2
            print("✅ Sua divisão é igual a:", resultado)
        else:
            print("❌ Erro: não é possível dividir por zero!")

    else:
        print("⚠️ Erro: operação inválida!")

    print("------------------------------------")

    # Pergunta se o usuário quer continuar
    continuar = input("Deseja fazer outro cálculo? (s/n): ").lower()
    if continuar != "s":
        print("-------------------------------------------------")
        print("Encerrando a calculadora... Até mais! 👋")
        print("-------------------------------------------------")
        break                 