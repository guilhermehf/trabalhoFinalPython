'''''
#Exemplo For
for i in range(5):
    print(i)

'''
'''''    
#Exemplo While
j=0
while j<5:
    print(f"j:",j)
    j=j+1
print("fim")  

'''
'''''
for i in range(3):
    nome=input("Digite um nome:")
    anoNasc=int(input("Digite um ano de nascimento:"))
    print(nome, "tem", 2023 - anoNasc," de idade")

'''

'''''

nome=input("Digite um nome:")
while nome != "FIM":
    anoNasc=0
    while anoNasc <= 1923 or anoNasc >=2024:
        anoNasc=int(input("Digite ano de nascimento do "+nome))
    print(nome, "tem", 2023 - anoNasc, "de idade") 
    nome=input("Digite o proximo nome:")   
    '''
