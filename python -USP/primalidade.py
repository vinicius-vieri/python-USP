n = int(input("Digite um número inteiro: "))

primo = True

if n == 0 or n == 1:
    primo = False
else:
    i = 2
    while i < n and primo:
        if n % i == 0:
            primo = False
        i += 1
        
if primo:
    print("primo")
else:
    print("não primo")