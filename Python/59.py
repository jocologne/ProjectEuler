import time

inicio = time.time()

resp = ''

cifra =[]
file = open('files/cipher.txt')
file = file.readline()
c = file.split(',')
for item in c:
    cifra.append(int(item))

print(len(cifra))

chr_key = []
int_key = []

for i in range(97,123):
    for j in range(97,123):
        for k in range(97,123):
            chr_key.append(chr(i)+chr(j)+chr(k))
            int_key.append([i,j,k])

#print(cifra)

for chave in int_key:
    texto = ''
    for j in range(0,len(cifra),3):
        for i in range(0,3):
            car = cifra[j+i] ^ chave[i]
            texto = texto + chr(car)
    if ' the' in texto and ' and ' in texto and ' of ' in texto:
        print(texto)
        resp = texto
        print(chave)
        print(chr(chave[0])+chr(chave[1])+chr(chave[2]))

#print(resp)
arr = []

for letra in resp:
    arr.append(ord(letra))
#print(arr)

s = 0
for n in arr:
    s = s + n
print("A soma dos caracteres é")
print(s)

fim = time.time()
tempo = fim - inicio
print(tempo)