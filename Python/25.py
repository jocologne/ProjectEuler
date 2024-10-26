digitos=1

def conta_digitos(n):
    a = len(str(n))
    return a

fib=[1,1]

while digitos < 1000:
    ultimofib = fib[len(fib)-1]
    penultimofib = fib[len(fib)-2]
    proximo = ultimofib + penultimofib
    digitos = conta_digitos(proximo)
    if digitos == 1000:
        print("{} tem 1000 digitos".format(proximo))
    fib.append(proximo)

print(len(fib))