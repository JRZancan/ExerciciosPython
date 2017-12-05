import easygui as ei

menu_options = ["Cadastrar cliente", "Remover cliente", "Consultar clientes", "Sair"]
new_clients_fields = ["CPF/CNPJ", "Nome"]
cliente = dict()
clientes = dict()
result = ''
new_client = []
clientes_list = []

while True:
    result = ei.choicebox("Escolha uma opção", "Menu", menu_options)

    if result == menu_options[0]:  # Cadastrar Cliente
        new_cliente = ei.multenterbox("Informe os dados do cliente", "Cadastrar cliente", new_clients_fields)

        cliente["cpfcnpj"] = new_cliente[0]  #Salva o CPF em um objeto "Cliente"
        cliente["nome"] = new_cliente[1]  #Salva o Nome no mesmo objeto "Cliente"

        clientes[new_cliente[0]] = cliente  #Salva o objeto "Cliente" acima, em um objeto "Clientes", com vários outros

    elif result == menu_options[1]:
        if len(clientes) == 0:
            ei.msgbox("Não há clientes cadastrados", "Ops...")
        else:
            clientes_list = list(clientes.keys())
            cpf_do_removido = ei.choicebox("Escolha o CPF/CNPJ do cliente que deseja remover", "Remoção", clientes_list)
            pergunta = ei.ynbox('Tem certeza que deseja remover o cliente ' + cpf_do_removido + '?', "Confirmação")

            if pergunta:
                clientes.pop(cpf_do_removido)
                ei.msgbox("Cliente removido!", "Sucesso!")

    elif result == menu_options[2]:
        clientes_list = list(clientes.keys())
        resposta = ei.choicebox("De qual cliente deseja obter os dados?", "Consulta", clientes_list)
        escolhido = clientes[resposta]
        ei.msgbox('DADOS DO CLIENTE\n\n' + 'CPF: ' + escolhido['cpfcnpj'] + '\nNome: ' + escolhido['nome'])

    elif result == menu_options[3]:  #Sair
        ei.msgbox("Até mais", "Saindo")
        break
