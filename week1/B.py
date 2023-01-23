n = int(input())
a = 1
l = []
for i in range(n):
    l.append(input().split())
for i in l:
    c = ''
    for j in i:
        for k in j:
            d = chr(ord(k) + a)
            if d <= 'Z':
                c += d
            if d > 'Z':
                e = chr(ord(d) - 26)
                c += e
    a += 1
    print(c)