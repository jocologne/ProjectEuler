#Implementar um cache para melhorar a eficiencia do codigo

import time

maior=0
vencedor=0


def collatz_even(n):
    n = (n / 2)
    return n

def collatz_odd(n):
    n = (3 * n + 1)
    return n

def collatz(num):
    count = 0
    while num != 1:

        #print(int(num))
        if num % 2 == 0:
            num = collatz_even(num)
            count += 1
        else:
            num = collatz_odd(num)
            count += 1
    return count

t0=time.time()

for i in range(1,1000000+1):
    termos=collatz(i)
    #print("collatz de {} é {}".format(i,termos+1))
    if termos > maior:
        maior = termos
        vencedor = i


t1 = time.time()
tp = t1 - t0


print("{} segundos".format(tp))
print("Maior é {}".format(maior+1))
print("Vencedor é {}".format(vencedor))
