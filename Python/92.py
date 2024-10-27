#Problem 92
#How many starting numbers below ten million will arrive at 89 whem
#continuously adding the square of the digits in a number
import time
def aplica_regra(n):
    s = 0
    nm = str(n)
    for d in nm:
        s = s + (int(d) * int(d))
    #print(s)
    return s

stime = time.time()

limite = 10000001
res = 0

c89 = []
c1 = []

for i in range(1,limite):
    n = i
    while True:
        if n == 1:
            c1.append(i)
            break
        if n == 89:
            c89.append(i)
            print(str(i)+' é 89')
            res = res + 1
            break
        n = aplica_regra(n)

print('O resultado é: '+ str(res))

#print(c1)
#print(c89)

etime = time.time()

t = etime-stime
print(t)