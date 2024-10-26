def divisores(n):
    div = []
    limite = round((n/2)+1)
    for i in range(1, limite):
        if (n % i) == 0:
            div.append(i)
    s = 0
    for item in div:
        s = s + item
    print(n)
    print(s)
    if s > n:
        abundante.append(n)

abundante = []

for m in range(1,30000):
    divisores(m)

print(abundante)

