a = input().split()
c = []
for x in a:
    d = len(x)
    while d > 0:
        if (d == 1):
            c.append('YES')
            break
        if (d % 2 != 0):
            c.append('NO')
            break
        d = d / 2
sum = ''
for x in c:
    sum = sum + x + ' '
print(sum)