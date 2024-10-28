#problem 34
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

dit = {'1': 1,
       '2': 2,
       '3': 6,
       '4': 24,
       '5': 120,
       '6': 720,
       '7': 5040,
       '8': 40320,
       '9': 362880,
       '0': 1}

arr = []
for i in range(3, 100001):
    n = str(i)
    print(n)
    s = 0
    for d in n:
        s = s + (dit[d])
    if int(n) == s:
        arr.append(n)

print(arr)