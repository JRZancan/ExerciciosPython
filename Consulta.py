cod = str(input("Digite o codigo do produto: "))
arq = open("produto.txt", 'r')
orq = open("fornecedor.txt", 'r')
p1 = dict()
f1 = dict()



for linha in arq:
    vet = linha.split(";")
    produto = {"codigop": vet[0], "nomep": vet[1], "preco": vet[2], "codigof": vet[3]}
    p1[vet[0]] = produto

for linha in orq:
    vet = linha.split(";")
    fornecedor = {"codigof": vet[0], "nomef": vet[1]}
    f1[vet[0]] = fornecedor

arq.close()
orq.close()

if cod in p1:
    produtobuscado = p1[cod]
    codigofornecedor = produtobuscado["codigof"]
    fornecedorbuscado = f1[codigofornecedor]

    print("Nome do produto: " + produtobuscado["nomep"])
    print("Preco do produto: " + produtobuscado["preco"])
    print("Nome do fornecedor: " + fornecedorbuscado["nomef"])
else:
    print("Produto nao cadastrado")



