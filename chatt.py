import os 

mensagens = []

nome = input("nome: ")
while True:

    #limpando o terminal
    os.system('clear')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
    print("_________________")

    # obtendo texto
    
    texto = input("mensagem: ")
    if texto== "fim":
        break

    #adicionando mensagem na lista
    mensagens.append({
    "nome": nome,
    "texto": texto
    })
    