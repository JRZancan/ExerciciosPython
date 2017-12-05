import easygui as eg

menu_options = ["Cadastrar cliente", "Remover cliente", "Sair"]
new_clients_fields = ["CPF/CNPJ", "Nome"]
cliente = dict()
clientes = dict()

while True:
    result = eg.choicebox("Escolha uma opção", "Menu", menu_options)

    if result == menu_options[0]:  # Cadastrar Cliente
        new_cliente = eg.multenterbox("Informe os dados do cliente", "Cadastrar cliente", new_clients_fields)  #Pega os dados do cliente

        cliente["cpfcnpj"] = new_cliente[0]  #Salva o CPF em um objeto "Cliente"
        cliente["nome"] = new_cliente[1]  #Salva o Nome no mesmo objeto "Cliente"

        clientes[new_cliente[0]] = cliente  #Salva o objeto "Cliente" acima, em um objeto "Clientes", com vários outros

    elif result == menu_options[2]:  #Sair
        eg.msgbox("Até mais", "Saindo")
        break

    print(clientes)
