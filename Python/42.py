
def letter_value(ch):
    return ord(ch) - 64

with open("files/0042_words.txt", "r") as file:
    words = file.read().replace('"', '').split(',')

arr = []
n = 1
while n < 50:
    t = (n * (n + 1) / 2)
    arr.append(int(t))
    n += 1

res = 0
for word in words:
    sm = 0
    for letter in word:
        sm += letter_value(letter)
    for n in arr:
        if sm == n:
            res += 1

print(res)
