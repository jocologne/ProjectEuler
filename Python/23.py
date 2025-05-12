#Ainda não esta completo, o array abundantes contem todos os numeros
#abundantes até 30000. 

def divisores(n):
    div = []
    limite = round((n/2)+1)
    for i in range(1, limite):
        if (n % i) == 0:
            div.append(i)
    s = 0
    for item in div:
        s = s + item
    if s > n:
        abundante.append(n)

abundante = []
somas = []

for m in range(1,30000):
    divisores(m)

for num in abundante:
    for num2 in abundante:
        if (num + num2) < 28123:
            somas.append(num + num2);
            print(num+num2)


somas = set(somas)

res = 0
for i in range(1,28123):
    if i not in somas:
        res = res + i
        print(res)