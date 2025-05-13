def somadigitos(n):
	nn = str(n)
	soma = 0
	for i in range(0, len(nn)):
		soma += int(nn[i])
	return soma

res = 0;
for i in range(1,100):
	for j in range(1,100):
		soma = somadigitos(i ** j)
		if soma > res:
			res = soma
print(res)
