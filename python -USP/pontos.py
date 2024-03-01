import math

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))

distancia = math.sqrt(((n1 - n3)**2) + ((n2 - n4)**2))

if distancia >= 10:
    print("longe")
else:
    print("perto")
    

