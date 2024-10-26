numero = 100

fatorial = 1

while numero > 1:
    fatorial *= numero
    numero -= 1

#print(fatorial)

#Recebe um numero num e retrona uma lista tr com cada digito separado.
def divide_numero(num):
    tr = []
    for i in str(num):
        tr.append(int(i))
    return tr


digitos = divide_numero(fatorial)

soma = 0
for j in digitos:
    soma += j

print(soma)
