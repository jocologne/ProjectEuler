numeros=[]

def soma_quinta(n):
    soma = 0
    b = str(n)
    for i in b:
        soma += int(i) ** 5
    if soma == n:
        numeros.append(n)

for i in range(2,1000000):
    soma_quinta(i)

resultado = 0

for i in numeros:
    resultado += i

print(numeros)
print(resultado)