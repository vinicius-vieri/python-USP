# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

n = int(input("Digite um número inteiro: "))

adjacente = False

while n > 0 and not adjacente:
    if n % 10 == (n // 10) % 10:
        adjacente = True
    n //= 10
    
if adjacente:
    print("sim")
else:
    print("não")
    
    