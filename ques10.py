lista = []

for i in range(5):
    num=int(input("Digite um numero: "))
    lista.append(num)

for i in range(len(lista)):
    if lista[i]%2==0:
        print("eh par",lista[i])