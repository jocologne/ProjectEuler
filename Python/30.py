#Problem 30
#Find the sum of all the numbers that can be written as the sum of fifth 
#powers of their digits.

numeros=[]

def soma_quinta(n):
    soma = 0
    numero = str(n)
    for digito in numero:
        soma += int(digito) ** 5
    if soma == n:
        numeros.append(n)

for i in range(2,200000):
    soma_quinta(i)

resultado = 0

for i in numeros:
    resultado += i

print(numeros)
print(resultado)