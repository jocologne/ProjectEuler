#Problema 01
#Find the sum of all the multiples of 3 and 5 below 1000

soma = 0
limite = 1000

for x in range(1,limite):
    if x % 3 == 0 or x % 5 == 0:
        soma = soma + x
print(soma)