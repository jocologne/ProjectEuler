limite=2000000
primos=[]

#Inicializa todos os numeros até limite como True.
numeros = [True] * limite
numeros[0]=False
numeros[1]=False

for i in range (0,len(numeros)):
    if numeros[i]:
        print(i)
        primos.append(i)
        for j in range (i,limite,i):
            numeros[j]=False

#Crivo de Eratóstenes marca como false todos os multiplos de i

resultado=0
for p in primos:
    resultado += p

print(resultado)