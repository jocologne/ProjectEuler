#Problem 29
#How many distinct terms are in the sequence generated by a**b (2,100)

limite = 100
arr = []
for i in range (2, limite + 1):
	for j in range (2, limite + 1):
		arr.append(i**j)
arr.sort()
print(len(set(arr)))