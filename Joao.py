import easygui as ei

lista = []
lista_impares = []
listanumeros = []


def carregar(lista):
    msg = "Escolha o arquivo que quer carregar"
    title = "Carregamento"
    arquivonome = ei.fileopenbox(msg, title)

    if arquivonome is None:
        return

    arquivo = open(arquivonome, 'r')

    for linhas in arquivo:
        palavras = linhas.split(',')
        for tamanho in palavras:
            numeros = len(tamanho)
            listanumeros.append(numeros)

            if numeros % 2 != 0:
                lista_impares.append(tamanho)

    arquivo.close()
    return lista_impares


x = carregar(lista)

print(x)