
limite = 20000
primos=[]

numeros=[True]*limite
numeros[0]=False
numeros[1]=False

for i in range(0,limite):
    if  numeros[i]:
        primos.append(i)
        #print(i)
        for j in range(i,limite,i):
            numeros[j]=False

#print(primos)
fatores=[]

for numero in primos:
    teste = 600851475143 % numero
    #print(teste)
    if teste == 0:
        fatores.append(numero)

print(fatores)