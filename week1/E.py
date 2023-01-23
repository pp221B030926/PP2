n = int(input())
d = dict()
for i in range(n):
    l = str(input())
    d[l] = 0
m = int(input())
for i in range(m):
    k = str(input())
    d[k] += 1
for i in d.keys():
    for j in d.values():
        if d[i] == j:
            if j > float(m * 0.07):
                print(i)