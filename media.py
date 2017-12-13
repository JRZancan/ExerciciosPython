def media(n1,n2,n3):
    nota=(n1+n2+n3)/3
    if nota>=6:
        print ("Aprovado e sua nota e: " +str(nota)+ ".")
    if nota<6 and nota>=4:
        print ("Final e sua nota e: " +str(nota)+ ".")
    if nota<4:
        print ("Reprovado e sua nota e: " +str(nota)+ ".")
        
n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
n3=float(input("Digite a terceira nota: "))
media(n1,n2,n3)