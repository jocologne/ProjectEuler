numero = 2 ** 1000

#Recebe um numero num e retrona uma lista tr com cada digito separado.
def divide_numero(num):
    tr = []
    for i in str(num):
        tr.append(int(i))
    return tr


digitos = divide_numero(numero)

soma = 0
for j in digitos:
    soma += j

print(soma)
