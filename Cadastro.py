cadastro = []
vet = []
final = ""
finalmesmo = ""


while True:
    nome=str(input("Digite o nome do cliente: "))
    cpf=str(input("Digite o cpf do cliente: "))
    tel=str(input("Digite o telefone do cliente: "))

    cliente = {"nome": nome, "cpf": cpf, "tel": tel}
    cadastro.append(cliente)

    continuar=str(input("Deseja continuar? s/n: "))

    if continuar == "n":
        break


arq=open("cadastro.txt", 'w')

for pessoa in cadastro:
   final += pessoa["nome"] + ";" + pessoa["cpf"] + ";" + pessoa["tel"] + "\n"

arq.write(final)
arq.close()

exc = str(input("Digite o cpf excluido: "))

arq=open("cadastro.txt", 'r')

for linha in arq:
    vet.append(linha)

arq.close()

for i in range(0, len(vet)):
    dados = vet[i].split(";")
    if dados[1] == exc:
        vet.pop(i)
        break

for item in vet:
    finalmesmo += str(item)

arq=open("cadastro.txt", 'w')

arq.write(finalmesmo)

arq.close()