def save(cpf, nome, telefone):
    dados= open('cadastro.txt', 'w')
    for x in range (len(nome)):
        dados.write(cpf[x]+'\t'+ nome[x]+'\t' +telefone[x]+ '\t\n')
    dados.close()
    
cpf=[]
nome=[]
telefone=[]
y='s'

while y=='s':
    no=raw_input("Informe o nome do usuario: ")
    nome.append(no)
    
    t=raw_input("Informe o telefone do usuario: ")
    telefone.append(t)
    
    c=raw_input("Informe o CPF do usuario: ")
    cpf.append(c)
    y=raw_input("Continuar no cadastro? s\n")
    y.lower()
    
if y=='n':
    save(cpf,nome,telefone)