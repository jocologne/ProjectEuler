#Problema 01

import time

soma=0
arr=[]
limite = 1000

for x in range(1,limite):
    if x % 3 == 0 or x % 5 == 0:
        arr.append(x)


for x in range(0, len(arr)):
    soma = soma + arr[x]

print(soma)