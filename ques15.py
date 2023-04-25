lista = []

for i in range(5):
    num=int(input("Digite um numero: "))
    lista.append(num)
    
x = int(input("Digite um número para verificação: "))

if x in lista:
    print("O número", x, "está na lista!")
else:
    print("O número", x, "não está na lista.")