'''''
numUm = int(input("Digite um numero:"))

numDois = int(input("Digite Segundo Numero:"))
print(f"Resposta Numero 1:", numUm)
print(f"Resposta Numero Dois:{numDois}")

'''

'''''
vA = int(input("Digite vA:"))
print(f"resposta vA:", vA)

vB = int(input("Digite vB:"))
print(f"resposta vB:", vB)

vC = vA
vA = vB

print(f"resposta vA:", vC)

print(f"resposta vB:", vA)

'''
'''''
numUm = int(input("Digite um Numero:"))
numDois = int(input("Digite Segundo Numero:"))
soma = int(numUm + numDois)
print(f"Resposta Soma:", soma)

'''
'''''
numUm = int(input("Digite um Numero:"))
numDois = int(input("Digite Segundo Numero:"))
numTres = int(input("Digite terceiro Numero:"))
media = int(numUm+numDois+numTres/3)
print(f"resposta:", media)
'''
'''''
numUm = int(input("Digite um Numero:"))
numDois = int(input("Digite Segundo Numero:"))
numTres = int(input("Digite terceiro Numero:"))
numQuatro = int(input("Digite quarto Numero:"))
numQuinto = int(input("Digite quinto Numero:"))
soma = int(numUm+numDois+numTres+numQuatro+numQuinto)
media = int(soma/5)
print(f"Resposta soma:", soma)
print(f"Resposta Media:", media)

'''

'''
EXERCICIO GABARITO 31/08
'''


#VERIFICADOR DE NUMERO PAR/IMPAR

n = int(input("Digite um numero:"))

if n % 2 == 0:
    print("Par")
else:
    print("Impar")

#CONVERSOR DE TEMPERATURA

unidade = input("Qual unidade de temperatura deseja converter? (Celsius/Fahrenheit):")  
valor = float(input("Digite o valor da temperatura em Celsius:")) 
print(f"{valor} Celsius = {valor * 9/5 + 32} Fahrenheit") 

#DECISAO DE VOTACAO

idade = int(input("Digite sua idade:"))

if idade >= 16:
    print("Você pode votar nas eleições")
else:
    print("Você não pode votar nas eleições")   


#VERIFICADOR DE NUMERO POSITIVO NEGATIVO ZERO

n = (input("Digite um numero:"))    

if n > 0:
    print("Positivo")
elif n < 0:
    print("Negativo")
else:
    print("Zero")    


#VERIFICADOR MAIOR NUMERO

n1 = int(input("Digite um numero:"))
n2 = int(input("Digite o segundo numero:"))

if n1 > n2:
    print(f"O maior numero é {n1}")
else:
    print(f"O maior numero é {n2}")

#CALCULADORA DE IMC

peso = float(input("Digite seu peso (kg):"))
altura = float(input("Digite sua altura (m):"))

imc = peso/ altura **2
print(f"Seu IMC é {imc:.2f}")


 
