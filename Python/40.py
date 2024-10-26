n = ''
for i in range (1,200001):
    n = n + str(i)

d1 = n[1-1]
print(d1)
d10 = n[10-1]
print(d10)
d100 = n[100-1]
print(d100)
d1000 = n[1000-1]
print(d1000)
d10000 = n[10000-1]
print(d10000)
d100000 = n[100000-1]
print(d100000)
d1000000 = n[1000000-1]
print(d1000000)

a1 = int(d1)
a10 = int(d10)
a100 = int(d100)
a1000 = int(d1000)
a10000 = int(d10000)
a100000 = int(d100000)
a1000000 = int(d1000000)

sol = a1*a10*a100*a1000*a10000*a100000*a1000000
print(sol)