#Problema 04

# Para 3 digitos definir inicio em 100 e limite em 1000

inicio = 100
limite = 1000

prd = []
prdinv=[]

for i in range(inicio, limite):
    for j in range(inicio, limite):
        pr = i * j
        prd.append(pr)


# Cria um array prd com todos os produtos dos numeros entre inicio e limite

def inverte_numero(num):
    a = str(num)
    i = len(a)
    b = ""
    while i >= 1:
        b = b + a[i - 1]
        i -= 1
    return int (b)

respostas=[]

for i in prd:
    invertido = inverte_numero(i)
    if i == invertido:
        print(i)
        respostas.append(i)

resposta = 0

for i in respostas:
    if i > resposta:
        resposta = i

print(resposta)

#print(prd)
#print(prdinv)
