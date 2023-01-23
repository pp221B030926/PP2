a = input()
d = dict()
a = a.lower()
b = 97
for i in range(0,26):
    d[chr(b)] = 0
    b += 1
for i in a:
    for j in i:
        if j in d.keys():
            d[j] += 1
for i,j in d.items():
    print(f'{i}: {j}')