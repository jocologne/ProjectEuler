
#Problem 21
#Sum of all amicable numbers under 10000

def sum_of_div(n):
	i = 1
	soma = 0
	while (i <= n / 2):
		if (n % i == 0):
			soma += i
		i = i + 1
	return (soma)

def is_amic(n1, n2):
	if (sum_of_div(n1) == n2 and sum_of_div(n2) == n1 and n1 != n2):
		return 1
	return 0

num = 284
arr = []
res = 0

for i in range (1, 10000):
	if (is_amic(i, sum_of_div(i))):
		arr.append(i)
		res += i

print(arr)
print(res)
