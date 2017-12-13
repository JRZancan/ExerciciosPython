import easygui as ei


str1 = "Ola"

oi = int(str1)

print (oi)

def carregar():
    soma = 0
    msg = "Abra o arquivo"
    title = "SOME"

    arquivonome = ei.fileopenbox(msg, title)

    if arquivonome is None:
        return

    arquivo = open(arquivonome, "r")

    for linhas in arquivo:
        lista = linhas.split(" ")

        for numero in lista:
            try:
                numero_atual = float(numero)
                print("OK:" + str(numero_atual))
            except ValueError:
                numero_atual = 0

        #soma) = float(soma) + float(numero)
            #print(numero)
    arquivo.close()
    return soma


def salvar(lista):

    msg = "Escolha onde salvar"
    title = "SALVAR"
    default = "Soma.csv"
    nomearquivo = ei.filesavebox(msg,title,default)

    if nomearquivo is None:
        return

    arquivo = open(nomearquivo,'w')

    arquivo.write(lista)
    arquivo.close()

x = carregar()

salvar(x)
