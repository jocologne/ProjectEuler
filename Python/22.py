dict = {"A":1,
        "B":2,
        "C":3,
        "D":4,
        "E":5,
        "F":6,
        "G":7,
        "H":8,
        "I":9,
        "J":10,
        "K":11,
        "L":12,
        "M":13,
        "N":14,
        "O":15,
        "P":16,
        "Q":17,
        "R":18,
        "S":19,
        "T":20,
        "U":21,
        "V":22,
        "W":23,
        "X":24,
        "Y":25,
        "Z":26,}

f = open('files/names.txt')

for line in f.readlines():
    linha = line.replace('\n', '')

ln = linha.replace('"','')
arr = ln.split(',')
arr.sort()

scores = []

for item in arr:
    nome = item
    s = 0
    for letra in nome:
        s = s + dict[letra]
    scores.append(s)

#print(arr)
#print(scores[2])
total = 0
for i in range(0, len(scores)):
    res = scores[i] * (i + 1)
    total = total + res

print(total)
