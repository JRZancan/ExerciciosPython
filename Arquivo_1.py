import easygui as ei

nome_arquivo = ei.fileopenbox("Escolha o arquivo que deseja abrir", "Aqruivo")

print(nome_arquivo)

coisa = open(nome_arquivo, 'r')
impares = []
for item in coisa:
    linha_atual = item.split(" ")

    for palavra in linha_atual:
        palavra.strip()  #Remove TABs e whitespaces da palavra, que atrapalham a contagem de caracteres
        if palavra != "\n":  #Verifica se a "palavra" não é apenas um "\n"
            tamanho = len(palavra)

            if tamanho % 2 != 0:
                impares.append(palavra)

arquivo_saida = ei.filesavebox("Onde deseja salvar?", "Salvar")

final = open(arquivo_saida, 'w')

for palavra in impares:
    linha = palavra + '\n'
    final.write(linha)
