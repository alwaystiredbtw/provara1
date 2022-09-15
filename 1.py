# 3 numeros inteiros e printar o mairo deles 


num = int(input("Digite o primeiro numero:"))
lista = [num]
cont = 0

while cont < 2:
    num = int(input("Digite o proximo numero:"))
    if num > 0:
        lista.append(num)
    cont += 1

print (f"O maior numero eh {max(lista)}")
