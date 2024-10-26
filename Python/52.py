def checa_numero(n):
    corr = ''
    nn = str(n)
    for i in range(0, 10):
        if str(i) in nn:
            corr = corr + '1'
        else:
            corr = corr + '0'
    return (corr)

ver = True
m = 0
while ver:
    m += 1
    a = 2 * m
    b = 3 * m
    c = 4 * m
    d = 5 * m
    e = 6 * m

    mm = checa_numero(m)
    aa = checa_numero(a)
    bb = checa_numero(b)
    cc = checa_numero(c)
    dd = checa_numero(d)
    ee = checa_numero(e)

    if mm == aa and mm == bb and mm == cc and mm == dd and mm == ee:
        print(m)
        ver = False