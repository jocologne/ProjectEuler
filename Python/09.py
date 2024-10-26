import math

trip = []
limite = 1000

for a in range(1, limite):
    for b in range(1, limite):
        cc = a ** 2 + b ** 2
        c = math.sqrt(cc)
        d = c - int(c)
        if d == 0 and a + b + c == 1000:
            # trip.append([a,b,c])
            print(a * b * c)

print("Fim")
