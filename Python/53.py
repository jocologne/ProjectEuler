def factorial(n):
	res = 1
	while (n > 1):
		res = res * n
		n = n - 1
	return (res)

def comb(n, r):
	c = factorial(n)/(factorial(r)*factorial(n - r))
	return (c)

lim = 100
i = 1
g = 0

while (i <= lim):
	j = 1
	while (j <= lim):
		if comb(i , j) > 1000000:
			g += 1
		j += 1
	i += 1

print(g)
