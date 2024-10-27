arr = []

with open('files/0102_triangles.txt') as file:
    for line in file:
        a = line.replace('\n', '')
        b = a.split(',')
        for n in b:
            num = int(n)
            arr.append(num)

#print(arr)

triangulos = []
for i in range(0,len(arr),6):
    triangulos.append([arr[i],arr[i+1],arr[i+2],arr[i+3],arr[i+4],arr[i+5]])

s = 0

for t in triangulos:
    #ponto 1
    x1 = t[0]
    y1 = t[1]
    # ponto 2
    x2 = t[2]
    y2 = t[3]
    # ponto 3
    x3 = t[4]
    y3 = t[5]

    pc1_2 = x1 * y2 - x2 * y1
    pc2_3 = x2 * y3 - x3 * y2
    pc3_1 = x3 * y1 - x1 * y3

    if pc1_2 > 0 and pc2_3 > 0 and pc3_1 > 0:
        s += 1
    if pc1_2 < 0 and pc2_3 < 0 and pc3_1 < 0:
        s += 1

print(s)
print(len(triangulos))