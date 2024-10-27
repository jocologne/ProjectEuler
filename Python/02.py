#Problema 02
#Find the sum of the even-valued terms in Fibonacci sequence below 4000000

soma = 0

arr = []
limite = 4000000

arr.append(1)
arr.append(2)

while arr[len(arr) - 1] < limite:
    a = arr[len(arr) - 1]
    b = arr[len(arr) - 2]
    c = a + b
    arr.append(c)
arr.pop(len(arr) - 1)
even=[]
for x in range (0,len(arr)):
    if arr[x] % 2 == 0:
        even.append(arr[x])
for x in range (0,len(even)):
    soma += even[x]
print(soma)