n = int(input("Digite o valor de n: "))

fatorial = 1

if n == 0:
    fatorial = 1
elif n < 0:
    print("Não existe fatorial de número negativo")
else:
    while n > 0:
        fatorial = fatorial * n
        n -= 1
        
print(fatorial)
