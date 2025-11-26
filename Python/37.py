def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if (n % i == 0):
            return False
    return True

def truncate_left(n):
    if n > 9:
        st = str(n)
        st = st[1:]
        return int(st)
    return 0
    
def truncate_right(n):
    if n > 9:
        st = str(n)
        st = st[:-1]
        return int(st)
    return 0

add = False
arr = []
n = 11

while (len(arr) < 11):
    print(n)
    if is_prime(n):
        add = True
        nl = truncate_left(n)
        while(nl > 0):
            if not is_prime(nl) and nl > 0:
                add = False
                break
            nl = truncate_left(nl)
        nr = truncate_right(n)
        while(nr > 0):
            if not is_prime(nr) and nr > 0:
                add = False
                break
            nr = truncate_right(nr)
        if add:
            arr.append(n)
    n += 1

print(arr)

soma = 0
for n in arr:
    soma += n

print(soma)