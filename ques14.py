lista = []
x = int(input("Digite um número: "))

for i in range(5):
    num=int(input("Digite um numero: "))
    lista.append(num)

lista.sort(reverse=True)
print(lista)