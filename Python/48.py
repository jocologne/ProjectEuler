arr=[]

for i in range(1,1000):
    arr.append(i**i)

res = 0

for num in arr:
    res=res+num

#print(arr)
print(res)