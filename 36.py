def inverte_numero(num):
    a = str(num)
    i = len(a)
    b = ""
    while i >= 1:
        b = b + a[i - 1]
        i -= 1
    return int (b)

def binario(num):
    if num == 0:
        return 0
    res = 0
    place = 1
    while num > 0:
        res += (num % 2) * place
        num = num // 2
        place *= 10
    return res


res = 0
for i in range(1, 1000000):
	if(i == inverte_numero(i) and binario(i) == inverte_numero(binario(i))):
		res += i
print("A soma dos números palíndromos é: ", res)