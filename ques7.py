indice = int(input("Digite um numero: "))

a, b = 0, 1
i = 0

while i <= indice:
    print(a, end=" ")
    a, b = b, a+b
    i += 1