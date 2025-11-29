
def triangular(n):
    return (n * (n + 1) // 2)

def pentagonal(n):
    return (n * (3 * n - 1) // 2)

def hexagonal(n):
    return (n * (2 * n - 1))

hexa = set()
pent = set()

n = 1
while True:
    t = triangular(n)
    pent.add(pentagonal(n))
    hexa.add(hexagonal(n))

    if t in pent and t in hexa and t > 40755:
        print(t)
        break
    n += 1