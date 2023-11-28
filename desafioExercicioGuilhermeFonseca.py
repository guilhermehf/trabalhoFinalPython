''''

def verificar_idade():
    anoNasc = int(input("Digite data de nascimento:"))

    if anoNasc >= 18:
        print("Maior de 18 anos")

    elif anoNasc <= 18:
        print("Menor de idade")    


verificar_idade()

'''

'''
def conversor_moeda(cn,ie):

    cr = int(cn * ie)/2

    print("Calcular moeda:",cr)


conversor_moeda(100,5.0)

'''

'''
def eh_par(x):

if x == x*2%0:
  
  print("True")
else:
    print("False")


eh_par(2)

'''



