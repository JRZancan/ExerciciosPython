orq = open("ordena.txt", 'r')

vet = ""
todosaux=[]

for linha in orq:
    aux = linha.split(";")
    for item in aux:
        if item != "\n" and item != "":
            todosaux.append(item)

todosaux.sort()

for item in todosaux:
    vet += str(item) + ";"

orq.close()

arq = open("ordena.txt",'w')
arq.write(vet)
arq.close()












