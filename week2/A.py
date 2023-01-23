import re
n = int(input())
d = dict()
for i in range(n):
    l = input().split()
    c = len(l) - 2
    a = 2
    if l[0] not in d.keys():
        d[l[0]] = ''
    if l[1] == 'add':
        while c > 0:
            d[l[0]] += l[a] + ' '
            a += 1
            c -= 1
    if l[1] == 'drop':
        while c > 0:
            for v in d.values():
                re.sub(l[a],'', string)
            a += 1
            c -= 1
for i in sorted(d.keys()):
    for j in d.values():
        if d[i] == j:
            print(i,':',j)