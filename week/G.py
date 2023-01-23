a = int(input())
max = 0
c = []
f = a
while a > 0:
    b = int(input())
    if b > max:
        max = b
    c.append(b)
    a = a - 1
d = ''
e = 1
while len(d) <= max:
    d = d + str(e)
    e = e * 10
cnt = 0
while f > 0:
    print(d[c[cnt] - 1], end = ' ')
    cnt = cnt + 1
    f = f - 1