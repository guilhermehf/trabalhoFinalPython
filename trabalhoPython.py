'''
#inicialização das listas
alunos=['Jean','Alves','Bianca','Isadora','juliano']
idades=[12,15,18,21,10]
def menu():
    while True:
        print("Escolha uma Opção:")
        print("   ")
        print("1 adicionar alunos e suas idades")
        print("2 listar alunos e idades")
        print("3 Calcular a média de idade dos participantes")
        print("4 Listar por classificação de idade")
        print("5 Listar um aluno e sua classificação")
        print("10 Encerra o programa")
        try:
            opcaof=int(input("\n Digite a Opção"))
            return(opcaof)
        except:
            print("Digite somente numeros")
def adiciona():
    print("******** Adiciona Alunos e Idades *********")
    nome=input("Digite o nome de um aluno")
    idade=int(input("Digite a idade de "+nome+": "))
    alunos.append(nome)
    idades.append(idade)
def listar(parar):
        print("************** Listar Listas ********")
        print("Nome    Idade")
        for i in range(len(alunos)):
            print(alunos[i]," ",idades[i])
        print("******************************\n")
        if parar =='S':
            input("[ENTER] para continuar!")
def media():
    mediaIdades = sum(idades)/len(idades)
    listar('N')
    print("Media dos alunos = ", mediaIdades)
    input("[ENTER] para Continuar!")
# inicio do Programa
while True:
    opcao   = men
u()
    if opcao==10:
        break
    elif opcao==1:
        adiciona()
    elif opcao==2:
        listar('S')
    elif opcao==3:
        media()
print ("Programa FINALIZADO!")  

'''


alunos=[]
idades=[]
pesos=[]
alturas=[]
imc=[]
def menu():

    while True:
        print(" 1 - Incluir Aluno:")
        print(" 2 - Listar todos alunos e seus dados")
        print("Listar dados do aluno")
        print("Listar dados dos alunos de uma determinada idade")
        print("10 - Encerrar Programa")
        try:
            opcaof=int(input("\n Digite a opcao:"))
            return opcaof
        except:
            print("Digite somente numeros!")    


def incluirAluno():
    print("********Adicionar Aluno nome,idade,peso,altura e imc= peso /(Altura*Altura)")
    nome = input("Digite o nome do aluno:")
    idade = int(input("Digite a idade do aluno:"))
    peso = float(input("Digite o peso do aluno:"))
    altura = float(input("Digite a altura do aluno:"))
    alunos.append(nome)
    idades.append(idade)
    pesos.append(peso)
    alturas.append(altura)
    imc.append(peso/(altura*altura))

def listarAluno():
    print('***********Listar Alunos ****************')
    for i in range(len(alunos)):
        print(alunos[i])
        print(idades[i])
        print(pesos[i])
        print(alturas[i])
        print(imc[i])
        print("**************")

       


#inicio do programa

while True:
    opcao = menu()

    if opcao == 10:
        break 

    if opcao == 1:
        incluirAluno()  

    if opcao == 2:
        listarAluno() 