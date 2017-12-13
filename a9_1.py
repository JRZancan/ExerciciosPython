def written(n, lista):
    arq= open('ordena.txt', 'w')
    for x in range(n):
        arq.write(str(lista[x]) + '\n')
    arq.close()
    
lista=[]
n=10

for x in range (n):
    num=float(input("Informe um numero: "))
    lista.append(num)
written(n, lista)