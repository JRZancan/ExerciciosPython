import easygui as ei

impares = []


nome_arquivo = ei.fileopenbox("Escolha o arquivo que deseja abrir", "Aqruivo" )
arquivo = open(nome_arquivo,'r')

for linha in arquivo:
    linha=linha.split(' ')
    for palavra in linha:
       if len(palavra)%2 == 1:
            impares.append(palavra)

arquivo_saida = ei.filesavebox("Onde deseja salvar?","Salvar")
final = open(arquivo_saida, 'w')

for palavra in impares:
    linha = palavra + '\n'
    final.write(linha)