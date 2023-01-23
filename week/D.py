a = list(map(int, input().split()))
b = input().split()
c = int(b[1])
if b[0] == 'R':
    d = len(a) - c
if b[0] == 'L':
    d = c
d = len(a) - c
e = []
for x in a:
    e.append(a[d])
    d = d + 1
    if d == len(a):
        break
cnt = 0
for x in a:
    e.append(a[cnt])
    cnt = cnt + 1
    if cnt == c:
        break
for x in e:
    print(x, end = ' ')