import easygui as ei

lista_impares = []


def carregar():
    msg = "Escolha o arquivo que quer carregar"
    title = "Carregamento"
    arquivonome = ei.fileopenbox(msg, title)

    if arquivonome is None:
        return

    arquivo = open(arquivonome, 'r')

    for linhas in arquivo:
        palavras = linhas.split(' ')
        for tamanho in palavras:
            numeros = len(tamanho)
            if numeros % 2 != 0:
                lista_impares.append(tamanho)

    arquivo.close()
    return lista_impares


def salvar(palavras_impares):
    msg = "Escolha onde deseja salvar"
    title = "SALVAR"
    default = "arquivosalvo.csv"

    nomearquivo = ei.filesavebox(msg, title, default)

    if nomearquivo is None:
        return

    arquivo1 = open(nomearquivo, 'w')

    for palavra in palavras_impares:
        texto = palavra + '\n'

        arquivo1.write(texto)


carregar()

salvar(lista_impares)
