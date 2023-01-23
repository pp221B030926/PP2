a = str(input())
b = 0
c = 1
d = 2
ans = ''
for x in a:
    sum = a[b] + a[c] + a[d]
    ans = ans + chr(int(sum))
    b = b + 3
    c = c + 3
    d = d + 3
    if d > len(a):
        break
print(ans)