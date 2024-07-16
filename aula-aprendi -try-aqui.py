total = 0 

while True:
    entrada = input("Digite um número (ou 'sair' para encerrar o programa): ")

    if entrada.lower() == 'sair':
        break
    
    # try é uma estrutura que pode gerar uma exceção.
    try:
        numero = float(entrada)
        total += numero 
    # except faz parte da estrutura try que é ativada por uma exceção específica.
    except ValueError:
        print("Por favor, digite um número válido.")
    # Bloco finally é executado independentemente de haver exceções ou não.
    finally:
        print("Tentativa de processamento completa.")

print(f"O total das somas foi {total}")
