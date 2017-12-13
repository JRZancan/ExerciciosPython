def classifica(idade):
    if idade>=18:
        print ("Sua classificacao e ADULTO")
    elif idade<18 and idade>=14:
        print ("SUa classficacao e JUVENIL")
    elif idade<14 and idade>=9:
        print ("Sua classificacao e INFANTIL")
    elif idade<9:
        print("Sua classificacao e MIRIM")
        
idade=int(input("Digite a idade do nadador: "))
classifica()