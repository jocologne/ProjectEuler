import math
import time

t0=time.time()
num=0

lista = [1]
fatores=0
limite = 500

# Função que adciona um numero a lista
def cria_numero():
    ultimo = lista[len(lista) - 1]
    proximo = ultimo + len(lista) + 1
    lista.append(proximo)
    return proximo

#Função que encontra os divisores de um numero e retorna a quantidade de divisores
def encontra_divisores(numero):
    divisores=[]
    for i in range (1,int(math.sqrt(numero))+1):
        resto=numero%i
        if resto==0:
            divisores.append(i)
            if i!=numero/i:
                divisores.append(numero/i)

    return len(divisores)



while fatores<limite:

    num = cria_numero()
    #print(num)
    fatores=encontra_divisores(num)

print(num)
t1=time.time()
tp=(t1-t0)
print(tp)
