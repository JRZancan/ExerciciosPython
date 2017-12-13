def imprime(n):
    msg = 'Os valores sao: \n'
    for i in range (0,n+1):
        msg += str(i) + '\t'
    print(msg)

n = int(input("Digite um numero inteiro: "))
imprime(n)