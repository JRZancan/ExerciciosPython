import pylab as py


n = int(input('Informe o numero de pontos:'))

x0 = []
A=[]
for i in range(0,n):
    print ('Informe x[%i]: '%i)
    x0.append(float(input()))

y0 = []
B = []
for i in range(0,n):
    print ('Informe y[%i]: '%i)
    y0.append(float(input()))

for i in range(n):
    aux=[]
    for j in range(n):
        if j==0:
            aux.append(x0[i])
        if j==1:
            aux.append(1)
    A.append(aux)
print(A)

for i in range(n):
    aux=[]
    aux.append(y0[i])
    B.append(aux)


A = py.array(A)
b = py.array(B)

z = py.solve(A, b)

print(z)

x1= float(input('Informe um valor para interpolar: '))
for i in z:
    y=x1*z[0]+z[1]

print(y)