
def is_prime(n):
	i = 2
	while (i * i < n):
		if (n % i == 0):
			return False
		i += 1
	return True

prime = []
for i in range (1000, 10000):
	if (is_prime(i)):
		prime.append(i)

#Array prime com todos os primos de 4 digitos.
print(prime)