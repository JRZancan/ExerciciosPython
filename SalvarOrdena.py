cont = 0
numeros = []
vet = ""
while cont <= 10:
    n = float(input("DIgite um numero: "))
    numeros.append(n)
    cont = cont+1

for n in numeros:
    vet += str(n)+";"

arq = open("ordena.txt", 'w')
arq.write(vet)
arq.close()
