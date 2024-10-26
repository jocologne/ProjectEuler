#Problema 06

import time


def soma_dos_quadrados(n):
    somaq=0
    while n>=1:
        somaq+=n*n
        n-=1
    return somaq

def quadrado_da_soma(n):
    res=0
    while n>=1:
        res+=n
        n-=1
    return res*res


num=100

t0=time.time()
print(quadrado_da_soma(num)-soma_dos_quadrados(num))
t1=time.time()

print(t1-t0)