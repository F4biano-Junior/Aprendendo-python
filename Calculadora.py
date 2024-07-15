def calculadora():
    while True:
        print("Escolha uma ação:")
        print("1. Somar        2. Subtrair")
        print("3. Multiplicar  4. Dividir")
        print("5. Sair")

        escolha = input("Digite o número da ação desejada: ")

        if escolha == '5':
            print("Saindo da calculadora.")
            break
        elif escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}\n")
            elif escolha == '2':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}\n")
            elif escolha == '3':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}\n")
            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}\n")
                else:
                    print("Erro: Divisão por zero não é permitida.\n")
        else:
            print("Escolha inválida, por favor tente novamente.\n")
