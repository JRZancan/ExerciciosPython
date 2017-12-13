def MAIOR(vet,n):
    x=vet[0]
    for i in range(len(vet)):
        if x<vet[i]:
            x=vet[i]
    return x
    
def MENOR(vet,n):
    y=vet[0]
    for i in range(len(vet)):
        if y>vet[i]:
            y=vet[i]
    return y 
    
def POSITIVO(vet,n):
    positivo=0
    for i in range (n):
        if vet[i]>0:
            positivo+= 1
    return positivo

def ORDENA(vet,n):
    vet.sort()
    return vet
