import sys
from collections import Counter
s = list(map(str, sys.stdin.read().split()))
c = ''
for i in s:
    c += i
e = []
c += ' '
a = ''
for i in c:
    if i == ' ':
        e.append(a)
        a = ''
        continue
    a += i
d = dict()
for i in e:
    if i not in d.keys():
        d[i] = 1
    else: d[i] += 1
# d = dict(Counter(s))
for i in sorted(d.values(), reverse = True):
    for j in sorted(d.keys()):
        if d[j] == i:
            j = j + ':'
            print(j,i)