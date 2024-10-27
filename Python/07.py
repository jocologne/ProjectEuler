#Problem 7
#What is the 10001st prime number

import time

t0 = time.time()

limite = 10001
numbers = []
primos = [2]


def gera_impar(i):
    n = 2 * i + 1
    # print(n)
    numbers.append(n)
    return n


def checa_primo(j):
    ind = 2
    divisores = []

    while ind * ind <= j:
        resto = j % ind
        if resto == 0 and j != ind:
            divisores.append(ind)
            break
        ind += 1

    if len(divisores) == 0:
        primos.append(j)
        print("{}.....{} é primo".format(len(primos),j))


while len(primos) < limite:
    gr = gera_impar(len(numbers) + 1)
    checa_primo(gr)

# print(numbers)
# print(primos)

t1 = time.time()

tp = t1 - t0

print(tp)
